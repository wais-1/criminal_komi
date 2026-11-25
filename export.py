import csv
import json

from openpyxl import Workbook

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph
)

pdfmetrics.registerFont(
    TTFont(
        "CyrillicFont",
        "/Library/Fonts/Arial Unicode.ttf"
    )
)


def export_csv(filename, headers, data):

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(headers)
        writer.writerows(data)


def export_excel(filename, headers, data):

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Пользователи"

    sheet.append(headers)

    for row in data:
        sheet.append(row)

    # Автоматическая ширина колонок
    for column in sheet.columns:

        max_length = 0
        column_letter = column[0].column_letter

        for cell in column:

            if cell.value:
                max_length = max(
                    max_length,
                    len(str(cell.value))
                )

        sheet.column_dimensions[
            column_letter
        ].width = min(max_length + 2, 40)

    workbook.save(filename)


def export_json(filename, headers, data):

    result = []

    for row in data:

        item = dict(
            zip(headers, row)
        )

        result.append(item)

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            result,
            file,
            ensure_ascii=False,
            indent=4
        )


def export_pdf(filename, headers, data):

    document = SimpleDocTemplate(
        filename,
        pagesize=landscape(A4)
    )

    styles = getSampleStyleSheet()

    title = Paragraph(
        "Отчёт о пользователях",
        ParagraphStyle(
            "CyrillicTitle",
            parent=styles["Title"],
            fontName="CyrillicFont"
        )
    )

    table_data = [headers] + data

    table = Table(
        table_data,
        repeatRows=1
    )

    table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "CyrillicFont"
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            )
        ])
    )

    document.build([
        title,
        table
    ])