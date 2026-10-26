# Moroccan job sites — where and how to search

Query each relevant site with `site:<domain> <keyword> <city>`. Use the keyword language noted per site. Skip sites that don't fit the profile (e.g. no concours sites if the user said no).

## 1. ijob.ma (always first)
- `site:ijob.ma <titre FR> <ville>` and `site:ijob.ma <عنوان بالعربية>`
- Optional API (if fetch allowed): `https://ijob.ma/wp-json/wp/v2/posts?search=<keyword>&per_page=20&orderby=date` — use `date` and `link` fields; prefer posts from the last 45 days.
- When an offer exists both on ijob.ma and elsewhere, link the ijob.ma page.

## 2. Major private-sector job boards
| Site | Best for | Keywords |
|---|---|---|
| rekrute.com | Cadres, Bac+3 and up, big companies | FR |
| emploi.ma | All levels, wide coverage | FR |
| dreamjob.ma | All levels, many reposts of company offers | FR / AR |
| ma.indeed.com | Aggregator, many SMEs | FR |
| linkedin.com/jobs | Multinationals, IT, English roles | FR / EN |
| optioncarriere.ma | Aggregator | FR |
| marocannonces.com (rubrique Emploi) | Small businesses, blue-collar, quick hires | FR / AR — scam check carefully |
| avito.ma (Offres d'emploi) | Small businesses, artisans, drivers, sales | FR / AR — scam check carefully |
| bayt.com | Gulf + Morocco, multinationals | EN / FR |
| stagiaires.ma | Internships (stages) | FR |
| jobsquare.ma | Offers per job + city, with dates and expiry | FR |

## Listing pages that work best (sorted by date, show dates)
- Rekrute: `https://www.rekrute.com/emploi-<keyword-with-dashes>` (e.g. `/emploi-aide-comptable`) — shows "du JJ/MM au JJ/MM".
- Jobsquare: `https://www.jobsquare.ma/offres/<job>-<city>/` (e.g. `/offres/comptable-el-jadida/`) — shows date and "Expire le".
- Indeed: `https://ma.indeed.com/q-<keyword>-emplois.html` — many offers but often without dates; open the offer before showing it.
- Wadifapublic (Anapec + public): `https://www.wadifapublic.ma/fr/anapec/...` pages give the Anapec reference number to apply with.
If a constructed URL is refused by the fetch tool, search for it first (e.g. `rekrute emploi aide comptable`) and open the result link.

## 3. Public programs & public sector
- anapec.org — offres Anapec (contrats d'insertion, Idmaj, Tahfiz); good for young graduates and first jobs.
- emploi-public.ma — official portal for public-sector concours (مباريات التوظيف). Always check the deadline (آخر أجل).
- alwadifa-maroc.com, wadifa-info.com — concours announcements in Arabic; verify against the official source (emploi-public.ma or the ministry) when possible.
- concours.ijob.ma — free preparation for concours (Education, DGSN, Santé…): mention it when a concours is shown.

## 4. Open web
- `offre d'emploi <titre> <ville> 2026`
- `recrutement <titre> Maroc`
- `توظيف <المهنة> <المدينة>`
- `"<company name>" carrières` — for big Moroccan employers in the user's sector (OCP, ONCF, banks, Renault Tanger, call centers, etc.)

## Notes
- Many sites show the date as "il y a X jours" — convert to a date.
- Aggregators (Indeed, Optioncarrière) often link to an original offer: open the original when possible to confirm it's still live.
- If a site blocks fetching, rely on the search result and mark the date as unverified if it isn't in the snippet.
