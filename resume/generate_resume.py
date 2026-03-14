import json
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parent
PROFILE_PATH = ROOT.parents[1] / "one-percent-better-os" / "public_profile.json"
AVENIR_NEXT = "/System/Library/Fonts/Avenir Next.ttc"
CONTACT_LINE_1 = "North York, ON | chris.yoon@outlook.com"


def load_profile() -> dict:
    with PROFILE_PATH.open("r", encoding="utf-8") as fh:
        return json.load(fh)


PROFILE = load_profile()
LINKS = PROFILE["links"]
CONTACT_LINE_2 = (
    f'<link href="{LINKS["linkedin"]}" color="#4E4A44">linkedin.com/in/sukminyoon</link>'
    f' | <link href="{LINKS["github"]}" color="#4E4A44">github.com/sukminc</link>'
    f' | <link href="{LINKS["brand"]}" color="#4E4A44">onepercentbetter.dev</link>'
)
OPB_ABOUT_URL = LINKS["about"]
VARIANTS = PROFILE["resume_variants"]


def register_fonts():
    pdfmetrics.registerFont(TTFont("AvenirNext-Regular", AVENIR_NEXT, subfontIndex=7))
    pdfmetrics.registerFont(TTFont("AvenirNext-Medium", AVENIR_NEXT, subfontIndex=5))
    pdfmetrics.registerFont(TTFont("AvenirNext-Demi", AVENIR_NEXT, subfontIndex=2))
    pdfmetrics.registerFont(TTFont("AvenirNext-Bold", AVENIR_NEXT, subfontIndex=0))


def build_styles():
    styles = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name",
            parent=styles["Heading1"],
            fontName="AvenirNext-Demi",
            fontSize=21,
            leading=24,
            alignment=TA_CENTER,
            spaceAfter=4,
            textColor=colors.HexColor("#111111"),
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=styles["Normal"],
            fontName="AvenirNext-Regular",
            fontSize=10,
            leading=13.1,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#4E4A44"),
        ),
        "section": ParagraphStyle(
            "Section",
            parent=styles["Heading2"],
            fontName="AvenirNext-Demi",
            fontSize=11.1,
            leading=13.8,
            spaceBefore=8,
            spaceAfter=4,
            textColor=colors.HexColor("#111111"),
        ),
        "body": ParagraphStyle(
            "Body",
            parent=styles["Normal"],
            fontName="AvenirNext-Regular",
            fontSize=9.85,
            leading=13.2,
            spaceAfter=4,
            textColor=colors.HexColor("#171717"),
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=styles["Normal"],
            fontName="AvenirNext-Regular",
            fontSize=9.7,
            leading=12.6,
            leftIndent=17,
            firstLineIndent=-11,
            spaceAfter=2,
            textColor=colors.HexColor("#171717"),
        ),
        "role": ParagraphStyle(
            "Role",
            parent=styles["Normal"],
            fontName="AvenirNext-Demi",
            fontSize=10.35,
            leading=12.9,
            spaceBefore=5,
            spaceAfter=1,
            textColor=colors.HexColor("#111111"),
        ),
        "meta": ParagraphStyle(
            "Meta",
            parent=styles["Normal"],
            fontName="AvenirNext-Medium",
            fontSize=9.25,
            leading=11.7,
            spaceAfter=2,
            textColor=colors.HexColor("#6A645C"),
        ),
        "eyebrow": ParagraphStyle(
            "Eyebrow",
            parent=styles["Normal"],
            fontName="AvenirNext-Medium",
            fontSize=9.1,
            leading=11.8,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#6A645C"),
        ),
    }


def divider():
    return HRFlowable(
        width="100%",
        thickness=0.5,
        color=colors.HexColor("#D9D3C8"),
        spaceBefore=3,
        spaceAfter=6,
    )


def section(title, styles):
    return [Paragraph(title, styles["section"]), divider()]


def role(title, company, meta, styles):
    return [
        Paragraph(f"{title} | {company}", styles["role"]),
        Paragraph(meta, styles["meta"]),
    ]


def linked_role(title, company, meta, url, styles):
    linked_title = f'<link href="{url}" color="#111111">{title}</link>'
    linked_company = f'<link href="{url}" color="#111111">{company}</link>'
    linked_meta = f'<link href="{url}" color="#6A645C">{meta}</link>'
    return [
        Paragraph(f"{linked_title} | {linked_company}", styles["role"]),
        Paragraph(linked_meta, styles["meta"]),
    ]


def bullets(items, styles, url=None):
    bullet_lines = []
    for item in items:
        content = item
        if url:
            content = f'<link href="{url}" color="#171717">{item}</link>'
        bullet_lines.append(Paragraph(f"•&nbsp;{content}", styles["bullet"]))
    bullet_lines.append(Spacer(1, 0.03 * inch))
    return bullet_lines


