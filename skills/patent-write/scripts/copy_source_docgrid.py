#!/usr/bin/env python3
"""Copy section-level Word docGrid settings from a source DOCX to a target DOCX.

Usage:
    python copy_source_docgrid.py source.docx target.docx output.docx
    python copy_source_docgrid.py source.docx target.docx output.docx --skip-source-sections 1

The default skip value is 1 because the Central South University pre-review
template often stores an internal communication page in section 1, while the
formal patent body starts from section 2.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def copy_docgrid(source_path: Path, target_path: Path, output_path: Path, skip_source_sections: int) -> None:
    with ZipFile(source_path) as source_zip:
        source_doc = etree.fromstring(source_zip.read("word/document.xml"))

    with ZipFile(target_path) as target_zip:
        target_members = {name: target_zip.read(name) for name in target_zip.namelist()}
        target_doc = etree.fromstring(target_members["word/document.xml"])

    source_sections = source_doc.xpath(".//w:sectPr", namespaces=NS)
    target_sections = target_doc.xpath(".//w:sectPr", namespaces=NS)
    formal_source_sections = source_sections[skip_source_sections:]

    if len(formal_source_sections) < len(target_sections):
        raise SystemExit(
            f"source has {len(formal_source_sections)} usable sections after skipping "
            f"{skip_source_sections}, but target has {len(target_sections)} sections"
        )

    for idx, target_section in enumerate(target_sections):
        source_grid = formal_source_sections[idx].find("w:docGrid", namespaces=NS)
        target_grid = target_section.find("w:docGrid", namespaces=NS)
        if target_grid is not None:
            target_section.remove(target_grid)
        if source_grid is not None:
            target_section.append(deepcopy(source_grid))

    target_members["word/document.xml"] = etree.tostring(
        target_doc,
        xml_declaration=True,
        encoding="UTF-8",
        standalone="yes",
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output_path, "w", compression=ZIP_DEFLATED) as output_zip:
        for name, data in target_members.items():
            output_zip.writestr(name, data)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_docx", type=Path)
    parser.add_argument("target_docx", type=Path)
    parser.add_argument("output_docx", type=Path)
    parser.add_argument("--skip-source-sections", type=int, default=1)
    args = parser.parse_args()

    copy_docgrid(args.source_docx, args.target_docx, args.output_docx, args.skip_source_sections)
    print(args.output_docx)


if __name__ == "__main__":
    main()
