"""Georgia tax sales, redemption, barment and liens that survive (Atlanta: Fulton and DeKalb counties)."""

CHAPTER = "Georgia Tax Sales"
CH_RED = "Redemption & Barment"
CH_LIEN = "Liens & Due Diligence"
CH_JUD = "Judicial In Rem Sales"

CORE = [
    ("Georgia sells which of these at a county tax sale?",
     ["A tax lien certificate that earns interest", "A tax deed that the owner can still redeem",
      "A sheriff's warranty deed with no redemption", "A lease on the property until taxes are paid"], 1,
     "Georgia is a redeemable tax DEED state. The winning bidder gets a tax deed, but the owner and anyone with a "
     "recorded interest can redeem it (O.C.G.A. 48-4-40)."),
    ("How long does the owner have to redeem after a Georgia tax sale before the buyer can start barring redemption?",
     ["30 days", "6 months", "12 months", "3 years"], 2,
     "Redemption is allowed any time within 12 months of the sale, and afterwards until the buyer forecloses the "
     "right of redemption with proper notice (O.C.G.A. 48-4-40 and 48-4-45)."),
    ("You paid $10,000 at a tax sale. The owner redeems 8 months later and you paid no other taxes. What is the "
     "redemption price?",
     ["$10,000", "$11,000", "$12,000", "$13,000"], 2,
     "Amount paid plus a 20% premium for the first year or any fraction of a year: $10,000 + $2,000 = $12,000 "
     "(O.C.G.A. 48-4-42)."),
    ("You paid $10,000 at a tax sale. The owner redeems 18 months later. What premium is added?",
     ["20% total", "30% total (20% first year + 10% for the partial second year)", "10% total", "40% total"], 1,
     "20% for the first year or fraction, plus 10% for each year or fraction after that. 18 months = 20% + 10% = "
     "30%, so $13,000 plus any later taxes you paid (O.C.G.A. 48-4-42)."),
    ("During the redemption period, who is entitled to rents and profits from the property?",
     ["The tax sale buyer", "The county", "Not the tax sale buyer - the buyer has no immediate control",
      "Whoever collects first"], 2,
     "DeKalb County's tax sale rules state the purchaser is not entitled to rents or profits during the redemption "
     "period. The buyer has a defeasible title, not possession."),
    ("Why is it risky to start renovating right after you win a Georgia tax sale?",
     ["Renovation is illegal in Atlanta", "The owner can still redeem and you are only repaid the price, later taxes, "
      "HOA/condo dues and the premium - not your repair costs", "The county keeps your bid if you renovate",
      "Permits cannot be issued for 10 years"], 1,
     "Redemption pays back what O.C.G.A. 48-4-42 lists: the bid, taxes and special assessments you paid, certain "
     "association dues, sheriff/publication costs and the premium. Repair money is not on that list."),
    ("After the 12 months pass, what must the tax deed buyer do to cut off redemption (\"barment\")?",
     ["Nothing - it ends automatically", "Serve a notice of foreclosure of the right to redeem on the owner, the "
      "occupant and everyone with a recorded interest, and publish it", "Change the locks", "Pay the owner 10%"], 1,
     "O.C.G.A. 48-4-45 requires sheriff service on in-county parties, certified/registered mail to out-of-county "
     "parties, and newspaper publication once a week for four weeks."),
    ("What happens to the owner's existing mortgage (security deed) when the owner redeems?",
     ["It is erased", "Title goes back to the owner subject to all liens that existed at the time of the tax sale",
      "It transfers to the tax buyer", "It becomes a county lien"], 1,
     "Redemption puts title back in the owner subject to all liens existing at the time of the tax sale "
     "(O.C.G.A. 48-4-43)."),
    ("If a lender (not the owner) pays the redemption price, what does the lender get?",
     ["Nothing", "A first lien on the property for the amount paid, if the quitclaim deed is recorded",
      "Ownership of the property", "A tax refund"], 1,
     "A creditor or interested party who redeems gets a first lien for the amount spent, repaid before other claims "
     "once the quitclaim deed is recorded (O.C.G.A. 48-4-43)."),
    ("When a property is redeemed, what document must the tax sale buyer give?",
     ["A warranty deed", "A quitclaim deed back to the defendant in fi. fa.", "A bill of sale", "Nothing"], 1,
     "The purchaser makes a quitclaim deed reciting who paid and in what capacity, and records it within 10 days "
     "of redemption (O.C.G.A. 48-4-44)."),
    ("A tax deed recorded after July 1, 1996 ripens into fee simple title by prescription after how long, even "
     "without barment notice?",
     ["1 year", "4 years from recording", "7 years from the sale", "20 years"], 1,
     "O.C.G.A. 48-4-48: four years from recordation for deeds properly executed on or after July 1, 1996. Barment "
     "notice is not required for ripening."),
    ("Who gets the excess money when a tax sale brings more than the taxes and costs?",
     ["The buyer", "The county keeps it", "The owner and lienholders in order of priority, after notice from the "
      "tax commissioner", "The sheriff"], 2,
     "The officer must mail notice of excess funds within 30 days to the record owner, security deed holders and "
     "other recorded interests; funds go to them in order of priority (O.C.G.A. 48-4-5)."),
    ("What is the starting bid at a DeKalb County tax sale?",
     ["$1", "Half the assessed value", "The total of taxes and costs (levy, recording, advertising, commissions)",
      "The fair market value"], 2,
     "DeKalb's published rules: bidding starts at taxes and costs and the property goes to the highest bidder. "
     "If no one bids, the county may bid the starting amount."),
    ("A federal (IRS) tax lien was properly notified before a tax sale. How long does the United States have to "
     "redeem?",
     ["It cannot redeem", "120 days or the state redemption period, whichever is longer", "30 days", "5 years"], 1,
     "26 U.S.C. 7425(d): 120 days from the sale or the local redemption period, whichever is longer."),
    ("After barment notice is given, can the old owner sue to cancel your tax deed without paying anything?",
     ["Yes, any time", "Not unless they pay or tender the full redemption price, except when the tax was not due or "
      "notice was not properly given", "Only within 30 days", "Never under any circumstance"], 1,
     "O.C.G.A. 48-4-47 bars suits to set aside the deed unless the redemption price is tendered, with exceptions for "
     "taxes not due or improper notice."),
    ("After barring redemption, why do most investors still file a quiet title action before reselling?",
     ["It is required to get a permit", "Title insurers usually will not insure a tax deed title until a court "
      "clears the clouds on it", "It lowers property taxes", "It cancels code violations"], 1,
     "Georgia's Quiet Title Act lets a person holding land under a tax deed sue in rem against all the world to "
     "remove clouds, including an equity of redemption (O.C.G.A. 23-3-61). A court order makes title insurable."),
    ("A City of Atlanta demolition or repair lien under the unsafe building law ranks how?",
     ["Below every mortgage", "Superior to all other liens except tax liens", "It is not a lien", "Equal to "
      "credit card debt"], 1,
     "O.C.G.A. 41-2-9: the lien for repair, closure or demolition costs is superior to all other liens except taxes "
     "and continues until paid. Check for these before you bid."),
    ("Where do you look for code enforcement orders and lis pendens before bidding?",
     ["Only on the property's front door", "The Clerk of Superior Court deed records and general execution docket, "
      "plus the city's code enforcement records", "The DMV", "The IRS website"], 1,
     "Unsafe-building complaints require a lis pendens, and the order and lien are recorded in the deed records and "
     "entered on the general execution docket (O.C.G.A. 41-2-12 and 41-2-9)."),
    ("Under the judicial in rem tax foreclosure process, how long does the owner have to redeem after the sale?",
     ["12 months", "60 days, by paying the minimum bid into court", "No time at all", "4 years"], 1,
     "O.C.G.A. 48-4-81(c): the owner's right of redemption lasts 60 days after a judicial in rem sale."),
    ("What does a judicial in rem tax sale do that a regular nonjudicial tax sale does not?",
     ["Nothing different", "Sells the property free and clear of most liens under a superior court order, with a "
      "short 60-day owner redemption", "Gives the buyer a lease", "Requires the buyer to live there"], 1,
     "O.C.G.A. 48-4-79 orders the sale free and clear of all liens except federal redemption rights, other "
     "Georgia tax liens, easements and recorded covenants."),
]

