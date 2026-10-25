"""Generate both languages from the same four authoritative Markdown files.

No document body is stored in a display template. Metadata belongs to AGENTS.md;
the HTML is disposable and is never committed back into the source repository.
"""

from __future__ import annotations

import html
import os
from pathlib import Path
import re
import shutil

import markdown
import yaml


# ==========================================
# Source documents and metadata
# ==========================================

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "_site"
REPOSITORY_URL = "https://github.com/kojikomatsuzaki/development-standards"
DOCUMENTS = {
    "README.md": ("index.html", "概要", "Overview"),
    "AGENTS.md": ("agents.html", "開発規約", "Standards"),
    "DECISIONS.md": ("decisions.html", "設計判断", "Decisions"),
    "CHANGELOG.md": ("changelog.html", "変更履歴", "Changelog"),
}


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate keys instead of silently replacing an earlier value."""


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node)
    return result


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def read_document(filename):
    text = (ROOT / filename).read_text(encoding="utf-8")
    metadata = {}
    if text.startswith("---\n"):
        _, header, text = text.split("---\n", 2)
        metadata = yaml.load(header, Loader=UniqueKeyLoader)
    boundary = r"^<!-- language: (ja|en) -->$"
    markers = re.findall(boundary, text, flags=re.MULTILINE)
    if markers != ["ja", "en"]:
        raise ValueError(f"Expected exactly one Japanese and English section: {filename}")
    _, _, japanese, _, english = re.split(boundary, text, flags=re.MULTILINE)
    if not japanese.strip() or not english.strip():
        raise ValueError(f"Empty translation: {filename}")
    return metadata, {"ja": japanese, "en": english}


def read_metadata():
    metadata, _ = read_document("AGENTS.md")
    required = {
        "version", "status", "established", "revised", "author",
        "authoritative_language", "approval_record",
    }
    if required - metadata.keys():
        raise ValueError("Missing standards metadata")
    if not re.fullmatch(r"\d+\.\d+\.\d+", metadata["version"]):
        raise ValueError("Invalid semantic version")
    if metadata["status"] not in {"Draft", "Approved"}:
        raise ValueError("Invalid status")
    if metadata["status"] == "Approved" and not metadata["approval_record"]:
        raise ValueError("Approved requires a human approval record")
    for key in ("established", "revised"):
        from datetime import date
        date.fromisoformat(metadata[key])
    return metadata


# ==========================================
# Presentation adapter
# ==========================================

def render_markdown(source):
    # Resolve local source links only in href attributes, not inside code examples.
    rendered = markdown.markdown(
        source, extensions=["tables", "fenced_code", "toc"], output_format="html"
    )
    for filename, (destination, _, _) in DOCUMENTS.items():
        rendered = rendered.replace(f'href="{filename}"', f'href="{destination}"')
    return rendered


def render_page(filename, language, metadata, reference):
    _, sections = read_document(filename)
    english = language == "en"
    output_name, japanese_title, english_title = DOCUMENTS[filename]
    title = english_title if english else japanese_title
    prefix = "../" if english else ""
    other_language_url = prefix + output_name if english else "en/" + output_name
    labels = {
        "version": "Version" if english else "バージョン",
        "revised": "Revised" if english else "改訂日",
        "established": "Established" if english else "制定日",
        "source": "Source on GitHub" if english else "GitHubの原文",
        "history": "Document history" if english else "文書の変更履歴",
    }
    navigation = "".join(
        f'<a href="{destination}"'
        + (' aria-current="page"' if document == filename else "")
        + f'>{en_title if english else ja_title}</a>'
        for document, (destination, ja_title, en_title) in DOCUMENTS.items()
    )
    esc = html.escape
    draft_notice = (
        "Draft · Not approved. No license has been selected."
        if english else "草案（Draft）・未承認です。ライセンスは未決定です。"
    )
    approved_notice = (
        "Approved · See the approval record; check README for license status."
        if english else "承認済み（Approved）・承認記録とREADMEの利用条件を確認してください。"
    )
    notice = draft_notice if metadata["status"] == "Draft" else approved_notice
    approval_link = ""
    if metadata["approval_record"]:
        record = metadata["approval_record"]
        if not isinstance(record, str) or not record.startswith("https://github.com/"):
            raise ValueError("Approval record must be an explicit GitHub URL")
        approval_link = f'<p><a href="{esc(record, quote=True)}">Approval record / 承認記録</a></p>'
    commit_link = (
        f'<a href="{REPOSITORY_URL}/commit/{reference}">{reference[:12]}</a>'
        if reference != "main" else "Local preview / ローカル確認"
    )
    return f'''<!doctype html>
<html lang="{language}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="共通開発規約 / Shared development standards">
  <title>{esc(title)} | Development Standards</title>
  <link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
  <a class="skip-link" href="#content">{'Skip to content' if english else '本文へ移動'}</a>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="index.html">共通開発規約<span>Development Standards</span></a>
      <div class="header-actions">
        <a class="language-switch" href="{other_language_url}" lang="{'ja' if english else 'en'}" hreflang="{'ja' if english else 'en'}">{'日本語' if english else 'English'}</a>
        <details class="site-menu">
          <summary><span aria-hidden="true">☰</span> {'Menu' if english else 'メニュー'}</summary>
          <nav class="menu-panel" aria-label="{'Site menu' if english else 'サイト内メニュー'}">{navigation}</nav>
        </details>
      </div>
    </div>
    <nav class="container document-tabs" aria-label="{'Documents' if english else '文書'}">{navigation}</nav>
  </header>
  <div class="container">
    <aside class="standards-metadata" aria-label="{'Standards metadata' if english else '規約情報'}">
      <p class="status">{esc(notice)}</p>
      <dl>
        <div><dt>{labels['version']}</dt><dd>{esc(metadata['version'])}</dd></div>
        <div><dt>Status</dt><dd>{esc(metadata['status'])}</dd></div>
        <div><dt>{labels['revised']}</dt><dd><time datetime="{metadata['revised']}">{metadata['revised']}</time></dd></div>
        <div><dt>{labels['established']}</dt><dd>{metadata['established']}</dd></div>
      </dl>
      <p class="author">{esc(metadata['author'])} · Authoritative Language: {esc(metadata['authoritative_language'])}</p>
      {approval_link}
    </aside>
    <main id="content" tabindex="-1">{render_markdown(sections[language])}</main>
    <footer>
      <p><a href="{REPOSITORY_URL}/blob/{reference}/{filename}">{labels['source']}</a> · <a href="{REPOSITORY_URL}/commits/{reference}/{filename}">{labels['history']}</a> · <a href="{REPOSITORY_URL}">GitHub</a></p>
      <p>Build: {commit_link} · <a href="https://kojikomatsuzaki.github.io/">{'Personal site' if english else '個人サイト'}</a></p>
    </footer>
  </div>
</body>
</html>
'''


def main():
    metadata = read_metadata()
    reference = os.environ.get("GITHUB_SHA", "main")
    if reference != "main" and not re.fullmatch(r"[0-9a-f]{40}", reference):
        raise ValueError("GITHUB_SHA must be a full commit SHA")
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    (OUTPUT / "en").mkdir(parents=True)
    (OUTPUT / "assets").mkdir()
    shutil.copy2(ROOT / "assets/style.css", OUTPUT / "assets/style.css")
    (OUTPUT / ".nojekyll").touch()
    for filename, (destination, _, _) in DOCUMENTS.items():
        for language in ("ja", "en"):
            directory = OUTPUT / "en" if language == "en" else OUTPUT
            (directory / destination).write_text(
                render_page(filename, language, metadata, reference), encoding="utf-8"
            )
    print(f"Built 8 pages: {metadata['version']} / {metadata['status']}")


if __name__ == "__main__":
    main()
