# Search strategy

## Keywords
Build 3–6 keyword sets from the profile:
- **Titles in the local language(s)** of the target market, with gender forms where the language has them (infirmier / infirmière, Krankenpfleger / Pflegefachfrau), official short forms (IDE, RN, LPN), and English for multinationals and tech.
- **Synonyms and adjacent titles**: comptable → aide-comptable, chargé de comptabilité, gestionnaire comptable; software developer → software engineer, web developer, full-stack developer.
- **Seniority variants**: junior, entry-level, graduate, new grad, débutant, recién egresado, fresh graduate; or senior / lead for experienced profiles.
- **Skills that recruiters put in titles**: "React developer", "SAP FI accountant".
- **Places as written locally**: Montréal / Montreal, München / Munich, Casablanca / الدار البيضاء; plus the region or metro area (Grand Lyon, GTA for Toronto, Île-de-France).

## Query patterns
- Listing pages of each site (see the region file) — best, because they're sorted by date.
- `site:<domain> <title> <city>` — fallback; expect old results, so always open the offer.
- Open web: `<title> <city> job`, `offre d'emploi <titre> <ville>`, `oferta de empleo <puesto> <ciudad>`, `وظيفة <المسمى> <المدينة>`, `<title> <city> careers`.
- Company career pages: `"<employer>" careers <title>` for the big employers of the sector in that city (hospitals, banks, public transport, large tech firms…).
- Add the current year only if results are stale (never assume the year — use today's date).

## Breadth
- Run queries in parallel; 15–40 candidates before filtering.
- If a site blocks fetching, rely on a search result for that offer and mark the date "not verified" unless it's in the snippet.
- If a constructed URL is refused, search for it and open the result instead.

## Privacy
Never include in a query: the user's name, phone, email, ID/passport/social-security number, street address, date of birth, or their employer's internal details. Roles, skills, places only.

## Remote jobs
"Remote" often means "remote within one country or time zone". Check the offer's location restriction against the user's country before keeping it.
