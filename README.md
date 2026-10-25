<!-- language: ja -->

# この規約について

このサイトでは、私のプロジェクトに共通する開発の約束を公開しています。**人が読みやすく、長く使い続けられるコードとデータを作るための規約**です。

コードを書く人も、AIに開発を頼む人も、まず[開発規約](AGENTS.md)をご覧ください。

## 責任者とAIの役割

本GitHub RepositoryおよびPagesの開発・管理・運用責任者は、小松崎浩司です。規約の正式承認、ライセンスの決定、各プロジェクトへの規約の採用・更新は、小松崎浩司が判断します。AIは、そのための調査、比較、提案、実装を支援します。

## 何を大切にするか

- **人が読めること**：意味の分かる名前を付け、設計の理由を残します。
- **正本を一つにすること**：同じデータから、WebやCSVなどを作ります。
- **長く保守できること**：役割を分け、必要以上に複雑にしません。
- **判断と責任を明確にすること**：規約の変更と採用には、小松崎浩司の承認を残します。

## どの文書を読むか

| 知りたいこと | 文書 |
| --- | --- |
| 開発で守ること | [開発規約 / AGENTS.md](AGENTS.md) |
| このサイトの目的と使い方 | [概要 / README.md](README.md) |
| なぜこの設計にしたか | [設計判断 / DECISIONS.md](DECISIONS.md) |
| 何が変わったか | [変更履歴 / CHANGELOG.md](CHANGELOG.md) |

上部の文書メニューは、スクロールしても表示されます。狭い画面では左右にスクロールできます。右上の「☰ メニュー」からも同じ文書を選べます。日本語と英語は、右上の言語ボタンで切り替えます。

## プロジェクトで使うには

1. 承認済みの規約から、使う版を選びます。
2. プロジェクトのAGENTS.mdに、版、コミットSHA、承認記録URL、採用日を記録します。固有の追加・例外と理由も書きます。
3. 小松崎浩司が採用を承認します。

共通規約が更新されても、採用する版は自動で変わりません。更新する場合は、プロジェクトごとに影響を確認し、小松崎浩司が承認します。過去の作業へ遡って適用しません。

固定参照の形式は次のとおりです。`<承認対象SHA>` を、実際に承認したコミットに置き換えます。

```text
https://github.com/kojikomatsuzaki/development-standards/blob/<承認対象SHA>/AGENTS.md
```

規約をプロジェクト内へコピーする場合も、上流の版とSHAを併記します。コピーを別の正本にはしません。`main` や `latest` だけを指定する運用は避けてください。

## 現在の公開状態

