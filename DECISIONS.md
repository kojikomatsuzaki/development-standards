<!-- language: ja -->

# 設計判断

記録日：2026-10-25。以下は初版構築時のDraft設計記録です。正式承認は未実施です。共通方針として依頼で指定された内容と、実装上選んだ方法を区別して記録します。

## D001：正本と日英対訳

- 判断：日本語を正本とし、各Markdown内に英語の対訳を保持する。Pagesは生成物とする。
- 理由：One Source, Multi Useを守り、本文の二重管理を避ける。
- 代替案：言語ごとの独立ファイル、HTMLへの手動転記。
- 再検討：翻訳規模が増えた場合、同じ正本からの翻訳管理を維持できる方式を評価する。

## D002：静的生成と公開

- 判断：Python、Python-Markdown、PyYAMLとGitHub ActionsでHTMLを生成し、Pagesへ公開する。閲覧時JavaScriptは使わず、日英は通常のリンクで切り替える。
- 理由：小規模な4文書に必要な表・見出し・コード表示を備え、依存を限定し、ビルド時に正本とリンクを検証できる。
- 代替案：Jekyll、MkDocs等、ブラウザー上でMarkdownを変換する方式。
- 再検討：全文検索、多数の版の同時公開、多人数翻訳が必要になった場合。生成物の手修正は採用しない。

## D003：メタデータの所在

- 判断：AGENTS.md冒頭のYAMLに版・状態・日付・著者・正本言語・承認記録を置く。Pagesの各画面はこれを参照する。
- 理由：版表示の不一致を防ぎ、AIも人間も同じ資料を確認できる。
- 代替案：独立した設定ファイルへの転記、各ページへの重複記載。
- 再検討：複数の独立した規約を管理するようになった場合。

## D004：承認とバージョン固定

- 判断：人間の明示的なGitHub記録を承認の根拠にし、SSH署名は任意とする。承認済み版・SHAをプロジェクトごとに採用する。
- 理由：判断した人と対象差分を追跡し、予期しない遡及適用を防ぐ。単独管理者でも明示コメントと本人のマージ記録を使う。
- 代替案：署名付きタグの必須化、mainへの追従、AI判断のみの確定。
- 再検討：共同管理、監査要件、GitHubの権限・プランや保護機能が変わる場合。レビュー強制設定はまだ未設定。

## D005：ライセンスは保留

- 判断：リポジトリのライセンスを今回確定しない。プロジェクトごとに権利対象と用途を確認し、人間が選ぶ。
- 理由：ソフトウェア、規約文章、データでは目的と条件が異なる。
- 代替案：MITへの統一、コンテンツを含めCC BY-SA 4.0で一括指定。
- 再検討：対象、権利者、候補、互換性を整理したPRを人間が承認したとき。

## D006：責務分離と必要十分な構成

- 判断：業務ロジックをPort / Adapter経由で外部から分離する。小規模な処理の形式的な多層化は避ける。CSSは1ファイルを章立てする。
- 理由：プロトコルや依存先の変更範囲を狭め、読みやすさと長期保守を両立させる。
- 代替案：外部APIとロジックの一体化、初めから多数の抽象化層を導入。
- 再検討：責務、規模、変更頻度が増え、分割による効果が明確になった場合。

<!-- language: en -->

# Design decisions

Recorded: 2026-10-25. These are draft design records for initial construction, not formal approval. They distinguish requested shared policies from implementation choices.

## D001: Authoritative source and translations

- Decision: Japanese is authoritative, with English in each Markdown document; Pages is generated.
- Reason: Preserve One Source, Multi Use and avoid separately maintained display copies.
- Alternatives: Independent language files; manual transcription into HTML.
- Reconsider when: Translation scale increases, while preserving a single authoritative source.

## D002: Static generation and publication

- Decision: Generate HTML with Python, Python-Markdown, PyYAML, and GitHub Actions; publish to Pages. Use ordinary links for language switching, without runtime JavaScript.
- Reason: Support tables, headings, and code for four small documents, limit dependencies, and validate source correspondence and links during builds.
- Alternatives: Jekyll, MkDocs, or browser-side Markdown conversion.
- Reconsider when: Full-text search, concurrent version hosting, or multiple translators become necessary. Hand-editing generated output remains excluded.

## D003: Metadata location

- Decision: Keep version, status, dates, author, authoritative language, and approval record in the YAML header of AGENTS.md; all site pages read it.
- Reason: Avoid inconsistent version displays and provide the same evidence to people and AI.
- Alternatives: Separate duplicated configuration; metadata repeated on every page.
- Reconsider when: Managing several independent standards.

## D004: Approval and fixed adoption

- Decision: Use explicit human GitHub records; SSH signing is optional. Each project adopts an approved version and SHA.
- Reason: Trace the decision maker and reviewed diff, preventing unexpected retroactive changes. A sole maintainer can use an explicit comment and their own merge record.
- Alternatives: Mandatory signed tags, following main, or AI-only approval.
- Reconsider when: Collaboration, audit requirements, permissions, plans, or protection features change. Mandatory review enforcement is not configured yet.

## D005: License deferred

- Decision: Do not select this repository's license now. Humans select project licenses after examining scope and intended use.
- Reason: Software, standards text, and data may require different terms.
- Alternatives: MIT for everything; CC BY-SA 4.0 for all content.
- Reconsider when: A human approves a PR identifying scope, rights holders, candidates, and compatibility.

## D006: Responsibilities and sufficient simplicity

- Decision: Separate business logic from external systems through Ports / Adapters; avoid formal layering of small tasks. Keep CSS in one file with sections.
- Reason: Limit protocol and dependency change impact while preserving readability and long-term maintenance.
- Alternatives: Mix APIs with logic; introduce many abstraction layers immediately.
- Reconsider when: Responsibilities, size, or change frequency make the benefit of separation clear.
