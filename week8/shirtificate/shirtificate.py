from fpdf import FPDF
from fpdf.enums import Align


def main() -> None:
    shirtificate(input("Name: "))


def shirtificate(name: str) -> None:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 48)
    pdf.set_auto_page_break(False)
    pdf.set_margin(0)
    pdf.cell(pdf.epw, pdf.eph / 4, "CS50 Shirtificate", align=Align.C)
    pdf.ln()
    pdf.image("shirtificate.png", 0, pdf.eph / 4)
    pdf.set_font_size(32)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(pdf.epw, pdf.eph / 2, f"{name} took CS50", align=Align.C)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()

