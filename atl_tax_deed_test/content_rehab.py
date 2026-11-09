"""Fixing up the property after the tax deed without picking up new code liens, fines or permit trouble."""

CHAPTER = "Rehab & Permits"
CH_CODE = "Avoiding Code Liens"
CH_TREE = "Trees, Historic & Lead"

CORE = [
    ("When is the right time to start a full renovation on a Georgia tax deed property?",
     ["The day after the sale", "After redemption is barred and you have legal possession (ideally after quiet "
      "title)", "During the first month", "Whenever the neighbors complain"], 1,
     "Before barment the owner can redeem and you would not be repaid for repairs. Possession comes after the "
     "right to redeem is foreclosed."),
    ("Who issues building permits for work inside the City of Atlanta?",
     ["Fulton County Tax Commissioner", "The City of Atlanta Department of City Planning, Office of Buildings",
      "The State Bar", "The water department"], 1,
     "The Office of Buildings issues permits, does inspections and enforces building codes."),
    ("What happens to a City of Atlanta building permit after about six months with no inspection activity?",
     ["Nothing", "It can expire, and the fees already paid are forfeited", "It doubles in value", "It turns into a "
      "certificate of occupancy"], 1,
     "The city warns that permits approaching six months of inactivity can expire; expired permits are invalid and "
     "paid fees are forfeited."),
    ("Your Atlanta permit expired 75 days ago. What now?",
     ["Ask for an extension", "Apply for a new permit - permits expired more than 60 days cannot be extended",
      "Keep working", "Pay a $5 fee"], 1,
     "Expired less than 60 days: written extension request. More than 60 days: a new permit application is "
     "required."),
    ("A permit application in Atlanta may affect trees. What must happen BEFORE you submit it (since June 25, 2025)?",
     ["Nothing", "A formal Arborist Meeting with the Office of Buildings arborist plan review staff",
      "Cut the trees first", "Ask the neighbors"], 1,
     "Ordinance 25-O-1341 requires an Arborist Meeting before submitting permits that may impact trees."),
    ("What must be on site for every City of Atlanta inspection?",
     ["Nothing", "The city-stamped approved plans", "The tax deed", "The previous owner"], 1,
     "DCP-stamped plans are required on-site for all inspections."),
    ("Your property is in an Atlanta historic or landmark district. What is the first step before exterior work?",
     ["Start work and apologize later", "Check the district on gis.atlantaga.gov/propinfo and get historic "
      "preservation review/approval", "Paint it any color", "Remove the porch"], 1,
     "Historic rules come from Chapter 20 of the City Code; the Urban Design Commission and HP staff review work."),
    ("You are flipping a house built in 1965 and your crew will sand painted trim. What rule applies?",
     ["None", "EPA/Georgia lead Renovation, Repair and Painting rules - use a lead-safe certified firm",
      "Only OSHA ladder rules", "The tree ordinance"], 1,
     "RRP applies to paid work disturbing paint in pre-1978 homes, including flippers. Georgia runs an "
     "EPA-authorized program."),
    ("A contractor you did not pay files a lien. How long did they have to file it?",
     ["7 days", "90 days after finishing work or supplying materials", "5 years", "They cannot file"], 1,
     "O.C.G.A. 44-14-361.1: claims of lien must be filed within 90 days. Get lien waivers with every payment."),
    ("What is the best way to stop NEW code violations while you wait to take possession or start work?",
     ["Ignore the house", "Keep grass cut, remove trash, secure doors and windows, and watch for posted notices",
      "Let people stay there", "Remove the address numbers"], 1,
     "Most new liens and fines come from overgrowth, open structures, junk and unpermitted work. Fix those first."),
]

CHAPTER_OF = {q[0]: CHAPTER for q in CORE}
for _q in CORE[4:8]:
    CHAPTER_OF[_q[0]] = CH_TREE
CHAPTER_OF[CORE[9][0]] = CH_CODE

