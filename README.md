<!-- Generated from one-percent-better-os/public_profile.json via scripts/profile_sync.py -->
# Chris Yoon

Senior Data Engineer building reliable pipelines, quality-first data systems, and simple public products that prove recent execution.

Toronto, ON
Open to Senior Data Engineer, Analytics Engineer, Data Platform Engineer, AI Product Engineer roles
[LinkedIn](https://linkedin.com/in/sukminyoon) | [GitHub](https://github.com/sukminc) | [1% Better.dev](https://onepercentbetter.dev) | [1% Better.poker](https://onepercentbetter.poker)

[Resume: Data Engineer](./resume/Chris_Yoon_Data_Engineer_Resume_2026.pdf)

[Resume: AI Product Engineer](./resume/Chris_Yoon_AI_Product_Engineer_Resume_2026.pdf)

## Job Search Copilot

`LinkedIn`과 `Indeed` 저장 공고를 넣으면 현재 레쥬메 방향에 맞춰 어떤 버전으로 지원할지 추천하는 CLI를 추가했습니다.

무엇을 해주나:

- `Data Engineer`와 `AI Product Owner / Engineer` 트랙으로 공고를 점수화
- 각 공고에 맞는 추천 레쥬메 PDF 자동 선택
- 블로커(미국 거주 필수, 보안 클리어런스 등) 감지
- 현재 방향, 검색 쿼리, 지원 큐를 Markdown/JSON으로 출력
- 원하면 macOS `launchd`용 plist 생성

샘플 실행:

```bash
cd /Users/chrisyoon/GitHub/sukminc
python3 -m job_search.cli
```

직접 공고 파일 넣어서 실행:

```bash
cd /Users/chrisyoon/GitHub/sukminc
python3 -m job_search.cli \
  --input /absolute/path/to/jobs.csv \
  --output-dir /Users/chrisyoon/GitHub/sukminc/tmp/job_search/latest
```

입력 포맷은 CSV 또는 JSON이며 다음 필드를 지원합니다:

- `source`
- `title`
- `company`
- `location`
- `url`
- `description`
- `salary`
- `posted_at`
- `employment_type`
- `job_id`
- `notes`

스케줄링용 plist 생성:

```bash
cd /Users/chrisyoon/GitHub/sukminc
python3 -m job_search.cli \
  --input /absolute/path/to/jobs.csv \
  --write-launchd-plist /Users/chrisyoon/Library/LaunchAgents/com.chrisyoon.jobsearch.report.plist \
  --run-hour 9 \
  --run-minute 0
```

생성물:

- `tmp/job_search/latest/profile_snapshot.json`
- `tmp/job_search/latest/job_matches.json`
- `tmp/job_search/latest/job_search_report.md`

## What You Should Know

- 10+ years across data engineering, validation, migration, and data quality.
- Most recent full-time role: Senior Data Engineer at theScore / ESPN Bet.
- Main hiring story: proven data engineering experience first.
- Current public build track: 1% Better.dev, where I ship small products and show recent work in public.
- Poker remains a separate product vertical, not the main homepage story.

## Public Build Direction

- 1% Better is a simple-product brand, not a complexity brand.
- Public products should be small enough to explain in one sentence and ship in short loops.
- The website is a credibility layer for hiring, funding, and distribution.
- 1% Better OS is internal leverage. It should support the work, not become the main character.

## Experience Snapshot

### theScore / ESPN Bet
Senior Data Engineer | Jul 2023 - Jul 2025

- Built and maintained Airflow-orchestrated ETL pipelines across BigQuery and Redshift for millions of daily betting transactions.
- Designed a Python observability framework for 15+ pipelines that reduced debugging overhead by 60 percent.
- Delivered reconciliation workflows for SOX-compliant financial and regulatory reporting with full audit visibility.

### 1% Better.dev
Founder and Product Engineer | Jul 2025 - Present

- Built a public product studio that turns recent work into visible proof through a live site, linked repos, and ongoing activity.
- Use small products to keep shipping instincts sharp and stay hands-on across backend, data, and delivery decisions.
- Treat the platform as a credibility layer for recruiters and hiring managers rather than a place to make vague claims.

## Selected Work

| Project | Why it matters |
| --- | --- |
| [1% Better Today](https://github.com/sukminc/one-percent-better-today) | The core daily product: a narrow loop with the clearest chance of becoming the first real brand win. |
| [1% Better Focus](https://github.com/sukminc/one-percent-better-focus) | A lightweight focus timer that reinforces the same thesis: useful, simple, and shippable. |
| [1% Better - This Website](https://github.com/sukminc/one-percent-better-landing) | The live hiring, funding, and distribution layer that makes the rest of the work legible. |
| [Blue Jays Moneyball ETL](https://github.com/sukminc/bluejays-financial-mlops) | Production-style Airflow and PostgreSQL work that anchors the data-engineering side of the story. |
| [1% Better - Action Keeper](https://github.com/sukminc/one-percent-better-poker-staking) | A poker workflow product that shows trust-heavy product thinking without becoming the whole brand. |
| [TwelveLabs API Validator](https://github.com/sukminc/TwelveLabs) | An interview challenge archive that demonstrates validation rigor, edge-case handling, and quality discipline. |

## Hiring Signal

I do my best work where data correctness, pipeline reliability, and engineering judgment all matter.

The public story is straightforward: proven data engineering depth, simple products shipped in public, and AI used as an execution multiplier rather than a costume.
