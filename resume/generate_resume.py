from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import ListFlowable, ListItem, Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "Chris_Yoon_Resume_2026.pdf"


def build_styles():
    styles = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=20,
            leading=24,
            alignment=TA_CENTER,
            spaceAfter=4,
            textColor=colors.HexColor("#111111"),
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=12,
            alignment=TA_CENTER,
            spaceAfter=12,
            textColor=colors.HexColor("#333333"),
        ),
        "section": ParagraphStyle(
            "Section",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=12,
            spaceBefore=6,
            spaceAfter=6,
            textColor=colors.HexColor("#111111"),
        ),
        "body": ParagraphStyle(
            "Body",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=12,
            spaceAfter=4,
            textColor=colors.HexColor("#111111"),
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=9.1,
            leading=11.5,
            leftIndent=10,
            firstLineIndent=0,
            textColor=colors.HexColor("#111111"),
        ),
        "role": ParagraphStyle(
            "Role",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.4,
            leading=12,
            spaceBefore=3,
            textColor=colors.HexColor("#111111"),
        ),
        "meta": ParagraphStyle(
            "Meta",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=8.8,
            leading=11,
            textColor=colors.HexColor("#444444"),
        ),
    }


def bullets(items, styles):
    return ListFlowable(
        [
            ListItem(Paragraph(item, styles["bullet"]), leftIndent=0)
            for item in items
        ],
        bulletType="bullet",
        bulletFontName="Helvetica",
        bulletFontSize=7,
        leftIndent=14,
        spaceBefore=0,
        spaceAfter=4,
    )


def section(title, styles):
    return Paragraph(title, styles["section"])


def role(title, company, location, dates, styles):
    return [
        Paragraph(f"{title} | {company}", styles["role"]),
        Paragraph(f"{location} | {dates}", styles["meta"]),
    ]


def story():
    styles = build_styles()
    items = [
        Paragraph("Chris S. Yoon", styles["name"]),
        Paragraph(
            "North York, ON | 416-300-7316 | chris.yoon@outlook.com | linkedin.com/in/sukminyoon | github.com/sukminc | onepercentbetter.dev",
            styles["contact"],
        ),
        section("PROFESSIONAL SUMMARY", styles),
        Paragraph(
            "Senior Data Engineer with 10+ years building data systems that are reliable under real production pressure. At theScore / ESPN Bet, built and maintained Airflow-orchestrated pipelines across BigQuery and Redshift for millions of daily transactions, created a Python observability framework that cut debugging overhead by 60 percent, and delivered SOX-facing reconciliation workflows with full audit visibility. I pair that production discipline with hands-on product work through 1% Better.dev, where I ship small applications, learn AI-assisted workflows in public, and keep a visible build loop active while pursuing my next role.",
            styles["body"],
        ),
        section("CORE STRENGTHS", styles),
        Paragraph(
            "<b>Data Engineering:</b> ETL and ELT design, Apache Airflow, data quality gates, schema drift handling, reconciliation pipelines, warehouse modeling",
            styles["body"],
        ),
        Paragraph(
            "<b>Languages and Frameworks:</b> Python, SQL, FastAPI, Pandas, NumPy, SQLAlchemy, TypeScript, Next.js",
            styles["body"],
        ),
        Paragraph(
            "<b>Platforms and Tools:</b> BigQuery, Redshift, PostgreSQL, Docker, GitHub Actions, Jenkins, Pytest, Playwright, Stripe API",
            styles["body"],
        ),
        Paragraph(
            "<b>Current Focus:</b> AI-assisted product development, LLM workflow integration, public build discipline, fast release loops",
            styles["body"],
        ),
        section("EXPERIENCE", styles),
    ]

    items.extend(role("Founder and Product Engineer", "1% Better.dev", "Toronto, ON", "Jul 2025 - Present", styles))
    items.append(
        bullets(
            [
                "Built a public product studio to keep shipping while learning modern AI-assisted development workflows, with work visible across a live site, linked repositories, and ongoing commit history.",
                "Shaped and shipped small-scope products such as 1% Better Today and 1% Better Focus to prove a repeatable loop: pick a narrow problem, release quickly, learn, and improve.",
                "Using the platform as both a funding surface and a credibility layer for recruiters by connecting resume claims to live projects, recent activity, and product thinking.",
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

    items.extend(role("Data / QA Automation Engineer", "Wisetail, an Intertek company", "Toronto, ON", "Aug 2019 - Feb 2020", styles))
    items.append(
        bullets(
            [
                "Integrated backend data validation workflows into Jenkins and GitHub Actions pipelines to improve release confidence across policy systems.",
            ],
            styles,
        )
    )

    items.extend(role("SDET / QA Engineer", "Secret Location", "Toronto, ON", "Jul 2018 - Jul 2019", styles))
    items.append(
        bullets(
            [
                "Built end-to-end and SQL-backed validation suites across VR and mobile products, catching backend consistency issues before production release.",
            ],
            styles,
        )
    )

    items.extend(role("QA Engineer / Data Migration Analyst", "VRBO / Expedia Group", "Toronto, ON", "Jul 2016 - Mar 2018", styles))
    items.append(
        bullets(
            [
                "Validated large-scale platform migration with SQL reconciliation checks across source and target systems, preserving data integrity across millions of records.",
            ],
            styles,
        )
    )

    items.append(section("SELECTED PROJECTS", styles))
    items.extend(role("1% Better Today", "GitHub project", "Public repo", "Current", styles))
    items.append(
        bullets(
            [
                "Small daily reset product designed to be easy to release, easy to use, and easy to improve. Demonstrates low-friction product thinking and fast iteration.",
            ],
            styles,
        )
    )

    items.extend(role("1% Better Focus", "GitHub project", "Public repo", "Current", styles))
    items.append(
        bullets(
            [
                "Lightweight focus timer built around the same thesis as the studio: useful scope, fast shipping, and visible progress instead of overbuilt complexity.",
            ],
            styles,
        )
    )

    items.extend(role("Blue Jays Moneyball ETL", "GitHub project", "Public repo", "Live", styles))
    items.append(
        bullets(
            [
                "Production-style Airflow and PostgreSQL pipeline with fail-fast data quality gates and regression coverage that asserts the guardrails still fail when they should.",
            ],
            styles,
        )
    )

    items.extend(role("ActionKeeper", "GitHub project", "Public repo", "Building", styles))
    items.append(
        bullets(
            [
                "Full-stack workflow product for structured offers, counters, and agreement tracking with persistent audit history and trust-first interaction design.",
            ],
            styles,
        )
    )

    items.extend(role("TwelveLabs API Validator", "GitHub project", "Public repo", "Live", styles))
    items.append(
        bullets(
            [
                "Python validation framework for multimodal search covering fuzzy matching, multilingual queries, and injection-style edge cases.",
            ],
            styles,
        )
    )

    items.append(section("EDUCATION AND CERTIFICATIONS", styles))
    items.append(
        Paragraph(
            "University of Waterloo - Studies in Chemical Engineering | ISTQB Certified Tester, Foundation Level | Continuing development in LLM workflows, modern data tooling, and AI-assisted software delivery",
            styles["body"],
        )
    )
    return items


def add_page_number(canvas, doc):
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#666666"))
    canvas.drawRightString(7.75 * inch, 0.45 * inch, f"Page {doc.page}")


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=LETTER,
        leftMargin=0.68 * inch,
        rightMargin=0.68 * inch,
        topMargin=0.62 * inch,
        bottomMargin=0.6 * inch,
    )
    doc.build(story(), onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