CHAPTER_OF = {q[0]: CHAPTER for q in CORE}
for _q in CORE[5:11]:
    CHAPTER_OF[_q[0]] = CH_RED
for _q in CORE[13:18]:
    CHAPTER_OF[_q[0]] = CH_LIEN
for _q in CORE[18:]:
    CHAPTER_OF[_q[0]] = CH_JUD

FACTS = [
    ("Georgia tax sales of real property are held on which day", "The first Tuesday of the month",
     ["The last Friday of the month", "Every Monday", "The 15th of each month"],
     "Sheriff's and tax sales are held on the first Tuesday of each month (O.C.G.A. 9-13-161).", CHAPTER),
    ("Between which hours must a Georgia sheriff's or tax sale take place", "10:00 a.m. and 4:00 p.m.",
     ["8:00 a.m. and noon", "Noon and 8:00 p.m.", "Any time the sheriff chooses"],
     "Sales are at public outcry between 10 a.m. and 4 p.m. (O.C.G.A. 9-13-161).", CHAPTER),
    ("If the first Tuesday is New Year's Day or July 4th, the sale moves to", "The next Wednesday",
     ["The next Monday", "The following month", "The day before"],
     "O.C.G.A. 9-13-161 moves the sale to the immediately following Wednesday.", CHAPTER),
    ("How long must a tax sale be advertised in the county legal organ", "Once a week for four weeks",
     ["One day", "Once a week for two weeks", "Six months"],
     "Sales of land are advertised weekly for four weeks in the legal organ (O.C.G.A. 9-13-140).", CHAPTER),
    ("How many days of written notice must the delinquent owner get before a tax sale", "10 days by certified or "
     "registered mail", ["3 days by phone", "No notice is required", "1 year by email"],
     "O.C.G.A. 48-4-1 requires ten days' written notice by registered/certified mail or statutory overnight "
     "delivery.", CHAPTER),
    ("DeKalb County's legal organ for tax sale notices is", "The Champion Newspaper",
     ["The Wall Street Journal", "The county Facebook page", "There is none"],
     "DeKalb publishes tax sale notices in The Champion, its legal organ.", CHAPTER),
    ("A Georgia property tax lien attaches to the property on", "January 1 of the tax year",
     ["The day the bill is mailed", "The day of the tax sale", "December 31"],
     "The tax lien attaches as of January 1 and is superior to other liens (O.C.G.A. 48-2-56, cited by DeKalb).",
     CHAPTER),
    ("The document a tax commissioner issues against a delinquent taxpayer is called a", "Fi. fa. (tax execution)",
     ["Lis pendens", "Quitclaim", "Certificate of occupancy"],
     "Delinquent taxes lead to an execution (fi. fa.) that lets the levying officer levy and sell.", CHAPTER),
    ("Can a Georgia tax commissioner be forced to sell you (transfer) a tax fi. fa.", "No - transfers are allowed "
     "but no officer is required to make one", ["Yes, always", "Only on Sundays", "Only to banks"],
     "O.C.G.A. 48-3-19: the officer may transfer an execution to someone paying it in full, but is never required "
     "to.", CHAPTER),
    ("Within how many days must a transferee record a transferred tax execution on the general execution docket",
     "30 days", ["7 days", "1 year", "No recording is needed"],
     "O.C.G.A. 48-3-19 requires entry on the general execution docket within 30 days of transfer.", CHAPTER),
    ("Tax sale buyers in Georgia compete by bidding", "Up the price - highest bidder wins",
     ["Down the interest rate", "Down the ownership percentage", "By lottery"],
     "Georgia sells deeds to the highest bidder; there is no interest-rate bidding like lien states.", CHAPTER),
    ("Before redemption is barred, the tax deed buyer holds", "A defeasible title that can be undone by redemption",
     ["Full fee simple ownership", "Only a lien", "A lease"],
     "Full ownership is not acquired until the redemption period has ended and proper barment is done.", CHAPTER),
    ("Who may redeem property from a Georgia tax sale", "The owner or anyone with a right, title, interest in or "
     "lien on the property", ["Only the owner's attorney", "Only the county", "Only the highest bidder"],
     "O.C.G.A. 48-4-40 lets the defendant in fi. fa. or any person with an interest or lien redeem.", CH_RED),
    ("The redemption premium for the first year or fraction of a year is", "20%",
     ["10%", "12%", "18%"], "O.C.G.A. 48-4-42(a)(3): 20% for the first year or fraction.", CH_RED),
    ("The redemption premium for each year or fraction after the first is", "10%",
     ["20%", "5%", "25%"], "O.C.G.A. 48-4-42(a)(3): 10% for each year or fraction after the first.", CH_RED),
    ("Besides the bid and premium, the redemption price also includes", "Taxes and special assessments the buyer "
     "paid after the sale", ["The buyer's renovation costs", "The buyer's travel costs", "Attorney fees for any "
     "reason"], "O.C.G.A. 48-4-42(a)(1)-(2) adds later taxes and special assessments.", CH_RED),
    ("For tax sales after July 1, 2016, the redemption price can also include", "HOA or condo association dues the "
     "buyer paid", ["Utility deposits", "Lawn care", "Insurance on the buyer's car"],
     "O.C.G.A. 48-4-42(c) adds sums paid to property owners', condominium or homeowners' associations.", CH_RED),
    ("If redemption happens more than 30 days after barment notice, the price also adds", "The sheriff's service "
     "cost and publication cost", ["Nothing extra", "A 50% penalty", "The buyer's income tax"],
     "O.C.G.A. 48-4-42(b).", CH_RED),
    ("Redemption money must be paid", "In lawful U.S. money to the tax sale purchaser or successors",
     ["In gold to the county", "By personal IOU", "To the sheriff only"], "O.C.G.A. 48-4-42(d).", CH_RED),
    ("Barment notice may first be served", "After 12 months from the tax sale",
     ["The day after the sale", "After 30 days", "After 4 years"], "O.C.G.A. 48-4-45(a).", CH_RED),
    ("Barment notice must be served on", "The defendant in fi. fa., the occupant, and all persons with a recorded "
     "interest or lien", ["Only the owner", "Only the occupant", "Only the county"],
     "O.C.G.A. 48-4-45(a)(1).", CH_RED),
    ("Out-of-county parties entitled to barment notice must be sent it by", "Registered or certified mail or "
     "statutory overnight delivery", ["Text message", "Regular postcard", "Nothing - they are skipped"],
     "O.C.G.A. 48-4-45(a)(2).", CH_RED),
    ("Barment notice must be published", "Once a week for four consecutive weeks in the six months before the "
     "redemption deadline week", ["Once, the day after the sale", "Daily for a year", "It is never published"],
     "O.C.G.A. 48-4-45(a)(3).", CH_RED),
    ("The buyer must deliver the barment notices to the sheriff at least how long before the redemption deadline",
     "45 days", ["5 days", "10 days", "1 year"], "O.C.G.A. 48-4-46(b).", CH_RED),
    ("After receiving barment notices, the sheriff must serve in-county parties within", "15 days",
     ["2 days", "90 days", "6 months"], "O.C.G.A. 48-4-46(b).", CH_RED),
    ("If the sheriff cannot serve someone, the buyer must publish notice", "Once a week for two consecutive weeks",
     ["Never", "Once", "For a full year"], "O.C.G.A. 48-4-46(c).", CH_RED),
    ("Leaving a copy of the barment notice at a person's residence is", "Sufficient service",
     ["Not allowed", "Only allowed for corporations", "A crime"], "O.C.G.A. 48-4-46(b).", CH_RED),
    ("Heirs of a deceased owner entitled to barment notice must be", "Served by the sheriff or notified as the "
     "article provides", ["Ignored", "Called by phone only", "Paid $100"], "O.C.G.A. 48-4-45(c).", CH_RED),
    ("After redemption, the buyer must record the quitclaim deed within", "10 days of redemption",
     ["1 day", "90 days", "1 year"], "O.C.G.A. 48-4-44(e); the buyer pays recording costs.", CH_RED),
    ("If no quitclaim deed or witnesses are present at redemption, the buyer must sign one within", "7 days",
     ["24 hours", "30 days", "6 months"], "O.C.G.A. 48-4-44(d).", CH_RED),
    ("A tax deed recorded on or after July 1, 1996 ripens by prescription", "4 years after recording",
     ["1 year after the sale", "7 years after the sale", "Never"], "O.C.G.A. 48-4-48(b).", CH_RED),
    ("Excess funds notice must be mailed within", "30 days after the tax sale",
     ["1 year", "5 days", "It is optional"], "O.C.G.A. 48-4-5(a).", CHAPTER),
    ("Unclaimed tax sale excess funds go to the Georgia Department of Revenue after", "5 years",
     ["30 days", "1 year", "20 years"], "O.C.G.A. 48-4-5(c).", CHAPTER),
    ("The IRS's redemption window after a tax sale is", "120 days or the state period, whichever is longer",
     ["7 days", "Exactly 12 months always", "It has none"], "26 U.S.C. 7425(d)(1).", CH_LIEN),
    ("A judicial in rem tax foreclosure petition cannot be filed until taxes have been delinquent for",
     "12 months", ["1 month", "5 years", "10 days"], "O.C.G.A. 48-4-78(a).", CH_JUD),
    ("The hearing on a judicial in rem tax petition is held no earlier than", "30 days after filing",
     ["The same day", "1 year after filing", "7 days after filing"], "O.C.G.A. 48-4-79(a).", CH_JUD),
    ("A judicial in rem tax sale may not happen earlier than", "45 days after the court's order",
     ["The next day", "1 year after the order", "10 days after the order"], "O.C.G.A. 48-4-81(a).", CH_JUD),
    ("The minimum bid at a judicial in rem tax sale is", "The redemption amount",
     ["$1", "Fair market value", "Twice the taxes"], "O.C.G.A. 48-4-81(b).", CH_JUD),
    ("After a judicial in rem sale is not redeemed, the deed must be delivered within", "90 days of the sale",
     ["1 day", "4 years", "10 years"], "O.C.G.A. 48-4-81(d).", CH_JUD),
    ("Liens that SURVIVE a judicial in rem tax sale include", "Federal redemption rights, other Georgia tax liens, "
     "easements and recorded covenants", ["Every mortgage", "Credit card judgments", "Nothing survives"],
     "O.C.G.A. 48-4-79(b).", CH_JUD),
    ("A code enforcement repair or demolition lien attaches when", "A certified copy of the order is filed with the "
     "Clerk of Superior Court, relating back to the lis pendens", ["The inspector drives by", "The owner dies",
     "The property is sold"], "O.C.G.A. 41-2-9.", CH_LIEN),
    ("An unsafe-building complaint must be mailed to interested parties at least how long before the hearing",
     "14 days", ["1 day", "90 days", "1 year"], "O.C.G.A. 41-2-12(a).", CH_LIEN),
    ("How many residents can request an unsafe-building inspection under Georgia law", "Five residents",
     ["One hundred residents", "Only the mayor", "No residents"], "O.C.G.A. 41-2-9(a)(3).", CH_LIEN),
    ("Before you bid, a lis pendens on a property means", "A lawsuit affecting the property is pending",
     ["The taxes are paid", "The house is new", "The owner moved"],
     "Code cases and other suits are recorded as lis pendens with the Clerk of Superior Court.", CH_LIEN),
    ("A Georgia water supplier with separate meters may refuse service to a new owner because of the prior owner's "
     "unpaid bill", "False - it must seek payment from the person who ran up the charges",
     ["True, always", "True, only in Atlanta", "True if over $100"], "O.C.G.A. 36-60-17(a)-(b).", CH_LIEN),
    ("A buyer or closing attorney can request a written statement of past-due water charges, which the supplier must "
     "send within", "10 business days for no more than $10", ["1 hour for free", "90 days for $500",
     "They cannot request it"], "O.C.G.A. 36-60-17(c).", CH_LIEN),
    ("The best place to check open City of Atlanta building permits, stop work orders and violations is",
     "The city's Accela portal (aca-prod.accela.com/atlanta_ga)", ["Craigslist", "The DMV", "The post office"],
     "Atlanta's Office of Buildings runs permits and inspections through Accela.", CH_LIEN),
    ("Before bidding on an Atlanta property you should always", "Drive by it, pull title, check code cases, water "
     "bills and HOA status", ["Bid on photos only", "Skip title work to save money", "Assume all liens are wiped"],
     "Tax sales are as-is. Due diligence is the only protection against surviving liens and a bad house.", CH_LIEN),
    ("A nonjudicial Georgia tax deed buyer should expect title insurance to be", "Hard to get until redemption is "
     "barred and usually a quiet title is done", ["Automatic", "Free from the county", "Required by law at the "
     "sale"], "Quiet title (O.C.G.A. 23-3-61) is the usual path to insurable title.", CH_LIEN),
    ("Fulton County tax bills for City of Atlanta property are collected by", "The Fulton County Tax Commissioner",
     ["The Atlanta Police", "The IRS", "The State Bar"],
     "Fulton's Tax Commissioner collects for Fulton County, Atlanta schools, the State and the City of Atlanta.",
     CHAPTER),
    ("Part of the City of Atlanta lies in which second county besides Fulton", "DeKalb County",
     ["Cobb County", "Chatham County", "Clarke County"],
     "Atlanta spans Fulton and DeKalb, so check which county runs the sale for your parcel.", CHAPTER),
]
