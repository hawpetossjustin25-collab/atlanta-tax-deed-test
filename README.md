# Atlanta Tax Deed, Real Estate & Rehab - Adaptive Practice Test

100% free forever. Works offline. Built the same way as the
[Minnesota permit test](https://github.com/hawpetossjustin25-collab/minnesota-permit-test).

**Phone/web version:** https://hawpetossjustin25-collab.github.io/atlanta-tax-deed-test/
(open on your phone, then "Add to Home Screen").

## What it covers (1,000 questions)
- **Georgia tax sales**: Georgia sells redeemable *tax deeds* (not interest lien certificates); first-Tuesday
  courthouse sales, notice, bidding, excess funds (O.C.G.A. 48-4, 9-13).
- **Redemption & barment**: 12-month redemption, 20% / 10% premiums, barment notice, quitclaim, 4-year
  prescription, quiet title, IRS 120-day redemption.
- **Liens & due diligence**: liens that survive (city repair/demolition liens rank above everything but taxes),
  lis pendens, water bills, open permits.
- **Judicial in rem sales**: 60-day redemption, free-and-clear sales.
- **Real estate basics, deal math, financing & foreclosure, landlord & tenant.**
- **Rehab & permits / avoiding code liens / trees, historic & lead**: City of Atlanta Office of Buildings rules,
  permit expiration, the 2026 Tree Protection Ordinance, historic districts, lead RRP, contractor liens.

## How the test works
- Every run shows all 1,000 questions, shuffled.
- Max 15 wrong; the 16th wrong answer restarts the test instantly.
- Miss a question and the right answer and explanation are shown for 8 seconds, then the next question comes up.
- Missed questions come back first, then unseen ones, then ones you know. Progress is saved.
- Wrong Answers tab with explanations, CSV export, Study Guide tab.

## Install
```
pip install git+https://github.com/hawpetossjustin25-collab/atlanta-tax-deed-test.git
atl-tax-deed-test
```
Or download the ZIP and double-click `start_tax_deed_test.bat`.

## Development
```
pip install -e .[test]
python -m pytest              # bank validity, engine rules, web build, GUI flow
python -m atl_tax_deed_test.webgen   # rebuild index.html from the question bank
```

*Study tool only, not legal advice. Laws and city rules change; confirm with the county tax commissioner, the City of
Atlanta and a Georgia real estate attorney before you bid or build.*
