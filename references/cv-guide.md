# Building a professional CV / resume

## 1. Collect the information
**Interactive first:** show `assets/cv-form.html`. Translate `L` into the user's language; if an old CV is attached, fill `PREFILL` from it so the user only completes what's missing. Its button sends a message starting with `[jobfinder-cv]` — build the CV from that.

Text fallback — one numbered message, only what's missing:
1. Full name, city and country, phone, email (LinkedIn / portfolio if any)
2. Target job (one main role) and target country
3. Education: exact diploma, school, city, year (most recent first)
4. Experience: title, employer, city, dates (month/year), 2–4 tasks or results each. Internships, freelance and volunteering count.
5. Skills: tools/software, job-specific skills, licences/registrations (e.g. nursing registration number is NOT needed — only "registered")
6. Languages + level
7. (Optional) certifications, projects, volunteering, interests

Accept short or messy answers. **Never invent** a diploma, employer, date, number, result or skill. If something is vague, write it modestly.

## 2. Universal rules
- **ATS-friendly**: single column, standard section headings, no tables or text boxes for layout, no text inside images, no icons-only info, standard fonts (Calibri, Arial, Helvetica, Liberation Sans), 10–11 pt body.
- **Length**: 1 page under ~5 years of experience, 2 pages max otherwise (exceptions: academic CVs, some countries below).
- **Reverse chronological**; for no-experience candidates, Education before Experience, and give projects/internships full bullets.
- **Bullets** start with an action verb, include numbers only if the user gave them.
- **Keywords** from the target offer, used truthfully.
- **Photo**: only if the user provides one AND it's customary in the target country. Never generate, edit or "enhance" a photo.
- **Never include** ID/passport/social-security numbers, full street address (city is enough), salary history, health, religion, political views.
- **File names**: `CV_Firstname_Lastname.docx` / `.pdf` (or `Resume_…` for US/Canada).

## 3. Country differences
Pick the format from the **country where the user will apply**, not where they live.

| Market | Name & length | Photo | Personal details | Notes |
|---|---|---|---|---|
| **France** | "CV", 1 page (2 if senior) | Optional, fading; omit by default | No age/DOB required; no marital status needed | Short "Profil"/"Accroche"; titles in French; diplomas with French equivalents (Bac+2, Bac+5) when foreign; "Permis B" if relevant |
| **Belgium / Switzerland / Luxembourg** | CV, 1–2 pages | Common in CH, optional elsewhere | CH: nationality + permit type often stated (B, C, G) if foreign | Languages very important; CEFR levels |
| **Germany / Austria** | "Lebenslauf", 1–2 pages, tabular | Optional (anti-discrimination law AGG); omit by default | DOB optional | Precise month/year dates; no unexplained gaps; often sent with a cover letter and certificates |
| **UK / Ireland** | "CV", 2 pages | **No** | **No** DOB, age, marital status | Personal statement 3–4 lines; "References available on request" optional |
| **USA** | "Resume", 1 page (2 if 10+ yrs) | **No** | **No** age/DOB, photo, marital status, religion, nationality (employers avoid them for anti-discrimination reasons) | Summary + achievements; US Letter size; state "Authorized to work in the US" only if true and relevant |
| **Canada** | "Resume" / "CV" (Québec), 2 pages | **No** | **No** DOB, SIN, marital status, photo | Québec: French CV; mention bilingualism level; work permit status only if relevant ("Open work permit") |
| **Europass (EU)** | Europass format | Optional | As per template | Useful for EU institutions, public sector, mobility programmes; heavier than a national CV — offer it, don't impose it |
| **Spain / Latin America** | "Currículum", 1–2 pages | Common but optional | DOB sometimes; omit by default | Spanish titles; LatAm: national ID numbers (CURP, RUT, CPF) **not** on the CV |
| **Brazil / Portugal** | "Currículo", 1–2 pages | Optional | Omit by default | Portuguese; objective line common in Brazil |
| **Gulf (UAE, Saudi, Qatar…)** | "CV", 2 pages | Common | Nationality, visa status, notice period often expected; DOB common but optional | English (Arabic for some public jobs); state visa status only if the user agrees |
| **Morocco / Maghreb** | CV, 1 page | Optional | Omit CIN; city only | French for private sector; Arabic version for public sector |
| **Sub-Saharan Africa** | CV, 2 pages | Varies | Omit ID numbers | English or French depending on country; referees section common in anglophone countries |
| **India** | "Resume", 1–2 pages | Optional | DOB/marital status often included locally but not required — omit by default | Career objective, key skills, projects for freshers |
| **Japan** | Rirekisho (fixed form) + Shokumu keirekisho | Yes on rirekisho | As per form | For Japanese employers suggest both documents; for foreign firms an English resume |
| **Australia / NZ** | "Resume", 2–3 pages | No | No DOB | Referees often listed (with their consent); key skills section |

When unsure for a country, use the UK/US-style neutral resume without photo or personal details, and say so.

## 4. Structure (adapt the headings' language)
1. **Header**: Name (large) · Target title · City, Country · Phone · Email · LinkedIn/portfolio
2. **Profile / Summary** (2–3 lines, tailored; no empty clichés — back each claim with a fact)
3. **Experience** — Title — Employer, City | MM/YYYY – MM/YYYY (or "Present"), 2–4 bullets
4. **Education** — Diploma — School, City | Year (+ final project for juniors)
5. **Skills** — grouped (Technical / Tools / Licences)
6. **Languages** — with level (native, fluent, CEFR B2…)
7. **Certifications / Projects / Volunteering** (only if real and useful)

## 5. Output
- If file creation is available: build a **.docx** with `scripts/build_cv_docx.py` (JSON format at the top of the script) — or with the docx skill — and a **PDF** copy with `scripts/build_cv_pdf.py`. Deliver both.
- Otherwise: give the full CV as clean, copy-ready text with clear headings.
- Then show `assets/cv-ready-card.html` (honest strength score, what's good, 1–3 tips, action buttons, itravail.com cards) with a one-line message. Text fallback: 2–3 tips, offer another language/country version, a cover letter, and to **search matching jobs right away** (Step 1 with the profile filled).

## 6. Strength score (honest, 0–100)
Start at 100 and subtract: missing target title (−15), no summary (−5), bullets without results/verbs (−10), missing dates (−10), missing contact (−15), length over limit (−5), layout not ATS-friendly (−10), no languages (−5), spelling issues (−5), photo/personal data against the target country's norms (−5). Never inflate.