def build_common_experience(styles):
    items = []
    items.extend(role("Senior Data Engineer", "theScore / ESPN Bet", "Toronto, ON | Jul 2023 - Jul 2025", styles))
    items.extend(
        bullets(
            [
                "Built and maintained Apache Airflow DAGs orchestrating ingestion and transformation across BigQuery and AWS Redshift for millions of daily betting transactions.",
                "Designed a Python-based observability framework for 15+ ETL pipelines that detected schema drift and volume anomalies, reducing manual debugging effort by 60 percent.",
                "Developed SQL and Python reconciliation workflows for SOX-compliant financial and regulatory reporting, maintaining complete audit visibility.",
                "Supported legacy-to-cloud workflow validation across GCP and AWS while improving query performance and preventing data loss during migration.",
            ],
            styles,
        )
    )

    items.extend(role("Tech Lead", "QA Consultants", "Client: Avesis | Remote | Mar 2021 - Mar 2023", styles))
    items.extend(
        bullets(
            [
                "Led technical design for insurance ETL pipelines, defining data mapping specs and transformation logic for large-scale claims workflows.",
                "Engineered automated Python profiling routines that surfaced data corruption earlier in the development cycle and reduced downstream incident risk.",
            ],
            styles,
        )
    )

    items.extend(role("Data Engineer", "QA Consultants", "Client: Jewelers Mutual | Remote | Feb 2020 - Mar 2021", styles))
    items.extend(
        bullets(
            [
                "Authored and optimized SQL and Python ETL scripts for warehouse loading and introduced automated profiling to surface quality issues at ingestion.",
            ],
            styles,
        )
    )

    items.extend(section("EARLIER ENGINEERING BACKGROUND", styles))
    items.append(
        Paragraph(
            "Additional experience across Wisetail, Secret Location, and VRBO focused on automation, migration validation, release confidence, and backend data integrity. Those roles shaped the quality-first mindset I now bring to data and product engineering work.",
            styles["body"],
        )
    )
    return items


def build_projects(projects, styles):
    items = []
    for project in projects:
        linked_name = f'<link href="{project["url"]}" color="#111111">{project["name"]}</link>'
        items.extend(role(linked_name, project["meta"].split(" | ")[0], f"GitHub | {project['meta'].split(' | ')[1]}", styles))
        items.extend(bullets(project["bullets"], styles))
    return items


def build_story(variant_name):
    config = VARIANTS[variant_name]
    styles = build_styles()
    items = [
        Paragraph("Chris S. Yoon", styles["name"]),
        Paragraph(config["eyebrow"], styles["eyebrow"]),
        Spacer(1, 0.03 * inch),
        Paragraph(
            'North York, ON | <link href="mailto:chris.yoon@outlook.com" color="#4E4A44">chris.yoon@outlook.com</link>',
            styles["contact"],
        ),
        Paragraph(CONTACT_LINE_2, styles["contact"]),
        Spacer(1, 0.05 * inch),
    ]

    items.extend(section("PROFESSIONAL SUMMARY", styles))
    items.append(Paragraph(config["summary"], styles["body"]))

    items.extend(section("CORE STRENGTHS", styles))
    for line in config["strengths"]:
        items.append(Paragraph(line, styles["body"]))

    items.extend(section("EXPERIENCE", styles))
    if variant_name == "data_engineer":
        items.extend(build_common_experience(styles))
        items.extend(linked_role(config["opb_title"], "1% Better.dev", "Toronto, ON | Jul 2025 - Present", OPB_ABOUT_URL, styles))
        items.extend(bullets(config["opb_bullets"], styles, url=OPB_ABOUT_URL))
    else:
        items.extend(linked_role(config["opb_title"], "1% Better.dev", "Toronto, ON | Jul 2025 - Present", OPB_ABOUT_URL, styles))
        items.extend(bullets(config["opb_bullets"], styles, url=OPB_ABOUT_URL))
        items.extend(build_common_experience(styles))

    items.extend(section(config["project_section_title"], styles))
    items.extend(build_projects(config["projects"], styles))

    items.extend(section(config["signal_title"], styles))
    for paragraph in config["signal_body"]:
        items.append(Paragraph(paragraph, styles["body"]))

    items.extend(section("EDUCATION AND CERTIFICATIONS", styles))
    items.append(
        Paragraph(
            "University of Waterloo - Studies in Chemical Engineering | ISTQB Certified Tester, Foundation Level | Continuing development in LLM workflows, modern data tooling, and AI-assisted delivery.",
            styles["body"],
        )
    )
    return items


def add_page_number(canvas, doc):
    canvas.setFont("AvenirNext-Regular", 8.2)
    canvas.setFillColor(colors.HexColor("#7A746B"))
    canvas.drawRightString(7.75 * inch, 0.42 * inch, f"Page {doc.page}")


def build_pdf(filename, story):
    doc = SimpleDocTemplate(
        str(ROOT / filename),
        pagesize=LETTER,
        leftMargin=0.72 * inch,
        rightMargin=0.72 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.58 * inch,
        # Keep PDFs byte-stable across rebuilds when the content has not changed.
        invariant=1,
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


def main():
    register_fonts()
    ROOT.mkdir(parents=True, exist_ok=True)
    for variant_name, config in VARIANTS.items():
        build_pdf(config["filename"], build_story(variant_name))
        print(f"Wrote {ROOT / config['filename']}")


if __name__ == "__main__":
    main()
