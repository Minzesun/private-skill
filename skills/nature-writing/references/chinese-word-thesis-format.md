# Chinese Word Thesis Format Preset

Use this reference when the user asks for a Chinese Word document, Chinese
doctoral thesis style, Chinese dissertation formatting, or a local DOCX report
that should resemble a 985-university PhD thesis rather than a journal article.

## Preset name

`chinese_phd_thesis_985`

## Evidence basis

This preset is based on the user's approved synthesis of official Chinese
graduate-thesis formatting materials from Tsinghua University, Peking
University, and Shanghai Jiao Tong University. Treat it as a practical
cross-school default, not as a substitute for a target university's current
official template.

If the user names a specific university, prefer that university's official
current template over this preset.

## Page setup

- Paper: A4.
- Margins: top 3.0 cm, bottom 3.0 cm, left 3.0 cm, right 3.0 cm.
- Gutter: 0 cm unless the user requests printed binding.
- Header distance: 2.2 cm from edge.
- Footer distance: 2.2 cm from edge.

## Fonts

- Chinese body text: SimSun, 12 pt.
- Latin letters and numbers in body text: Times New Roman, 12 pt.
- Chinese headings: SimHei.
- Latin letters and numbers in headings: Times New Roman or Arial, matching the
  document builder's available fonts.
- Equations: Cambria Math where available; otherwise Times New Roman-compatible
  math rendering.

## Paragraph defaults

- Body paragraph alignment: justified.
- First-line indent: 2 Chinese characters.
- Line spacing: exactly 20 pt.
- Space before: 0 pt.
- Space after: 0 pt.

## Heading ladder

Use real Word styles, not direct formatting.

| Role | Style | Format |
|---|---|---|
| Chapter title | Heading 1 | SimHei 16 pt, centered, single spacing, 24 pt before, 18 pt after |
| First-level section | Heading 2 | SimHei 14 pt, left aligned, exactly 20 pt line spacing, 24 pt before, 6 pt after |
| Second-level section | Heading 3 | SimHei 13 pt, left aligned, exactly 20 pt line spacing, 12 pt before, 6 pt after |
| Third-level section | Heading 4 | SimHei 12 pt, left aligned, exactly 20 pt line spacing, 12 pt before, 6 pt after |

Use Heading 4 sparingly. If the outline needs deeper nesting, ask whether the
user wants a dissertation-style hierarchy or a shorter report-style hierarchy.

## Abstract

- Abstract heading: SimHei 16 pt, centered, 24 pt before, 18 pt after.
- Abstract body: SimSun 12 pt, justified, first-line indent 2 Chinese
  characters, exactly 20 pt line spacing.
- Keywords: SimSun 12 pt. Use a visible label such as `关键词：`.

## Figures, tables, and equations

- Figure captions: below figures, SimSun 11 pt, Latin/numbers in Times New
  Roman, centered, 6 pt before, 12 pt after.
- Table captions: above tables, SimSun 11 pt, Latin/numbers in Times New Roman,
  centered, 12 pt before, 6 pt after.
- Table body: SimSun 11 pt, Latin/numbers in Times New Roman, single spacing,
  3 pt before, 3 pt after.
- Equations: centered, 12 pt, 6 pt before, 6 pt after. Put equation numbers at
  the right margin only if the document already uses numbered equations or the
  user requests them.

## Header, footer, and page numbers

- Header: SimSun 10.5 pt, centered.
- Page number: Times New Roman 10.5 pt, centered in footer.
- Use simple headers for draft reports. Do not add decorative rules unless the
  target university template requires them.

## References

- Reference list text: SimSun 10.5 pt.
- Latin/numbers: Times New Roman 10.5 pt.
- Line spacing: exactly 16 pt.
- Space before: 3 pt.
- Space after: 0 pt.
- Hanging indent: 2 Chinese characters.

## Implementation notes for DOCX builders

- Implement the preset through Word styles before adding content.
- Avoid fake headings, fake numbered lists, and manual caption styling.
- Keep tables within page margins and use explicit column widths.
- Render the final DOCX to page images and inspect visual layout when the
  document toolchain allows it.
- If LibreOffice is unavailable or broken, use an alternate renderer such as
  Microsoft Word export plus PDF rasterization, then disclose the renderer used.

## Output behavior

When applying this preset, state briefly that the document uses the
`chinese_phd_thesis_985` format unless the user has supplied a more specific
school template.
