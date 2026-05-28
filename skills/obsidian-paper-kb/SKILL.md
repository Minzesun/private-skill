---
name: obsidian-paper-kb
description: Use when working with the user's Obsidian vault for academic paper reading, Zotero local API imports, Zotero citekeys, PDF literature notes, research concept cards, thesis knowledge summaries, topic maps, or Chinese/English scholarly note organization.
---

# Obsidian Paper KB

## Overview

Use the user's Obsidian vault as a research knowledge base for reading papers and distilling reusable knowledge. Default vault: `D:\Masterdegree_obsidian\Masterdegree`.

Preserve existing notes and folders. Add or update only the files needed for the requested paper, concept, topic, or output.

## Core Workflow

1. Confirm or infer the target vault. Prefer `D:\Masterdegree_obsidian\Masterdegree` unless the user provides another path.
2. Identify the source: Zotero item/citekey, local PDF, pasted abstract, paper title, DOI, or existing Obsidian note.
3. Create or update a literature note in `10-Papers/`.
4. Extract reusable ideas into concept cards in `20-Concepts/`.
5. Link papers and concepts to topic maps in `30-Topics/`.
6. Put review drafts, thesis paragraphs, presentation outlines, and summaries in `40-Outputs/`.
7. Leave unresolved material in `00-Inbox/` with clear next actions.

## Note Types

| Type | Folder | Purpose |
| --- | --- | --- |
| Literature note | `10-Papers/` | One note per paper, focused on claims, method, evidence, limits, and relevance. |
| Concept card | `20-Concepts/` | One reusable idea, equation, method, assumption, or distinction. |
| Topic map | `30-Topics/` | A research question or area that connects papers and concepts. |
| Output draft | `40-Outputs/` | Material meant to become a review, thesis section, report, or group meeting draft. |

## Hybrid Zotero Rules

- Let Zotero remain the source of truth for bibliographic metadata, PDFs, citation keys, and formal references.
- Let Obsidian hold understanding: summaries, comparisons, conceptual links, doubts, and writing-ready claims.
- Never invent missing bibliographic details. Use `unknown` or ask the user if a field matters.
- If Zotero metadata has no abstract, search reliable web metadata before writing a final literature note. Prefer DOI publisher pages, Crossref, OpenAlex, Semantic Scholar, PubMed/arXiv when applicable, and official repository pages. Record the abstract source URL in the note.
- Do not write fetched abstracts back to the Zotero database unless the user explicitly asks. Store enrichment status in Obsidian frontmatter/body instead.
- If no abstract is found after reasonable search, mark the note as `abstract_missing_after_search` and add a concrete follow-up task instead of inventing content.
- For highly relevant papers, especially FRIT/E-FRIT/ERIT/fictitious-reference papers, locate a PDF before producing a substantive reading note. First use Zotero attachments, then open-access DOI/Unpaywall/publisher/repository PDFs when available.
- Distinguish reading depth clearly: `metadata-noted`, `abstract-enriched`, `pdf-read`, or `needs-pdf`. Do not present a metadata-only note as a PDF-level reading note.
- When the user provides a Zotero citekey, include it in frontmatter and use it consistently.
- When the user provides only a PDF or title, create a useful note first and mark citation fields as incomplete.

## Direct Zotero Import

Use the local Zotero API before reading `zotero.sqlite` directly. Default Zotero URL: `http://127.0.0.1:23119`.

For a single paper, run the bundled helper:

```powershell
python -X utf8 "$env:USERPROFILE\.codex\skills\obsidian-paper-kb\scripts\zotero_to_obsidian.py" --query "citekey-or-title" --vault "D:\Masterdegree_obsidian\Masterdegree" --text-chars 12000 --json
```

The helper can search by Zotero item key, citation key, DOI, or title; resolve PDF attachment paths; optionally extract a PDF text excerpt with `pypdf`; and write a scaffold note in `10-Papers/`.

Use `--dry-run --json` first when matching may be ambiguous. Use `--overwrite` only when the user explicitly wants to replace an existing note.

