<!-- language: ja -->

# 共通開発規約 / Development Standards

可読性、保守性、長期的な再利用を重視する開発規約の正本リポジトリです。日本語を正本、英語を対訳とします。初版はDraftであり、承認済みの規約はまだありません。現在の版・状態・制定日・改訂日・著者は [AGENTS.md](AGENTS.md) 冒頭のYAMLを参照してください。

## 文書

| 文書 | 役割 |
| --- | --- |
| [AGENTS.md](AGENTS.md) | AIエージェント向け共通開発規約と版のメタデータ |
| [README.md](README.md) | 目的、使い方、構築・公開方法 |
| [DECISIONS.md](DECISIONS.md) | 設計判断、理由、代替案、再検討条件 |
| [CHANGELOG.md](CHANGELOG.md) | 版ごとの変更履歴 |

公開サイト：<https://kojikomatsuzaki.github.io/development-standards/>。
GitHub：<https://github.com/kojikomatsuzaki/development-standards>。

## プロジェクトでの利用

1. 正式承認後の規約を読み、採用する特定版を選びます。現在のDraftを承認済みとして採用しません。
2. プロジェクト固有のAGENTS.mdに、採用版、コミットSHA、承認記録URL、採用日、追加・例外を記録します。
3. 採用を人間が承認します。mainの最新版を継続的に読み込むだけの運用はしません。
4. 更新は各プロジェクトで影響を確認して承認します。既存プロジェクトへ自動・遡及適用しません。

固定参照は `https://github.com/kojikomatsuzaki/development-standards/blob/<承認対象SHA>/AGENTS.md` の形式です。実在する承認対象SHAで置換し、仮の値を承認記録として扱いません。規約本文をプロジェクト内へ配置する場合は、上流版とSHAを併記し、複製を独立した正本にしません。

## 変更と承認

規範変更はPRで提案し、人間の承認を得ます。PRには対象コミット、理由、影響、版、検証結果を記載します。単独管理者の場合は本人による明示コメントとマージ記録を使えます。詳細は [AGENTS.md](AGENTS.md) 第10節を参照してください。Approvedへの変更、ライセンス確定、正式タグ発行は初期構築に含めません。

`.github/pull_request_template.md` は確認事項のひな型です。`.github/CODEOWNERS` はレビュー担当の意思表示であり、ブランチ保護の設定ではありません。現時点で強制レビューを設定済みとは主張しません。GitHubの権限・プランによる設定可否を確認したうえで導入を検討します。

## 構成とOne Source, Multi Use

4つのMarkdownを `scripts/build_site.py` が読み込み、日英別のHTMLを `_site/` に生成します。各文書の `<!-- language: ja -->` と `<!-- language: en -->` が言語境界です。両言語を同じMarkdownで対訳管理し、表示用の規約本文は別管理しません。版の表示はAGENTS.md冒頭のYAMLから生成します。`assets/style.css` は1ファイル、生成時にコピーされます。閲覧時の外部CDNやGitHub API、JavaScriptは不要です。

## ローカル構築

Python 3.12を基準にします。作業ディレクトリで以下を実行してください。

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/build_site.py
.venv/bin/python scripts/check_site.py
.venv/bin/python -m http.server 8000 --directory _site
```

`http://localhost:8000/` を開き、各文書・日英切替・スマートフォン幅を確認します。生成物 `_site/` はコミットしません。依存パッケージの版はrequirements.txtに固定し、更新時に再検証します。

## GitHub Pagesの公開

1. publicリポジトリ `kojikomatsuzaki/development-standards` に本ファイル群を配置します。ライセンスは選択しません。
2. Settings → Pages → Build and deployment → Source を **GitHub Actions** にします。
3. mainへのpushで `.github/workflows/pages.yml` が検証・生成・公開します。PRでは検証のみ実行します。
4. Actionsの成功、公開ページ、4文書の日英切替、原文と履歴へのリンクを確認します。

