"""Real estate fundamentals for a Georgia investor: deeds, title, closing, financing, deal math, renting."""

CHAPTER = "Real Estate Basics"
CH_MATH = "Deal Math"
CH_RENT = "Landlord & Tenant"
CH_FIN = "Financing & Foreclosure"

CORE = [
    ("Georgia home loans are usually secured by which document?",
     ["A land contract", "A security deed (deed to secure debt)", "A bill of sale", "A lease"], 1,
     "Georgia uses security deeds, which let lenders foreclose by power of sale outside court."),
    ("Which deed gives the buyer the most protection?",
     ["Quitclaim deed", "General warranty deed", "Tax deed", "Limited warranty deed"], 1,
     "A general warranty deed warrants title against all claims, past and present. A quitclaim warrants nothing."),
    ("What does a quitclaim deed promise?",
     ["Clean title", "Nothing - it only passes whatever interest the grantor has", "Free title insurance",
      "No liens"], 1, "A quitclaim conveys only what the grantor owns, if anything."),
    ("What is ARV?",
     ["Annual rent value", "After repair value - what the house will be worth once fixed", "Assessed real value",
      "Average resale volume"], 1, "ARV comes from comparable sales of fixed-up homes nearby."),
    ("Using the 70% rule, ARV is $200,000 and repairs are $40,000. What is the most you should pay?",
     ["$100,000", "$140,000", "$160,000", "$180,000"], 0,
     "70% x $200,000 = $140,000, minus $40,000 repairs = $100,000. The 30% cushion covers holding, selling and "
     "profit."),
    ("A rental earns $12,000 a year in net operating income and costs $150,000. What is the cap rate?",
     ["6%", "8%", "10%", "12%"], 1, "Cap rate = NOI / price = 12,000 / 150,000 = 8%."),
    ("You put $50,000 cash into a rental that makes $5,000 a year after all expenses and loan payments. What is the "
     "cash-on-cash return?", ["5%", "10%", "15%", "50%"], 1, "Cash-on-cash = annual cash flow / cash invested."),
    ("What is the Georgia real estate transfer tax on a $250,000 sale?",
     ["$25", "$250", "$2,500", "$25,000"], 1,
     "$1 for the first $1,000 and 10 cents per $100 after that = $1 per $1,000 (O.C.G.A. 48-6-1)."),
    ("To get a Georgia homestead exemption for this year, you must have owned and lived in the home as of what date?",
     ["January 1", "April 15", "July 1", "December 31"], 0,
     "Homestead requires ownership and residence on January 1 (O.C.G.A. 48-5-40)."),
    ("A tenant stops paying rent in Georgia. What must the landlord do first?",
     ["Change the locks", "Demand possession, then file a dispossessory affidavit in court", "Remove the doors",
      "Shut off the water"], 1,
     "O.C.G.A. 44-7-50: demand possession, then file a dispossessory affidavit. Self-help eviction is not allowed."),
    ("After a dispossessory summons is served, how long does a Georgia tenant have to answer?",
     ["24 hours", "7 days", "30 days", "60 days"], 1, "O.C.G.A. 44-7-51(b): seven days from service."),
    ("Who must keep a rented house in repair in Georgia?",
     ["The tenant", "The landlord", "The city", "Nobody"], 1, "O.C.G.A. 44-7-13: the landlord must keep the "
     "premises in repair."),
    ("How much notice must a Georgia lender give before a nonjudicial foreclosure sale?",
     ["No notice", "At least 30 days' written notice to the debtor", "1 year", "5 days by phone"], 1,
     "O.C.G.A. 44-14-162.2."),
    ("What is a 1031 exchange?",
     ["A loan type", "A way to defer capital gains tax by trading one investment property for another",
      "A permit", "A tax lien"], 1, "Section 1031 lets investors defer gain when they buy like-kind replacement "
     "property under IRS timing rules."),
]

CHAPTER_OF = {q[0]: CHAPTER for q in CORE}
for _q in CORE[3:8]:
    CHAPTER_OF[_q[0]] = CH_MATH
for _q in CORE[9:12]:
    CHAPTER_OF[_q[0]] = CH_RENT
for _q in CORE[12:]:
    CHAPTER_OF[_q[0]] = CH_FIN