**Version 1.0.0は承認済み（Approved）です。** 小松崎浩司が会話で明示的に承認し、2026-10-26に状態へ反映しました。[承認記録](https://github.com/kojikomatsuzaki/development-standards/pull/4)には、承認対象のコミットと会話からの転記であることを記録しています。本人によるGitHubレビューとは区別します。

規約本文の承認対象はコミット `fef2d0598f1f828cf18265894d06b2b0de019486` です。正式な状態と承認情報はAGENTS.md冒頭のYAMLで確認できます。ライセンスの決定や、他プロジェクトでの採用は別の判断です。

- 版、状態、制定日、改訂日、著者は、AGENTS.md冒頭のYAMLで管理しています。各ページの規約情報も、ここから表示します。
- 日本語が正本で、英語は対訳です。
- このリポジトリのライセンスは未決定です。MITやCC BY-SA 4.0などの採用は、まだ承認していません。
- レビューを強制するブランチ保護は未設定です。CODEOWNERSは担当者を示すファイルで、保護設定そのものではありません。

公開サイト：<https://kojikomatsuzaki.github.io/development-standards/>

正本リポジトリ：<https://github.com/kojikomatsuzaki/development-standards>

## 修正を提案するには

PRに、変更理由、影響、対象版、検証結果を書いてください。規範の変更は、小松崎浩司の承認を得て確定します。詳しい手順は[開発規約の第10節](AGENTS.md)にあります。PRのひな型は `.github/pull_request_template.md` です。

公開やマージだけで、規約を正式承認したとは扱いません。DraftからApprovedへの変更、ライセンス確定、正式タグ発行は、それぞれ小松崎浩司の承認を経て行います。

## サイトを保守するには

4つのMarkdownが本文の正本です。`scripts/build_site.py` が日英のHTMLを生成し、GitHub ActionsがPagesへ公開します。本文をHTMLに転記して管理する必要はありません。

各Markdownでは、行頭の `<!-- language: ja -->` と `<!-- language: en -->` で言語を分けます。CSSは `assets/style.css` の1ファイルです。文書メニューはHTMLとCSSで動き、閲覧時のJavaScript、外部CDN、GitHub APIは使いません。

Python 3.12を基準に、次のコマンドで構築・検証できます。

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/build_site.py
.venv/bin/python scripts/check_site.py
.venv/bin/python -m http.server 8000 --directory _site
```

`http://localhost:8000/` を開き、文書間の移動、日英切替、狭い画面での操作を確認します。生成先の `_site/` はコミットしません。依存パッケージの版は `requirements.txt` に固定し、更新時に再検証します。依存パッケージには、それぞれのライセンスが適用されます。そのコードは、このリポジトリに同梱していません。

Pagesの公開元は **GitHub Actions** です。mainへのpushで検証・公開し、PRでは検証だけを行います。公開後はActionsの成功とリンクを確認してください。公開サイトは現在のmainを表示し、ビルド対象コミットにもリンクします。規約を特定版で採用する際は、公開トップではなく固定参照を使います。

<!-- language: en -->

# About these standards

This site publishes the development rules shared by my projects. **They help us create code and data that people can understand and maintain for years.**

Whether you write code or ask AI to develop it, start with the [development standards](AGENTS.md).

## Responsibility and the role of AI

Hiroshi (Kōji) Komatsuzaki is responsible for the development, management, and operation of this GitHub repository and its Pages site. He decides formal approval, license selection, and adoption or updates of these standards in each project. AI supports the research, comparison, proposals, and implementation needed for those decisions.

## What matters

- **Readability**: choose meaningful names and retain design reasons.
- **One authoritative source**: generate Web, CSV, and other outputs from the same data.
- **Long-term maintenance**: separate responsibilities and avoid unnecessary complexity.
- **Clear decisions and responsibility**: retain approval from Hiroshi (Kōji) Komatsuzaki for changes and adoption.

## Which document to read

| What you want to know | Document |
| --- | --- |
| Rules to follow during development | [Standards / AGENTS.md](AGENTS.md) |
| Purpose and use of this site | [Overview / README.md](README.md) |
| Reasons behind the design | [Decisions / DECISIONS.md](DECISIONS.md) |
| What changed | [Changelog / CHANGELOG.md](CHANGELOG.md) |

The document navigation stays visible as you scroll. On narrow screens, scroll it horizontally. The “☰ Menu” at the top right opens the same document choices. The language button switches between Japanese and English.

## How to adopt the standards

1. Choose a formally approved version.
2. Record its version, commit SHA, approval URL, and adoption date in the project's AGENTS.md. Include project additions or exceptions and reasons.
3. Obtain approval from Hiroshi (Kōji) Komatsuzaki for adoption.

Shared standards updates do not automatically change a project's adopted version. Assess each project's update separately and obtain approval from Hiroshi (Kōji) Komatsuzaki. Do not apply changes retroactively.

Use this fixed-reference format, replacing `<approved-SHA>` with an actual approved commit:

```text
https://github.com/kojikomatsuzaki/development-standards/blob/<approved-SHA>/AGENTS.md
```

If a project needs a local copy, retain the upstream version and SHA. It is not a separate authoritative source. Do not adopt only `main` or `latest`.

## Current publication status

**Version 1.0.0 is Approved.** Hiroshi (Kōji) Komatsuzaki explicitly approved it in this conversation; the status was updated on 2026-10-26. The [approval record](https://github.com/kojikomatsuzaki/development-standards/pull/4) identifies the reviewed commit and states that AI transcribed the conversation. It is distinct from a GitHub review posted personally by the owner.

The approved standards body is at commit `fef2d0598f1f828cf18265894d06b2b0de019486`. Check the opening YAML in AGENTS.md for status and approval metadata. License selection and adoption in another project remain separate decisions.

- Version, status, dates, and author are managed in the opening YAML of AGENTS.md. Site metadata is generated from it.
- Japanese is authoritative; English is a translation.
- This repository's license remains undecided. Neither MIT nor CC BY-SA 4.0 has been approved.
- Mandatory review enforcement is not configured. CODEOWNERS identifies ownership; it does not configure branch protection.

Published site: <https://kojikomatsuzaki.github.io/development-standards/>

Authoritative repository: <https://github.com/kojikomatsuzaki/development-standards>

## How to propose a correction

Explain the rationale, impact, target version, and verification in a PR. Obtain approval from Hiroshi (Kōji) Komatsuzaki before finalizing normative changes. See [section 10 of the standards](AGENTS.md). The PR template is `.github/pull_request_template.md`.

Publication or merging alone is not formal approval. Approved status, license selection, and formal tags each require approval from Hiroshi (Kōji) Komatsuzaki.

## How to maintain the site

The four Markdown documents are authoritative. `scripts/build_site.py` generates Japanese and English HTML, and GitHub Actions publishes it to Pages. No manually maintained HTML copy of the body is needed.

Separate languages with standalone lines `<!-- language: ja -->` and `<!-- language: en -->`. CSS lives in `assets/style.css`. Navigation uses HTML and CSS; reading requires no JavaScript, external CDN, or GitHub API.

Python 3.12 is the baseline. Build and check with:

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/build_site.py
.venv/bin/python scripts/check_site.py
.venv/bin/python -m http.server 8000 --directory _site
```

Open `http://localhost:8000/` and check document navigation, language switching, and narrow-screen controls. Do not commit `_site/`. Dependencies are pinned in `requirements.txt`; recheck when updating them. Dependencies retain their own licenses; their code is not bundled here.

The Pages source is **GitHub Actions**. Pushes to main verify and publish; PRs only verify. Check Actions and links after publication. The site displays current main and links to its build commit. Use a fixed reference rather than the public homepage when adopting a standards version.
