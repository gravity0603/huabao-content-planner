"""Regression for the N/P cohort boundary and duplicate-title handling."""

from pathlib import Path
import unittest
from uuid import uuid4

from openpyxl import Workbook

from monthly_n_titles import collect_monthly_titles


class MonthlyTitlesTest(unittest.TestCase):
    def test_uses_only_n_and_max_p(self) -> None:
        path = Path.cwd() / f"monthly_n_titles_fixture_{uuid4().hex}.xlsx"
        try:
            workbook = Workbook()
            sheet = workbook.active
            sheet.title = "卡片数据"
            sheet["B2"] = "旧图组高曝光"
            sheet["H2"] = 9_999_999
            sheet["N2"] = "本月新题"
            sheet["P2"] = 120
            sheet["N3"] = "本月新题"
            sheet["P3"] = 95
            sheet["N4"] = "另一个新题"
            sheet["P4"] = 0
            sheet["N5"] = "本月新题"
            sheet["P5"] = 180
            workbook.save(path)
            result = collect_monthly_titles(path)
            self.assertEqual(result["title_rows"], 4)
            self.assertEqual(result["unique_titles"], 2)
            self.assertEqual(result["duplicate_rows"], 2)
            self.assertEqual(result["positive_p_titles"], 1)
            self.assertEqual(result["zero_p_titles"], 1)
            self.assertEqual(result["titles"][0], {"title": "本月新题", "detail_exposure_p": 180.0})
            self.assertNotIn("旧图组高曝光", [item["title"] for item in result["titles"]])
        finally:
            path.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
