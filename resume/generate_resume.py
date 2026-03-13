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
AVENIR_NEXT = "/System/Library/Fonts/Avenir Next.ttc"
CONTACT_LINE_1 = "North York, ON | 416-300-7316 | chris.yoon@outlook.com"
CONTACT_LINE_2 = (
    '<link href="https://linkedin.com/in/sukminyoon" color="#4E4A44">linkedin.com/in/sukminyoon</link>'
    ' | <link href="https://github.com/sukminc" color="#4E4A44">github.com/sukminc</link>'
    ' | <link href="https://onepercentbetter.dev" color="#4E4A44">onepercentbetter.dev</link>'
)

VARIANTS = {
    "data_engineer": {
        "filename": "Chris_Yoon_Data_Engineer_Resume_2026.pdf",
        "eyebrow": "Senior Data Engineer | Pipeline Reliability | Data Quality",
        "summary": (
            "Senior Data Engineer with 10+ years across pipeline orchestration, data quality, reconciliation, and production validation. "
            "At theScore / ESPN Bet, I built and maintained Airflow-orchestrated pipelines across BigQuery and Redshift for millions "
            "of daily transactions, created a Python observability framework that cut debugging overhead by 60 percent, and delivered "
            "SOX-facing workflows with full audit visibility. My edge is building data systems that stay trustworthy under pressure, "
            "then making failure visible early enough to fix it before it spreads."
        ),
        "strengths": [
            "<b>Data Engineering</b>  ETL and ELT design, Apache Airflow, warehouse modeling, reconciliation pipelines, schema drift handling, data quality gates",
            "<b>Languages and Querying</b>  Python, SQL, Pandas, NumPy, SQLAlchemy, FastAPI, TypeScript",
            "<b>Cloud and Platforms</b>  BigQuery, Redshift, PostgreSQL, Docker, GitHub Actions, Jenkins",
            "<b>What I Optimize For</b>  Reliable pipelines, auditable data movement, earlier failure detection, and clear communication under ambiguity",
        ],
        "opb_title": "Founder and Product Engineer",
        "opb_bullets": [
            "Built 1% Better.dev as a public build layer for recent work, linked repositories, and visible execution while pursuing my next data engineering role.",
            "Use small-scope products to keep shipping instincts sharp, shorten feedback loops, and stay hands-on across backend, data, and delivery decisions.",
            "Treat the platform as a credibility surface: a hiring manager can move from resume to live site to repo activity in minutes.",
        ],
        "project_section_title": "SELECTED PROJECTS",
        "projects": [
            {
                "name": "Blue Jays Moneyball ETL",
                "meta": "Public repo | Live",
                "url": "https://github.com/sukminc/bluejays-financial-mlops",
                "bullets": [
                    "Production-style Airflow and PostgreSQL pipeline with fail-fast data quality gates.",
                    "Includes regression coverage that proves the guardrails still fail when they should, treating data safety as part of CI rather than documentation.",
                ],
            },
            {
                "name": "1% Better Today",
                "meta": "Public repo | Current",
                "url": "https://github.com/sukminc/one-percent-better-today",
                "bullets": [
                    "Small daily reset product designed to be easy to release, easy to use, and easy to improve.",
                    "Shows that I can move from idea to shipped product without hiding behind long planning cycles.",
                ],
            },
            {
                "name": "1% Better Focus",
                "meta": "Public repo | Current",
                "url": "https://github.com/sukminc/one-percent-better-focus",
                "bullets": [
                    "Lightweight focus timer built around a narrow user loop, quick iteration, and low-friction product scope.",
                ],
            },
            {
                "name": "TwelveLabs API Validator",
                "meta": "Public repo | Live",
                "url": "https://github.com/sukminc/TwelveLabs",
                "bullets": [
                    "Python validation framework for multimodal search covering fuzzy matching, multilingual queries, and injection-style edge cases.",
                ],
            },
        ],
        "signal_title": "PUBLIC BUILD SIGNAL",
        "signal_body": [
            "1% Better.dev gives recruiters a fast way to verify how I work now, not just what I did before: live product framing, linked repositories, and recent activity that support the resume.",
            "The hiring story is straightforward: proven data engineering experience first, public shipping discipline second, AI learning in support of better execution rather than as the main claim.",
        ],
    },
    "ai_product_engineer": {
        "filename": "Chris_Yoon_AI_Product_Engineer_Resume_2026.pdf",
        "eyebrow": "AI Product Engineer | Full-Stack Builder | Public Build Discipline",
        "summary": (
            "Product-minded engineer with a data engineering backbone and 10+ years of production experience. "
            "My foundation was built in data pipelines, validation, and reliability work at scale, most recently at "
            "theScore / ESPN Bet. I now use 1% Better.dev as a public build studio to ship small applications, learn "
            "AI-assisted workflows deeply, and turn ideas into visible products quickly. The combination I bring is "
            "technical depth, fast iteration, and the discipline to keep improving in public."
        ),
        "strengths": [
            "<b>Product Engineering</b>  Fast iteration, MVP scoping, full-stack implementation, public shipping loops, recruiter-friendly proof of work",
            "<b>AI and Backend</b>  Python, FastAPI, LLM workflow integration, API orchestration, SQLAlchemy, Pandas, TypeScript, Next.js",
            "<b>Infrastructure</b>  PostgreSQL, Docker, GitHub Actions, BigQuery, Redshift, Stripe API, Pytest, Playwright",
            "<b>Value I Bring</b>  Build speed, practical product judgment, technical range, and the confidence to ship while still learning",
        ],
        "opb_title": "Founder and AI Product Engineer",
        "opb_bullets": [
            "Built 1% Better.dev as a public product studio for fast-release apps, live portfolio proof, and continuous growth while job searching.",
            "Use ChatGPT and Claude as active collaborators in design, code, debugging, and iteration, which has dramatically increased my confidence and execution speed.",
            "Shipped and refined products such as 1% Better Today and 1% Better Focus to practice tight product loops instead of overbuilding in private.",
        ],
        "project_section_title": "SELECTED PRODUCTS",
        "projects": [
            {
                "name": "1% Better Today",
                "meta": "Public repo | Current",
                "url": "https://github.com/sukminc/one-percent-better-today",
                "bullets": [
                    "Small daily reset product built around minimal friction and immediate usefulness.",
                    "Represents the kind of narrow, shippable product I can move from concept to release quickly.",
                ],
            },
            {
                "name": "1% Better Focus",
                "meta": "Public repo | Current",
                "url": "https://github.com/sukminc/one-percent-better-focus",
                "bullets": [
                    "Lightweight focus timer shaped by the same thesis: clear value, low complexity, and visible progress.",
                ],
            },
            {
                "name": "ActionKeeper",
                "meta": "Public repo | Building",
                "url": "https://github.com/sukminc/one-percent-better-poker-staking",
                "bullets": [
                    "Full-stack workflow product for structured offers, counters, and agreement tracking with persistent audit history.",
                    "Shows product thinking around trust, negotiation state, and multi-step user flows.",
                ],
            },
            {
                "name": "Blue Jays Moneyball ETL",
                "meta": "Public repo | Live",
                "url": "https://github.com/sukminc/bluejays-financial-mlops",
                "bullets": [
                    "Keeps my backend and data engineering edge sharp through production-style pipelines and guardrail design.",
                ],
            },
        ],
        "signal_title": "WHY THIS PROFILE WORKS",
        "signal_body": [
            "I am intentionally targeting AI Product Engineer roles where shipping, taste, and technical adaptability matter as much as years in one exact stack.",
            "1% Better.dev lets hiring teams see the through-line from resume to shipped work to recent activity, which makes the story easier to trust.",
        ],
    },
}


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


def bullets(items, styles):
    bullet_lines = []
    for item in items:
        bullet_lines.append(Paragraph(f"•&nbsp;{item}", styles["bullet"]))
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
            'North York, ON | 416-300-7316 | <link href="mailto:chris.yoon@outlook.com" color="#4E4A44">chris.yoon@outlook.com</link>',
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
        items.extend(role(config["opb_title"], "1% Better.dev", "Toronto, ON | Jul 2025 - Present", styles))
        items.extend(bullets(config["opb_bullets"], styles))
    else:
        items.extend(role(config["opb_title"], "1% Better.dev", "Toronto, ON | Jul 2025 - Present", styles))
        items.extend(bullets(config["opb_bullets"], styles))
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
