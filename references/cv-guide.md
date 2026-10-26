# Building a professional CV for the Moroccan job market

## 1. Collect the information
**Interactive first:** show `assets/cv-form.html` (fill `L` in the user's language; if an old CV is attached, fill `PREFILL` from it so the user only completes what's missing). Its button sends a message starting with `[ijob-cv]` — build the CV from that.

Text fallback (one message, numbered). If an old CV is attached, read it and only ask what's missing. Otherwise ask, in the user's language:

1. Nom complet, ville, téléphone, email (and LinkedIn if any)
2. Le poste visé (one main target role)
3. Diplômes: intitulé exact, établissement, ville, année (most recent first). Include OFPPT, BTS, DUT, Licence, Master, Bac (série + année)
4. Expériences: poste, entreprise, ville, dates (mois/année), 2–4 tâches or results for each. Stages count — include them.
5. Compétences: logiciels/outils (Excel, Sage, AutoCAD…), techniques métier, permis de conduire
6. Langues + niveau (Arabe, Français, Anglais, Espagnol, Amazigh…)
7. (Optional) Certifications, bénévolat, activités, centres d'intérêt

Accept short or messy answers (voice-like Darija is fine). Never invent a diploma, employer, date, result or skill. If something is vague, write it modestly rather than inflating it.

## 2. Language and format
- **Default: French** — it is the language of most private-sector recruiters in Morocco. Offer an **English** version for multinationals / call centers / IT, and an **Arabic** version for public sector or Arabic-speaking employers if the user wants.
- **1 page** for under ~5 years of experience; 2 pages max otherwise.
- **ATS-friendly**: single column, standard section titles, no tables for layout, no text inside images, no icons-only info, standard fonts (Calibri / Arial / Helvetica), 10–11 pt body.
- Photo: optional in Morocco. Only add if the user provides one and wants it. Never generate or alter a photo.
- Do NOT include: CIN number, full home address (city is enough), religion, marital status unless the user insists, salary history.

## 3. Structure (in this order)
1. **En-tête**: Nom Prénom (large) · Poste visé · Ville · Téléphone · Email · LinkedIn
2. **Profil** (2–3 lines): who they are, years of experience, main strength, what they're looking for. Tailored to the target role. No clichés ("dynamique et motivé" alone means nothing — back it with a fact).
3. **Expérience professionnelle** (reverse chronological): Poste — Entreprise, Ville | MM/AAAA – MM/AAAA, then 2–4 bullets starting with an action verb (Saisir, Gérer, Assurer, Réaliser, Accompagner…), with numbers when the user gave them (nombre de clients, factures/mois, CA…).
4. **Formation**: Diplôme — Établissement, Ville | Année. Add "Projet de fin d'études: …" when relevant for juniors.
5. **Compétences**: grouped (Techniques / Logiciels / Permis).
6. **Langues**: with level (Langue maternelle, Courant, Intermédiaire, Notions — or CEFR B2 etc.).
7. **Certifications / Activités** (only if real and useful).

For candidates without experience: put Formation before Expérience, and give stages / projects / bénévolat full bullet points.

## 4. Keywords
Use the exact job title and keywords from the target offer(s) when known (e.g. "comptabilité générale", "rapprochement bancaire", "déclarations TVA"). This is what recruiters and ATS filters search for.

## 5. Output
- If the conversation can create files and a Word (docx) or PDF skill is available, produce a **.docx** (editable) and, if possible, a **PDF** copy. File name: `CV_Prenom_Nom.docx`.
- Otherwise, write the full CV in a clean, copy-ready format (markdown with clear sections) the user can paste into Word or Google Docs.
- After delivering, show `assets/cv-result.html` (honest strength score, what's good, 1–3 tips, action buttons, ijob.ma links) and keep the text to one line. Text fallback: give 2–3 short improvement tips, offer a version in another language, offer a lettre de motivation, and offer to **search matching jobs with this CV right away** (go to Step 1 of the skill with the profile already filled).