After the helper creates or previews a scaffold, synthesize the actual reading note: fill the research problem, main idea, method, evidence, limitations, reusable concepts, and topic links. Do not leave the imported metadata scaffold as the final answer when the user asked for整理 or总结.

## Abstract And PDF Enrichment Workflow

Use this workflow when the user asks to整理 many Zotero papers or when a note lacks an abstract:

1. Inspect Zotero local API metadata and existing Obsidian note status.
2. If `abstractNote` is empty, search web metadata in this order:
   - DOI publisher page metadata and official landing page.
   - OpenAlex abstract inverted index.
   - Semantic Scholar abstract.
   - Crossref abstract when present.
   - arXiv/PubMed/other primary repositories when applicable.
3. Record `abstract_source` and `abstract_status` in the note. Preserve uncertainty when the abstract is unavailable.
4. For high-priority papers, search PDFs in this order:
   - Zotero PDF attachments.
   - Open-access DOI/Unpaywall links.
   - Publisher or official repository PDF links.
5. When a new local/open PDF is found, sync it back to Zotero:
   - Prefer attaching to the existing Zotero item only if a safe supported API/tool is available.
   - If direct attachment is unavailable, save the PDF as a standalone Zotero attachment/item through the Zotero Connector so Zotero can auto-recognize and merge it.
   - Keep a manifest keyed by Zotero item key and PDF hash to avoid duplicate standalone saves on reruns.
6. Record `zotero_pdf_status` in the note/audit, such as `existing`, `standalone-saved`, `standalone-save-failed`, or `not-found`.
7. Extract enough text from accessible PDFs to fill the literature note sections. Mark `reading_depth: pdf-read` only after PDF text has actually been read.
8. If PDF access or Zotero sync fails, keep the note at `abstract-enriched` or `needs-pdf` and add a task with the attempted sources.
9. Keep a batch audit note in `00-Inbox/` or `40-Outputs/` when processing many papers, listing found abstracts, missing abstracts, PDFs read, Zotero PDF sync status, and unresolved items.

## Literature Note Standard

Each paper note should answer:

- What problem does this paper solve?
- What is the main idea or mechanism?
- What assumptions does it rely on?
- What equations, algorithms, or experimental settings matter?
- What evidence supports the claim?
- What are the limitations?
- How does it connect to the user's research topics?
- Which concepts should become reusable cards?

Use `assets/paper-note-template.md` when creating a new paper note.

## Concept Card Standard

Concept cards must be atomic enough to reuse. Prefer one card for one idea, such as a method, formula, modeling assumption, control objective, reward design pattern, benchmark, or failure mode.

Use `assets/concept-card-template.md` when creating a concept card.

## Topic Map Standard

Topic maps are living indexes. They should collect key questions, linked concepts, important papers, open problems, and possible output sections.

Use `assets/topic-index-template.md` when creating a topic.

## Output Standard

When drafting an output, separate evidence from prose:

- Source claims: linked to paper notes.
- Reusable concepts: linked to concept cards.
- Draft prose: written in coherent academic Chinese unless the user asks otherwise.
- Gaps: marked as tasks, not silently hidden.

Use `assets/output-draft-template.md` when creating a draft.

## Invocation Examples

- `用 $obsidian-paper-kb 整理这篇论文`
- `用 $obsidian-paper-kb 从 Zotero 读取 citekey: condrachiAnaerobicDigestionProcesses2022 并整理到 Obsidian`
- `用 $obsidian-paper-kb 把这段摘要变成论文笔记和知识点卡片`
- `用 $obsidian-paper-kb 根据 10-Papers 里的笔记整理元强化学习主题索引`
- `用 $obsidian-paper-kb 帮我从这些论文里提炼毕业论文综述段落`

## Common Mistakes

- Do not make a generic summary without links to concepts and topics.
- Do not mix several unrelated concepts into one concept card.
- Do not bury uncertain citation data as if it were verified.
- Do not reorganize existing user folders unless the user explicitly asks.
- Do not treat Obsidian as Zotero; keep citation management in Zotero and knowledge synthesis in Obsidian.
- Do not write to the Zotero database; use Zotero's local API or a read-only backup for discovery.