公開はDraftの閲覧用です。Pagesのトップは常にmainの現在の文書を示すため、プロジェクトの固定採用には使用しません。公開サイトにはビルド対象コミットへのリンクを表示します。

## ライセンス

**未決定・承認待ち**です。今回、LICENSEを追加せず、MITやCC BY-SA 4.0等を確定しません。第三者の依存パッケージはそれぞれのライセンスに従います。このリポジトリにそれらのコードは同梱しません。

<!-- language: en -->

# Development Standards

This is the authoritative repository for shared development standards emphasizing readability, maintainability, and long-term reuse. Japanese is authoritative; English is a parallel translation. The initial version is a draft; no approved standards version exists yet. See the opening YAML in [AGENTS.md](AGENTS.md) for current version, status, establishment date, revision date, and author.

## Documents

| Document | Purpose |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Shared standards for AI agents and version metadata |
| [README.md](README.md) | Purpose, usage, build, and publication |
| [DECISIONS.md](DECISIONS.md) | Decisions, reasons, alternatives, and reconsideration |
| [CHANGELOG.md](CHANGELOG.md) | Changes by version |

Published site: <https://kojikomatsuzaki.github.io/development-standards/>.
GitHub: <https://github.com/kojikomatsuzaki/development-standards>.

## Adoption in a project

1. Read and select a particular formally approved version. Do not adopt this draft as approved.
2. Record the version, commit SHA, approval URL, adoption date, and additions or exceptions in the project's AGENTS.md.
3. Obtain human approval for adoption. Do not continuously adopt whatever main currently contains.
4. Assess and approve updates for each project. Never apply them automatically or retroactively.

Use a fixed reference of the form `https://github.com/kojikomatsuzaki/development-standards/blob/<approved-SHA>/AGENTS.md`, replacing the placeholder with an actual approved commit. Placeholders are not approval records. If a project needs a local copy, retain upstream version and SHA; it is not an independent authoritative source.

## Changes and approval

Propose normative changes through a PR and obtain human approval. State the target commit, rationale, impact, version, and verification. A sole maintainer may use their explicit comment and merge record. See section 10 of [AGENTS.md](AGENTS.md). Approved status, license selection, and formal release tags are outside initial construction.

The PR template supports review. CODEOWNERS expresses review ownership but does not configure branch protection. Mandatory reviews are not claimed to be enforced. Consider enforcement after checking GitHub permissions and plan support.

## Structure and One Source, Multi Use

`scripts/build_site.py` reads the four Markdown documents and generates Japanese and English HTML in `_site/`. Markers `<!-- language: ja -->` and `<!-- language: en -->` separate the parallel translations in each source. No separately maintained display copy of the standards exists. Version metadata comes from the YAML in AGENTS.md. A single `assets/style.css` is copied during generation. Reading requires no external CDN, GitHub API, or JavaScript.

## Local build

Python 3.12 is the baseline. Run in this directory:

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/build_site.py
.venv/bin/python scripts/check_site.py
.venv/bin/python -m http.server 8000 --directory _site
```

Open `http://localhost:8000/` and inspect all documents, language switching, and mobile widths. Do not commit `_site/`. Dependency versions are pinned in requirements.txt and must be rechecked when updated.

## GitHub Pages publication

1. Put these files in the public repository `kojikomatsuzaki/development-standards` without choosing a license.
2. Set Settings → Pages → Build and deployment → Source to **GitHub Actions**.
3. On a push to main, `.github/workflows/pages.yml` verifies, builds, and deploys. Pull requests run verification only.
4. Check Actions, the public page, all four documents in both languages, and source/history links.

Publication makes the draft readable. The site tracks current main and is not the fixed reference used for adoption. The site links to its exact build commit.

## License

**Undecided; awaiting approval.** No LICENSE is added and neither MIT nor CC BY-SA 4.0 is selected. Third-party build dependencies retain their own licenses; their code is not bundled here.
