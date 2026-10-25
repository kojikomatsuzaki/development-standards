<!-- language: ja -->

# 設計判断

記録開始日：2026-10-25。D001〜D008は草案段階の設計記録です。2026-10-26のVersion 1.0.0承認はD009に記録します。共通方針として依頼で指定された内容と、実装上選んだ方法を区別して記録します。

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

- 判断：小松崎浩司本人の明示的なGitHub記録を承認の根拠にし、SSH署名は任意とする。承認済み版・SHAをプロジェクトごとに採用する。
- 理由：判断した人と対象差分を追跡し、予期しない遡及適用を防ぐ。単独管理者でも明示コメントと本人のマージ記録を使う。
- 代替案：署名付きタグの必須化、mainへの追従、AI判断のみの確定。
- 再検討：共同管理、監査要件、GitHubの権限・プランや保護機能が変わる場合。レビュー強制設定はまだ未設定。

## D005：ライセンスは保留

- 判断：リポジトリのライセンスを今回確定しない。プロジェクトごとに権利対象と用途を確認し、小松崎浩司が選ぶ。
- 理由：ソフトウェア、規約文章、データでは目的と条件が異なる。
- 代替案：MITへの統一、コンテンツを含めCC BY-SA 4.0で一括指定。
- 再検討：対象、権利者、候補、互換性を整理したPRを小松崎浩司が承認したとき。

## D006：責務分離と必要十分な構成

- 判断：業務ロジックをPort / Adapter経由で外部から分離する。小規模な処理の形式的な多層化は避ける。CSSは1ファイルを章立てする。
- 理由：プロトコルや依存先の変更範囲を狭め、読みやすさと長期保守を両立させる。
- 代替案：外部APIとロジックの一体化、初めから多数の抽象化層を導入。
- 再検討：責務、規模、変更頻度が増え、分割による効果が明確になった場合。

## D007：二つの入口と読みやすい文章

- 判断：言語ボタンの隣に「☰ メニュー」を置き、その下に文書メニューを常時表示する。上部全体をスクロール中も残し、狭い画面では文書メニューだけを横スクロールできるようにする。
- 理由：既存の新荘音頭サイトと操作位置をそろえつつ、文書一覧が隠れる問題を補う。二つのメニューは同じ一覧から生成し、現在のページを両方で示す。
- 代替案：ハンバーガーのみ、横並びメニューのみ。
- 再検討：文書が増えた場合や、固定部分が閲覧を妨げる場合。今回はHTMLのdetailsを使い、閲覧時のJavaScriptを増やさない。
- 文章方針：概要は目的と使い方、規約は守る行動を先に書く。理由と詳細を後に続け、現在の公開状態は概要にまとめる。承認・例外・データの保持に関する条件は削らない。
- 依頼者の指示：2026-10-25の会話で、メニュー併用案と文章の書き直しを指示。規約全体の正式承認は引き続き未実施。

## D008：開発・管理・運用責任者を明記する

- 判断：本GitHub RepositoryおよびPagesの開発・管理・運用責任者を、小松崎浩司と明記する。規約の正式承認、ライセンスの決定、各プロジェクトへの規約の採用・更新も、小松崎浩司が判断する。
- 理由：「人間の承認」だけでは判断する人が特定できないため。責任の範囲を、規約の管理からリポジトリと公開サイトの開発・管理・運用全体へ明示する。
- AIの役割：調査、比較、提案、実装を支援し、判断に必要な根拠、不確実な点、未確認事項を示す。
- 代替案：「人間」「管理者」などの一般的な役割名だけを記載する。
- 再検討：責任者の変更や共同運営への移行が決まった場合。変更内容と権限の範囲を記録し、明示的な承認を得て更新する。
- 依頼者の指示：2026-10-25の会話で上記の責任者表記を確定し、反映を指示。規約全体の正式承認やライセンスの選択は引き続き未実施。

## D009：会話での明示的な承認を記録してApprovedへ移行

