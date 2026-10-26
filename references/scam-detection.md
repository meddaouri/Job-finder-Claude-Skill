# Scam detection

Flag an offer with ⚠️ (and say why), or drop it, when you see any of these. Remind the user in one line: **a real employer never asks you to pay to get a job.**

## Universal red flags
1. **Asks for money** — application/processing fees, "training" or "starter kit" you must buy, equipment to buy from them, visa/work-permit/medical/insurance fees paid to the recruiter, "refundable deposit".
2. **Cheque or transfer schemes** — they send you a cheque or transfer and ask you to send part back, buy gift cards, or forward funds/parcels ("payment processing agent", "package reshipper"). Classic fake-cheque and money-mule fraud.
3. **Early requests for sensitive data** — bank login, card number, ID/passport scan or social-security number before any interview or signed offer.
4. **Unrealistic pay** for little work or no skills ("earn $500/day from home", "data entry 2h/day 3 000 €/month").
5. **Contact only by WhatsApp/Telegram/personal email**, no company domain, recruiter refuses a video call, interview by chat only.
6. **Hired instantly** — "you're selected" without any interview, or an offer for a job you never applied to.
7. **Vague or copied offer** — no company name, no address, generic text, many spelling errors, a company name that doesn't match the email domain or website.
8. **Pressure** — "reply in 1 hour", "only 2 places left".
9. **Task/"like-and-earn" jobs** — paid to like videos, rate products or "boost orders", where you must top up your own money to unlock earnings.
10. **Impersonation** — a real company or public body's name used on a look-alike domain. Check the domain against the official site.

## Verify quickly
- Search the company name + "scam" / "arnaque" / "estafa" / "احتيال".
- Check the offer also exists on the employer's official careers page.
- Compare the email domain with the official website.
- Public-sector jobs: confirm on the official government portal of that country (`special-tracks.md`). Public recruitment never requires paying an intermediary.

## Regional patterns (examples, not exhaustive)
- **Work abroad / visa sponsorship (all regions)**: agencies charging to "guarantee" a job, visa or work permit abroad; fake job offers from Canada, Gulf states, Europe asking for visa fees. Many countries cap or forbid recruitment fees charged to workers (ILO principle: employer pays). Treat any upfront fee as a red flag.
- **Europe / France**: fake "télétravail" offers for parcel reshipping or "agent de paiement"; offers asking for an IBAN + ID card scan before any interview; fake France Travail or company SMS.
- **North America**: fake-cheque "personal assistant" or "mystery shopper" jobs; equipment-purchase scams for remote jobs; fake recruiters on LinkedIn using real company names.
- **MENA / Gulf**: "visa + ticket" packages sold by agents; offers asking for passport copy and fees via WhatsApp; fake government recruitment pages.
- **Africa**: fees for "interview booking", medicals or "processing" for NGO/UN, oil & gas or mining jobs; fake recruitment for well-known public bodies on social media.
- **Asia-Pacific**: task/order-boosting scams via messaging apps; fake overseas jobs that lead to forced work in scam compounds — warn strongly about offers abroad with free flights, high pay and vague tasks.
- **Latin America**: "trabajo desde casa" with registration fees; fake offers using big retailers' names on social media; requests for CPF/CURP/RUT and bank data early.

## How to present
- In the card: set `scam:true` and put the reason in `gap`.
- In text: `⚠️ Possible scam: <reason>. A real employer never asks you to pay.`
- If most red flags are present, drop the offer and mention it in one line ("1 offer removed: asked for a fee").
