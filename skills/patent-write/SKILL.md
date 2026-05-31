---
name: patent-write
description: Use this skill when creating, auditing, or revising Chinese patent DOCX drafts to match a formal pre-review patent template, especially Word docGrid, page setup, fonts, paragraph settings, claims, abstracts, figures, and structured patent-language style.
---

# Patent Write

## Overview

Use this skill for Chinese patent writing tasks where the output must be a formal `.docx` patent draft rather than a paper-like technical report. It preserves the source template's Word grid, fonts, margins, paragraph settings, and patent section structure while revising the text into structured patent language.

When a source pre-review document is available, treat it as the formatting authority. For the Central South University pre-review template used in this workspace, load `references/zhongnan-precheck-format.md` before editing and use `scripts/copy_source_docgrid.py` when strict Word `docGrid` matching is required.

## Workflow

1. Identify the source template and target draft.
   - Prefer an existing pre-review `.doc` or `.docx` supplied by the user as the source of truth.
   - Convert `.doc` to `.docx` before structural or XML-level inspection.
   - If the source contains an internal agency/applicant communication page, exclude it from the formal patent body.

2. Audit structure before rewriting.
   - Confirm the formal sections: `说   明   书`, `权   利   要   求   书`, `说   明   书   摘   要`, `说   明   书   附   图`, `摘   要   附   图`.
   - In `说   明   书`, use the patent sequence `技术领域`, `背景技术`, `发明内容`, `附图说明`, `具体实施方式`.
   - Remove paper/report-style headings such as `一、总体`, `研究路线`, `本发明要解决的技术问题` as an independent section, and other non-patent framing unless the user or agency explicitly requires them.

3. Apply formatting from the template.
   - Match page size, margins, header/footer distances, page numbers, fonts, paragraph spacing, indentation, and line spacing.
   - For strict grid matching, copy each formal section's `w:docGrid` from the source template to the target using the bundled script.
   - Keep style changes scoped. Prefer direct formatting if the source template uses Normal/`正文` with direct role-specific formatting.

4. Rewrite into structured patent language.
   - Use `本发明的目的之一在于提供...`, `本发明的目的之二在于提供...`, and optional `本发明的目的之三...` paragraphs in `发明内容`.
   - Present the method as `本发明提供的这种...方法，包括如下步骤：`, followed by `S1` to `Sn` summary paragraphs.
   - Expand each step with `所述的步骤Sx，具体包括如下步骤：`.
   - In `具体实施方式`, repeat the step logic with implementation detail, examples, tables, figures, and system modules.
   - Use patent-friendly Chinese terms, for example `中心代表点` instead of `medoid`, `回退PID` instead of `fallback`, and `不安全标志` instead of `unsafe`.

5. Build claims, abstract, and figures.
   - Claim 1 should be a complete method claim with separate `S1` to `Sn` paragraphs.
   - Dependent claims should reference claim 1 and expand one step at a time using `其特征在于所述的步骤Sx，具体包括如下步骤：`.
   - Add a system claim when the invention includes implementable modules.
   - Write the abstract in the pattern `本发明公开了/提供了一种...。该方法...；...。本发明不仅...，而且...。`.
   - Use figure descriptions such as `图1为本发明方法的总体流程示意图。`.

6. Verify before delivery.
   - Render the final DOCX to PDF or page PNGs and inspect title pages, table pages, the claims start page, abstract pages, and figure pages.
   - Audit that required sections are present and forbidden paper-like headings/terms are absent.
   - If strict grid alignment was requested, inspect `word/document.xml` and confirm each formal section contains the expected `w:docGrid`.

## Formatting Reference

For the Central South University pre-review template, use `references/zhongnan-precheck-format.md` as the detailed formatting checklist. Important defaults:

- A4 portrait, top margin 2.50 cm, bottom 1.50 cm, left 2.50 cm, right 1.50 cm.
- Blank header and centered footer page number.
- Major patent section title: `楷体_GB2312`, 18 pt, centered, exact 25 pt line spacing.
- Patent name title: `宋体`, 22 pt, bold, centered.
- Level-1 patent headings: `宋体`, 14 pt, bold, justified.
- Body paragraphs: `宋体`, 14 pt, justified, first-line indent 28 pt, no before/after spacing, approximately 1.33 line spacing.
- English or Latin text: `Times New Roman`.
- Tables should match the source template. Use full grid borders when strict source replication is required.

## Tools And Scripts

- Use the Documents skill for `.docx` creation, revision, rendering, and visual QA.
- Use `scripts/copy_source_docgrid.py <source.docx> <target.docx> <output.docx>` to migrate section-level Word grid settings.
- On Windows, if LibreOffice is unavailable, Word COM export plus PyMuPDF rendering is an acceptable verification route.

## Review Checklist

- The formal draft does not include internal communication or agency instruction pages.
- Formal section titles and patent name title use the source template's fonts and spacing.
- The specification uses patent structure, not thesis/paper/report structure.
- Claims are numbered, stepwise, and dependency references are coherent.
- Abstract and figure descriptions are concise and patent-style.
- Tables, formulas, figures, and page breaks do not collide or overflow after rendering.
- `docGrid`, margins, footer page numbers, body indentation, and line spacing match the source template.
