from pathlib import Path

import pandas as pd
from markupsafe import Markup


def define_env(env):
    """Register custom MkDocs macros."""

    @env.macro
    def excel_table(file_path: str, sheet_name: str):
        """Read an Excel sheet and return it as a scrollable HTML table."""

        docs_dir = Path(env.conf["docs_dir"])
        workbook_path = docs_dir / file_path

        if not workbook_path.exists():
            return Markup(
                f'<p><strong>Excel file not found:</strong> '
                f'{workbook_path}</p>'
            )

        try:
            dataframe = pd.read_excel(
                workbook_path,
                sheet_name=sheet_name,
                engine="openpyxl",
            ).fillna("")
        except Exception as error:
            return Markup(
                f'<p><strong>Could not read Excel sheet:</strong> '
                f'{error}</p>'
            )

        table = dataframe.to_html(
            index=False,
            classes="excel-table",
            border=0,
            escape=True,
        )

        return Markup(
            f'<div class="excel-table-wrapper">{table}</div>'
        )