FACTS = [
    ("Real estate closings in Georgia are conducted by", "A licensed Georgia attorney",
     ["The real estate agent alone", "The buyer and seller with no one else", "The tax commissioner"],
     "Georgia is an attorney-closing state.", CHAPTER),
    ("Title insurance protects against", "Losses from defects in title that existed before you bought",
     ["Fire damage", "Tenant damage", "Price drops"], "Title policies cover past title defects, not physical "
     "damage.", CHAPTER),
    ("An owner's title policy protects", "The buyer", ["Only the lender", "The seller", "The real estate agent"],
     "The lender's policy protects the lender; the owner's policy protects you.", CHAPTER),
    ("Where are Georgia deeds recorded", "Clerk of Superior Court in the county where the land lies",
     ["The DMV", "The Secretary of State only", "The city water department"],
     "Deeds, security deeds, liens and lis pendens are recorded with the Clerk of Superior Court.", CHAPTER),
    ("The legal description of a property is found", "On the recorded deed and plat",
     ["On the mailbox", "On the tax bill only", "In the MLS photos"], "Use the deed and plat, not just the street "
     "address.", CHAPTER),
    ("Earnest money in a purchase contract is", "A good-faith deposit held until closing",
     ["The agent's commission", "The down payment refund", "A tax"], "It shows the buyer is serious.", CHAPTER),
    ("A buyer's due diligence period in a Georgia contract lets the buyer", "Inspect and walk away for any reason "
     "before it ends", ["Move in early", "Skip closing costs", "Change the price after closing"],
     "Georgia Association of REALTORS forms include a due diligence period.", CHAPTER),
    ("Zoning tells you", "What a property may legally be used for and how it can be built",
     ["Who owns it", "Its exact value", "How many taxes are unpaid"], "Check zoning before planning a duplex, ADU "
     "or rental.", CHAPTER),
    ("An easement is", "A right for someone else to use part of your land for a purpose",
     ["A type of mortgage", "A tax break", "A building permit"], "Utility easements are common and survive most "
     "sales.", CHAPTER),
    ("A lien is", "A legal claim against property to secure a debt", ["A type of deed", "A zoning rule",
     "An inspection report"], "Liens must be paid or cleared to deliver clean title.", CHAPTER),
    ("Comparable sales (comps) should be", "Recent, nearby sales of similar homes",
     ["Asking prices from anywhere", "Sales from 10 years ago", "Homes in other states"],
     "Use closed sales, ideally within six months and a short distance.", CH_MATH),
    ("Net operating income (NOI) is", "Rental income minus operating expenses, before loan payments",
     ["Rent minus the mortgage", "Gross rent", "Purchase price minus repairs"], "Debt service is not an operating "
     "expense.", CH_MATH),
    ("The 1% rule says monthly rent should be about", "1% of the all-in purchase price",
     ["10% of the price", "0.1% of the price", "Equal to the tax bill"], "It is a quick screen, not a full "
     "analysis.", CH_MATH),
    ("Holding costs on a flip include", "Taxes, insurance, utilities and loan interest while you own it",
     ["Only the purchase price", "Only the agent fee", "Nothing"], "Every month of delay costs money.", CH_MATH),
    ("A repair contingency budget is usually", "10-20% of the repair estimate",
     ["0%", "100% of the estimate", "1%"], "Old Atlanta houses often hide problems behind walls.", CH_MATH),
    ("Gross rent multiplier (GRM) equals", "Price divided by annual gross rent",
     ["Rent divided by price", "NOI divided by price", "Taxes divided by rent"], "Lower GRM usually means more "
     "income per dollar.", CH_MATH),
    ("Selling costs for a flip are often estimated at", "About 6-10% of the sale price",
     ["0%", "50%", "1%"], "Commissions, closing costs, concessions and transfer tax add up.", CH_MATH),
    ("Debt service coverage ratio (DSCR) is", "NOI divided by annual loan payments",
     ["Loan divided by price", "Rent divided by taxes", "Cash divided by repairs"], "Lenders often want 1.2 or "
     "higher.", CH_FIN),
    ("A hard money loan is typically", "Short-term, asset-based and more expensive than a bank loan",
     ["A 30-year fixed loan", "Free money from the city", "A tax credit"], "Used for flips and fast closings.",
     CH_FIN),
    ("The BRRRR method stands for", "Buy, Rehab, Rent, Refinance, Repeat",
     ["Bid, Redeem, Rent, Return, Repeat", "Build, Rent, Resell, Retire, Relax", "Buy, Rent, Repair, Refund, "
     "Redo"], "Refinancing pulls cash out to buy the next property.", CH_FIN),
    ("A Georgia nonjudicial foreclosure sale is advertised", "Like a sheriff's sale, on the first Tuesday at the "
     "courthouse", ["Online only", "Never", "In another state"], "O.C.G.A. 44-14-162.", CH_FIN),
    ("A lender must record its security deed or assignment", "Before the foreclosure sale",
     ["After the sale", "Never", "Only if the buyer asks"], "O.C.G.A. 44-14-162(b).", CH_FIN),
    ("A Georgia tenant who does not answer a dispossessory in time risks", "A default judgment for possession",
     ["Nothing", "Getting the house free", "A tax refund"], "O.C.G.A. 44-7-51(c).", CH_RENT),
    ("The Fair Housing Act forbids rental decisions based on", "Race, color, religion, sex, national origin, "
     "disability or familial status", ["Credit score", "Rental history", "Income verification"],
     "Screen every applicant with the same written criteria.", CH_RENT),
    ("A security deposit should be", "Held and returned under Georgia's security deposit rules with a move-in "
     "inspection list", ["Spent on repairs right away", "Never returned", "Optional to document"],
     "Document condition at move-in and move-out.", CH_RENT),
    ("Landlord-paid renovations on a pre-1978 rental that disturb paint require", "Lead-safe certified renovators",
     ["Nothing special", "Only a fresh coat of paint", "A pest inspection"], "EPA's RRP rule applies to rentals.",
     CH_RENT),
    ("Georgia's standard state homestead exemption is", "$2,000 off county and school taxes on a primary "
     "residence", ["$100,000 off all taxes", "Only for rentals", "Only for businesses"],
     "Counties like Fulton and DeKalb add bigger local exemptions.", CHAPTER),
    ("You can file for homestead exemption up to", "The county return deadline (April 1) or the end of the 45-day "
     "assessment appeal window", ["Any time ten years later", "Only in December", "Never"],
     "Georgia DOR homestead guidance.", CHAPTER),
    ("An investment property bought with a tax deed qualifies for homestead", "Only if you actually live in it as "
     "your residence on January 1", ["Always", "Never", "Only if vacant"], "Homestead is for owner-occupied "
     "primary residences.", CHAPTER),
    ("Property taxes on a flip you own on January 1 are", "Your responsibility and are prorated at closing",
     ["Paid by the city", "Waived for investors", "Paid by the tenant by law"], "Taxes follow the property.",
     CH_MATH),
]
