"""Read one workbook's N/P monthly title cohort without mixing in A-L data."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from openpyxl import load_workbook


def collect_monthly_titles(path: Path, sheet_name: str = "卡片数据") -> dict[str, Any]:
    workbook = load_workbook(path, read_only=True, data_only=True)
    try:
        sheet = workbook[sheet_name]
        titles: dict[str, float] = {}
        title_rows = 0
        for title, _other, exposure in sheet.iter_rows(
            min_row=2, min_col=14, max_col=16, values_only=True
        ):
            if title is None or not str(title).strip():
                continue
            title_rows += 1
            name = str(title).strip()
            if exposure is None:
                value = 0.0
            elif isinstance(exposure, (int, float)) and not isinstance(exposure, bool):
                value = float(exposure)
            else:
                raise ValueError(f"P 列不是数值：第 {title_rows + 1} 行，标题 {name!r}")
            if value < 0:
                raise ValueError(f"P 列为负：标题 {name!r}")
            titles[name] = max(value, titles.get(name, 0.0))
        if not titles:
            raise ValueError("N 列没有非空标题；请核对工作簿和工作表")
        ranked = sorted(titles.items(), key=lambda item: (-item[1], item[0]))
        return {
            "file": path.name,
            "title_rows": title_rows,
            "unique_titles": len(ranked),
            "duplicate_rows": title_rows - len(ranked),
            "positive_p_titles": sum(value > 0 for _, value in ranked),
            "zero_p_titles": sum(value == 0 for _, value in ranked),
            "titles": [{"title": name, "detail_exposure_p": value} for name, value in ranked],
        }
    finally:
        workbook.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="只读取月度工作簿 N 列标题与 P 列详情页曝光")
    parser.add_argument("workbook", type=Path)
    parser.add_argument("--sheet", default="卡片数据")
    parser.add_argument("--top", type=int, default=20, help="展示前 N 条；0 表示全部")
    args = parser.parse_args()
    if args.top < 0:
        parser.error("--top 不能为负数")
    result = collect_monthly_titles(args.workbook, args.sheet)
    if args.top:
        result["titles"] = result["titles"][: args.top]
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
