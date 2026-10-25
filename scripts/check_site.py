"""Check generated navigation, translations, metadata, and source correspondence."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build_site import DOCUMENTS, OUTPUT, ROOT, read_document, read_metadata, render_markdown


class PageInspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.language = None
        self.title_count = 0
        self.language_switches = 0

    def handle_starttag(self, tag, attributes):
        values = dict(attributes)
        if tag == "html":
            self.language = values.get("lang")
        if tag == "h1":
            self.title_count += 1
        if values.get("id"):
            identifier = values["id"]
            assert identifier not in self.ids, f"Duplicate ID: {identifier}"
            self.ids.add(identifier)
        if "language-switch" in values.get("class", "").split():
            self.language_switches += 1
        for name in ("href", "src"):
            if name in values:
                self.links.append(values[name])


def check():
    metadata = read_metadata()
    pages = sorted(OUTPUT.rglob("*.html"))
    assert len(pages) == 8, "Expected exactly 8 generated pages"
    inspectors = {}
    for path in pages:
        content = path.read_text(encoding="utf-8")
        inspector = PageInspector()
        inspector.feed(content)
        inspectors[path.resolve()] = inspector
        language = "en" if path.parent.name == "en" else "ja"
        assert inspector.language == language, path
        assert inspector.title_count == 1, path
        assert inspector.language_switches == 1, path
        assert metadata["version"] in content and metadata["status"] in content, path
        filename = next(name for name, value in DOCUMENTS.items() if value[0] == path.name)
        _, translations = read_document(filename)
        assert render_markdown(translations[language]) in content, "Source mismatch"

    for path, inspector in inspectors.items():
        for link in inspector.links:
            parts = urlsplit(link)
            if parts.scheme or parts.netloc:
                assert parts.scheme in {"http", "https", "mailto"}, link
                continue
            target = (path.parent / unquote(parts.path)).resolve() if parts.path else path
            assert target.is_relative_to(OUTPUT.resolve()), f"Link escapes output: {link}"
            assert target.is_file(), f"Missing target: {path}: {link}"
            if parts.fragment:
                assert target in inspectors, f"Fragment on non-HTML file: {link}"
                assert unquote(parts.fragment) in inspectors[target].ids, link

    source_files = [ROOT / name for name in DOCUMENTS]
    source_files += [ROOT / "assets/style.css", *sorted((ROOT / "scripts").glob("*.py"))]
    for path in source_files:
        raw = path.read_bytes()
        assert not raw.startswith(b"\xef\xbb\xbf"), f"Unexpected BOM: {path}"
        assert b"\r" not in raw and raw.endswith(b"\n"), path
        raw.decode("utf-8")
    print("PASS: 8 pages, language links, internal links, metadata, source correspondence, UTF-8/LF")
    print("External URLs and live Pages publication require separate verification.")


if __name__ == "__main__":
    check()