FACTS = [
    ("City of Atlanta permits are applied for online through", "The Accela Citizen Access portal",
     ["Facebook", "The county tax office", "The Georgia DMV"], "aca-prod.accela.com/atlanta_ga.", CHAPTER),
    ("Atlanta inspection requests received before 3:00 p.m. are usually inspected within", "2 business days",
     ["2 hours", "2 months", "1 year"], "City of Atlanta inspections guidance.", CHAPTER),
    ("Work that does not need a permit still has to", "Meet the minimum requirements of the applicable code",
     ["Nothing", "Be done at night", "Be hidden from inspectors"], "City of Atlanta: exempt work must still meet "
     "code.", CHAPTER),
    ("A failed inspection means", "You must correct the work and get a re-inspection",
     ["The permit is finished", "You can cover the work", "The house is condemned"], "Non-compliance requires "
     "re-inspection.", CHAPTER),
    ("A certificate of occupancy is issued only after", "All required trade permits and field inspections pass",
     ["The first payment", "The tax sale", "The house is listed"], "Atlanta Office of Buildings.", CHAPTER),
    ("Electrical, plumbing and HVAC work usually need", "Their own trade permits and inspections",
     ["No permits", "Only a building permit", "A tree permit"], "Trade permits are separate from the building "
     "permit.", CHAPTER),
    ("Properties with an active Stop Work Order in Atlanta", "Cannot use the Express Permit process to fix it",
     ["Get express approval", "Are exempt from permits", "Can keep working"], "Since Dec 2, 2024, SWO fixes go "
     "through regular residential review.", CHAPTER),
    ("Notarized documents for an Atlanta permit application must be dated within", "30 days of submittal",
     ["1 year", "1 day", "There is no limit"], "City of Atlanta customer notice.", CHAPTER),
    ("Express permit applications in Atlanta are submitted", "In person at the Office of Buildings",
     ["By text message", "Only by mail", "At the tax office"], "In person, weekdays 8:15 a.m. to 3:30 p.m.",
     CHAPTER),
    ("When a homeowner permit is inspected for activity, who must be present", "The homeowner (or the licensed "
     "general contractor on contractor permits)", ["Nobody", "The neighbor", "The tax commissioner"],
     "Required party must be on site with approved plans.", CHAPTER),
    ("In Georgia, residential or general contractor work over $2,500 generally requires", "A state-licensed "
     "contractor", ["No license", "A business card", "A real estate license"],
     "Georgia State Licensing Board for Residential and General Contractors.", CHAPTER),
    ("Before paying a contractor in full you should get", "A signed lien waiver and passed inspections",
     ["Nothing", "A promise", "Their social security number"], "Protects you from mechanics' liens.", CH_CODE),
    ("A contractor's lien claim becomes unenforceable if no lien action is started within", "365 days of filing",
     ["30 days", "10 years", "It never expires"], "O.C.G.A. 44-14-367.", CH_CODE),
    ("A claim of lien is void if no notice of commencement of a lien action is filed within", "395 days",
     ["90 days", "5 years", "1 day"], "O.C.G.A. 44-14-367.", CH_CODE),
    ("The biggest cause of new code fines on vacant Atlanta houses is", "Overgrowth, trash, open or unsecured "
     "structures and unpermitted work", ["Paint color", "Mailbox style", "Owning too many houses"],
     "Keep it cut, clean, closed and permitted.", CH_CODE),
    ("To report or ask about Atlanta code and historic violations, DCP uses the", "CodeBusters email inbox",
     ["IRS", "Fire department only", "School board"], "codebusters@atlantaga.gov.", CH_CODE),
    ("Under Georgia's unsafe-building law the city can", "Order repair, closure or demolition and lien the costs",
     ["Only send a letter", "Buy your house for $1", "Do nothing"], "O.C.G.A. 41-2-9.", CH_CODE),
    ("A demolition lien for a city's costs continues", "Until it is paid", ["30 days", "1 year", "Until the next "
     "election"], "O.C.G.A. 41-2-9.", CH_CODE),
    ("After you buy, the first calls to make are to", "Utilities, the city about open code cases, and your insurer "
     "for a vacant-property policy", ["Nobody", "A moving company", "The DMV"],
     "Vacant homes need special insurance; open code cases must be resolved.", CH_CODE),
    ("A scope of work is", "A written list of every repair with quantities and costs",
     ["A permit", "A tax bill", "A lien"], "It keeps bids comparable and stops change-order surprises.", CHAPTER),
    ("When comparing contractor bids, make sure", "Each bid uses the same scope of work, license and insurance",
     ["You pick the cheapest no matter what", "Pay 100% upfront", "Skip references"],
     "Licensed, insured, same scope, paid on draws after inspections.", CHAPTER),
    ("Contractor payments should be made", "In draws tied to completed, inspected work",
     ["All up front", "In cash with no receipts", "Before any work"], "Never get ahead of the work.", CHAPTER),
    ("Atlanta's updated Tree Protection Ordinance took effect", "January 1, 2026",
     ["1990", "Never", "January 1, 2030"], "Adopted June 2025, effective January 1, 2026 (Chapter 158, Art. II).",
     CH_TREE),
    ("Under the 2026 tree ordinance, who must register with the city", "Businesses providing tree professional "
     "services, not private property owners", ["Every homeowner", "Nobody", "Only renters"],
     "Private property owners are not required to register.", CH_TREE),
    ("To find out if a property is in a historic district, use", "The city's Property Info map at "
     "gis.atlantaga.gov/propinfo", ["Zillow", "The tax bill only", "Guess from the age"],
     "City of Atlanta Historic Preservation.", CH_TREE),
    ("Historic preservation rules for Atlanta are found in", "Chapter 20 of the City Code",
     ["The federal tax code", "The DMV handbook", "There are none"], "City of Atlanta Historic Preservation.",
     CH_TREE),
    ("The board that reviews historic district work in Atlanta is the", "Urban Design Commission",
     ["Zoning Review Board only", "Water Board", "School Board"], "UDC and HP staff review historic work.",
     CH_TREE),
    ("Lead-safe RRP rules apply to homes built before", "1978", ["2000", "1950", "1990"],
     "Lead paint for homes was banned in 1978.", CH_TREE),
    ("RRP does NOT usually apply to", "A homeowner working on their own home they live in",
     ["A flipper", "A landlord", "A paid painter"], "Flippers and landlords are covered.", CH_TREE),
    ("Georgia's lead RRP program is run by", "The state under EPA authorization",
     ["Nobody", "The City of Atlanta water department", "The IRS"], "Georgia is an EPA-authorized state.",
     CH_TREE),
]