- 判断：小松崎浩司の「approvedに上げてよいよ」と、その後の「続きよろしく」という明示指示に基づき、Version 1.0.0をApprovedへ変更する。記録・状態反映日：2026-10-26。
- 承認対象：コミット `fef2d0598f1f828cf18265894d06b2b0de019486` の規約本文（日英）。本文の意味や手順は変更しない。
- 記録：[PR #4](https://github.com/kojikomatsuzaki/development-standards/pull/4)に、承認者、対象コミット、発言、会話からのAI転記であることを明記する。本人によるGitHubコメント・レビュー・手動マージとして扱わない。
- 理由：今回は会話での明示指示を根拠として反映し、通常の本人によるGitHub承認手順との差を公開記録に残す。AIが独自に承認を決めたものではない。
- 代替案：Draftの維持、本人によるGitHubレビューを待つ方法。
- 範囲：状態・承認メタデータと、それに伴う概要・設計判断・変更履歴の更新。第10節の一般的な承認手順は変更しない。ライセンスは未決定のまま、他プロジェクトへの採用も行わない。
- 再検討：承認対象本文の変更、承認内容の訂正・撤回、責任者変更が生じた場合。対象と影響を示し、小松崎浩司の判断を得る。

<!-- language: en -->

# Design decisions

Records started: 2026-10-25. D001–D008 describe draft-stage decisions. D009 records approval of Version 1.0.0 on 2026-10-26. Requested shared policies are distinguished from implementation choices.

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

- Decision: Use explicit GitHub approval records from Hiroshi (Kōji) Komatsuzaki; SSH signing is optional. Each project adopts an approved version and SHA.
- Reason: Trace the decision maker and reviewed diff, preventing unexpected retroactive changes. A sole maintainer can use an explicit comment and their own merge record.
- Alternatives: Mandatory signed tags, following main, or AI-only approval.
- Reconsider when: Collaboration, audit requirements, permissions, plans, or protection features change. Mandatory review enforcement is not configured yet.

## D005: License deferred

- Decision: Do not select this repository's license now. Hiroshi (Kōji) Komatsuzaki selects project licenses after examining scope and intended use.
- Reason: Software, standards text, and data may require different terms.
- Alternatives: MIT for everything; CC BY-SA 4.0 for all content.
- Reconsider when: Hiroshi (Kōji) Komatsuzaki approves a PR identifying scope, rights holders, candidates, and compatibility.

## D006: Responsibilities and sufficient simplicity

- Decision: Separate business logic from external systems through Ports / Adapters; avoid formal layering of small tasks. Keep CSS in one file with sections.
- Reason: Limit protocol and dependency change impact while preserving readability and long-term maintenance.
- Alternatives: Mix APIs with logic; introduce many abstraction layers immediately.
- Reconsider when: Responsibilities, size, or change frequency make the benefit of separation clear.

## D007: Two navigation paths and readable instructions

- Decision: Place “☰ Menu” beside the language button and keep a document navigation row below it. Keep the header visible while scrolling; allow the document row to scroll horizontally on narrow screens.
- Reason: Match the control position on the existing Shinsō Ondo site while keeping document choices discoverable. Generate both menus from the same list and mark the current page in each.
- Alternatives: A hamburger menu alone; a document row alone.
- Reconsider when: More documents are added or the fixed area obstructs reading. Use native HTML details without adding runtime JavaScript.
- Writing approach: Start the overview with purpose and usage, and standards with required actions. Follow with reasons and details. Collect current publication status in the overview. Retain approval, exception, and data-preservation conditions.
- Requester instruction: The requester authorized the combined navigation and rewriting in the 2026-10-25 conversation. Formal approval of the standards remains pending.

## D008: Name the person responsible for development, management, and operation

- Decision: Identify Hiroshi (Kōji) Komatsuzaki as responsible for the development, management, and operation of this GitHub repository and its Pages site. He also decides formal approval, license selection, and adoption or updates of these standards in each project.
- Reason: “Human approval” does not identify who decides. State responsibility for the development, management, and operation of the repository and public site, beyond standards administration alone.
- AI's role: Support research, comparison, proposals, and implementation; present evidence, uncertainty, and unverified items needed for decisions.
- Alternative: Identify only a generic role such as “human” or “administrator.”
- Reconsider when: A change of responsible person or joint operation is agreed. Record the change and scope of authority and obtain explicit approval before updating.
- Requester instruction: The requester confirmed this wording and instructed implementation in the 2026-10-25 conversation. Formal approval of the standards as a whole and license selection remain pending.

## D009: Record explicit conversational approval and promote to Approved

- Decision: Promote Version 1.0.0 following Hiroshi (Kōji) Komatsuzaki's explicit instruction “approvedに上げてよいよ” and subsequent instruction “続きよろしく”. Recorded and applied on 2026-10-26.
- Scope approved: The Japanese and English standards body at commit `fef2d0598f1f828cf18265894d06b2b0de019486`. Its meaning and procedures are unchanged.
- Record: [PR #4](https://github.com/kojikomatsuzaki/development-standards/pull/4) identifies the approver, target commit, wording, and AI transcription from the conversation. It is not represented as a GitHub comment, review, or manual merge personally performed by the owner.
- Reason: Apply this specific explicit instruction while recording the difference from the usual owner-originated GitHub approval procedure. AI did not independently decide approval.
- Alternatives: Retain Draft; wait for a personally posted GitHub review.
- Implementation scope: Status and approval metadata and corresponding overview, decision, and changelog updates. Section 10's general approval procedure is unchanged. License remains undecided; no other project adopts the standards.
- Reconsider when: The approved body changes, approval is corrected or withdrawn, or responsibility changes. Identify the target and impact and obtain the owner's decision.
