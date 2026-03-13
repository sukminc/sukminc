from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import HRFlowable, ListFlowable, ListItem, Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "Chris_Yoon_Resume_2026.pdf"
AVENIR_NEXT = "/System/Library/Fonts/Avenir Next.ttc"


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
            leading=13.2,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#4E4A44"),
        ),
        "section": ParagraphStyle(
            "Section",
            parent=styles["Heading2"],
            fontName="AvenirNext-Demi",
            fontSize=11.2,
            leading=14,
            spaceBefore=8,
            spaceAfter=5,
            textColor=colors.HexColor("#111111"),
        ),
        "body": ParagraphStyle(
            "Body",
            parent=styles["Normal"],
            fontName="AvenirNext-Regular",
            fontSize=9.95,
            leading=13.6,
            spaceAfter=4,
            textColor=colors.HexColor("#171717"),
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=styles["Normal"],
            fontName="AvenirNext-Regular",
            fontSize=9.7,
            leading=12.9,
            leftIndent=8,
            textColor=colors.HexColor("#171717"),
        ),
        "role": ParagraphStyle(
            "Role",
            parent=styles["Normal"],
            fontName="AvenirNext-Demi",
            fontSize=10.45,
            leading=13,
            spaceBefore=6,
            spaceAfter=1,
            textColor=colors.HexColor("#111111"),
        ),
        "meta": ParagraphStyle(
            "Meta",
            parent=styles["Normal"],
            fontName="AvenirNext-Medium",
            fontSize=9.35,
            leading=12.2,
            spaceAfter=2,
            textColor=colors.HexColor("#6A645C"),
        ),
        "eyebrow": ParagraphStyle(
            "Eyebrow",
            parent=styles["Normal"],
            fontName="AvenirNext-Medium",
            fontSize=9.2,
            leading=12,
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


def bullets(items, styles):
    return ListFlowable(
        [ListItem(Paragraph(item, styles["bullet"]), leftIndent=0) for item in items],
        bulletType="bullet",
        bulletFontName="AvenirNext-Regular",
        bulletFontSize=7.5,
        leftIndent=16,
        spaceBefore=1,
        spaceAfter=5,
    )


def section(title, styles):
    return [Paragraph(title, styles["section"]), divider()]


def role(title, company, location, dates, styles):
    return [
        Paragraph(f"{title} | {company}", styles["role"]),
        Paragraph(f"{location} | {dates}", styles["meta"]),
    ]


def story():
    styles = build_styles()
    items = [
        Paragraph("Chris S. Yoon", styles["name"]),
        Paragraph("Senior Data Engineer | Product Builder | Public Build Discipline", styles["eyebrow"]),
        Spacer(1, 0.03 * inch),
        Paragraph(
            "North York, ON | 416-300-7316 | chris.yoon@outlook.com",
            styles["contact"],
        ),
        Paragraph(
            "linkedin.com/in/sukminyoon | github.com/sukminc | onepercentbetter.dev",
            styles["contact"],
        ),
        Spacer(1, 0.05 * inch),
    ]

    items.extend(section("PROFESSIONAL SUMMARY", styles))
    items.append(
        Paragraph(
            "Senior Data Engineer with 10+ years building data systems that stay reliable under real production pressure. At theScore / ESPN Bet, I built and maintained Airflow-orchestrated pipelines across BigQuery and Redshift for millions of daily transactions, created a Python observability framework that cut debugging overhead by 60 percent, and delivered SOX-facing reconciliation workflows with full audit visibility. I now pair that production discipline with hands-on product work through 1% Better.dev, where I ship small applications, learn AI-assisted workflows in public, and keep a visible build loop active while pursuing my next role.",
            styles["body"],
        )
    )

    items.extend(section("CORE STRENGTHS", styles))
    items.append(
        Paragraph(
            "<b>Data Engineering</b>  ETL and ELT design, Apache Airflow, data quality gates, schema drift handling, reconciliation pipelines, warehouse modeling",
            styles["body"],
        )
    )
    items.append(
        Paragraph(
            "<b>Languages and Frameworks</b>  Python, SQL, FastAPI, Pandas, NumPy, SQLAlchemy, TypeScript, Next.js",
            styles["body"],
        )
    )
    items.append(
        Paragraph(
            "<b>Platforms and Tools</b>  BigQuery, Redshift, PostgreSQL, Docker, GitHub Actions, Jenkins, Pytest, Playwright, Stripe API",
            styles["body"],
        )
    )
    items.append(
        Paragraph(
            "<b>Current Focus</b>  AI-assisted product development, LLM workflow integration, public build discipline, and fast release loops",
            styles["body"],
        )
    )

    items.extend(section("EXPERIENCE", styles))

    items.extend(role("Founder and Product Engineer", "1% Better.dev", "Toronto, ON", "Jul 2025 - Present", styles))
    items.append(
        bullets(
            [
                "Built a public product studio to keep shipping while learning modern AI-assisted development workflows, with work visible across a live site, linked repositories, and ongoing commit history.",
                "Shaped and shipped small-scope products such as 1% Better Today and 1% Better Focus to prove a repeatable loop: pick a narrow problem, release quickly, learn, and improve.",
                "Turned the platform into both a funding surface and a credibility layer by connecting resume claims to live products, recent activity, and product thinking.",
            ],
            styles,
        )
    )

    items.extend(role("Senior Data Engineer", "theScore / ESPN Bet", "Toronto, ON", "Jul 2023 - Jul 2025", styles))
    items.append(
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

    items.extend(role("Tech Lead, Contract", "Avesis via QA Consultants", "Remote", "Mar 2021 - Mar 2023", styles))
    items.append(
        bullets(
            [
                "Led technical design for insurance ETL pipelines, defining data mapping specs and transformation logic for large-scale claims workflows.",
                "Engineered automated Python profiling routines that surfaced data corruption earlier in the development cycle and reduced downstream incident risk.",
            ],
            styles,
        )
    )

    items.extend(role("Data Engineer, Contract", "Jewelers Mutual via QA Consultants", "Remote", "Feb 2020 - Mar 2021", styles))
    items.append(
        bullets(
            [
                "Authored and optimized SQL and Python ETL scripts for warehouse loading and introduced automated profiling to surface quality issues at ingestion.",
            ],
            styles,
        )
    )

    items.extend(section("ADDITIONAL EXPERIENCE", styles))
    items.append(
        Paragraph(
            "Wisetail, an Intertek company - Data / QA Automation Engineer | Toronto, ON | Aug 2019 - Feb 2020",
            styles["body"],
        )
    )
    items.append(
        Paragraph(
            "Secret Location - SDET / QA Engineer | Toronto, ON | Jul 2018 - Jul 2019",
            styles["body"],
        )
    )
    items.append(
        Paragraph(
            "VRBO / Expedia Group - QA Engineer / Data Migration Analyst | Toronto, ON | Jul 2016 - Mar 2018",
            styles["body"],
        )
    )
    items.append(
        Paragraph(
            "Across these roles, I built SQL-backed validation, migration reconciliation, and automated release checks across policy systems, VR and mobile products, and large platform transitions.",
            styles["body"],
        )
    )

    items.extend(section("SELECTED PROJECTS", styles))

    items.extend(role("1% Better Today", "Public repo", "GitHub", "Current", styles))
    items.append(
        bullets(
            [
                "Small daily reset product designed to be easy to release, easy to use, and easy to improve.",
                "Demonstrates low-friction product thinking and the kind of tight shipping loop I am intentionally practicing in public.",
            ],
            styles,
        )
    )

    items.extend(role("1% Better Focus", "Public repo", "GitHub", "Current", styles))
    items.append(
        bullets(
            [
                "Lightweight focus timer built around the same studio thesis: useful scope, fast shipping, and visible progress instead of overbuilt complexity.",
            ],
            styles,
        )
    )

    items.extend(role("Blue Jays Moneyball ETL", "Public repo", "GitHub", "Live", styles))
    items.append(
        bullets(
            [
                "Production-style Airflow and PostgreSQL pipeline with fail-fast data quality gates.",
                "Includes regression coverage that asserts the guardrails still fail when they should, treating data safety as part of CI rather than documentation.",
            ],
            styles,
        )
    )

    items.extend(role("ActionKeeper", "Public repo", "GitHub", "Building", styles))
    items.append(
        bullets(
            [
                "Full-stack workflow product for structured offers, counters, and agreement tracking with persistent audit history.",
                "Shows product thinking around trust, negotiation state, and clear user flows in multi-step decision workflows.",
            ],
            styles,
        )
    )

    items.extend(role("TwelveLabs API Validator", "Public repo", "GitHub", "Live", styles))
    items.append(
        bullets(
            [
                "Python validation framework for multimodal search covering fuzzy matching, multilingual queries, and injection-style edge cases.",
            ],
            styles,
        )
    )

    items.extend(section("PUBLIC BUILD SIGNAL", styles))
    items.append(
        Paragraph(
            "1% Better.dev gives recruiters a fast way to verify how I work now, not just what I did before: live product framing, linked repositories, recent commit activity, and a clear through-line from resume to portfolio.",
            styles["body"],
        )
    )
    items.append(
        Paragraph(
            "1% Better.poker is the longer-term specialist track. Right now the focus is shipping smaller applications quickly, learning LLM-assisted workflows deeply, and using public work as proof of execution.",
            styles["body"],
        )
    )

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


def main():
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=LETTER,
        leftMargin=0.72 * inch,
        rightMargin=0.72 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.58 * inch,
    )
    doc.build(story(), onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
