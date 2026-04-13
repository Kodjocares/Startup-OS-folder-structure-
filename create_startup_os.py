"""
Startup-OS Folder Structure Generator
Complete startup operating system folder structure.
Run: python3 create_startup_os.py
"""

import os

STRUCTURE = {
    "Startup-OS": {
        ".claude": {
            "System Prompts": ["Founder Prompts", "Investor Prompts", "Product Prompts", "Strategy Prompts", "Operations Prompts"],
            "Agents": ["Research Agent", "Pitch Agent", "Strategy Agent", "Hiring Agent", "Finance Agent"],
            "Workflows": ["Fundraising Workflow", "Hiring Workflow", "Product Launch Workflow", "Investor Update Workflow"],
            "Memory": ["Company Context", "Founder Bios", "Investor Profiles", "Market Context"],
            "MCP Configs": ["CRM Connections", "Finance Integrations", "Collaboration Tools"],
        },
        "Idea & Vision": {
            "Problem Statement": ["Problem Discovery", "Pain Point Research", "Root Cause Analysis", "Problem Validation"],
            "Vision & Mission": ["Vision Statement", "Mission Statement", "Core Values", "North Star", "10 Year Vision"],
            "Opportunity Mapping": ["Market Gaps", "Timing Analysis", "Why Now", "Unfair Advantage"],
            "Hypothesis": ["Core Assumptions", "Riskiest Assumptions", "Leap of Faith", "Validation Plan"],
            "Concept Development": ["Idea Iterations", "Concept Notes", "Brainstorm Sessions", "Pivots & Decisions"],
            "AI Workflows": ["Problem Framer", "Opportunity Scorer", "Vision Statement Builder"],
        },
        "Market Research": {
            "Market Sizing": ["TAM Analysis", "SAM Analysis", "SOM Analysis", "Sizing Models", "Market Maps"],
            "Target Market": ["Segment Analysis", "ICP Definition", "Early Adopters", "Beachhead Market", "Expansion Markets"],
            "Competitor Analysis": ["Direct Competitors", "Indirect Competitors", "Substitute Products", "Competitive Matrix", "Competitive Moat"],
            "Industry Research": ["Industry Reports", "Trend Analysis", "Regulatory Landscape", "Technology Shifts", "Market Drivers"],
            "Customer Research": ["Interview Notes", "Survey Results", "Behavioral Insights", "Jobs to Be Done", "Customer Quotes"],
            "Geographic Research": ["Finland Market", "West Africa Market", "EU Market", "Global Expansion"],
            "AI Workflows": ["Market Sizer", "Competitor Profiler", "Research Synthesizer"],
        },
        "Validation": {
            "Customer Discovery": ["Interview Scripts", "Interview Recordings", "Discovery Notes", "Pattern Analysis", "Key Insights"],
            "MVP Testing": ["Smoke Tests", "Landing Page Tests", "Concierge MVP", "Wizard of Oz", "Prototype Tests"],
            "Demand Validation": ["Waitlist Data", "Pre Sales", "LOIs", "Pilot Agreements", "Conversion Evidence"],
            "Problem Validation": ["Pain Evidence", "Frequency Data", "Willingness to Pay", "Current Solutions"],
            "Solution Validation": ["Solution Demos", "Feedback Sessions", "Usability Tests", "Iteration Log"],
            "AI Workflows": ["Interview Analyzer", "Assumption Tester", "Validation Report Writer"],
        },
        "Business Model": {
            "Business Model Canvas": ["Value Propositions", "Customer Segments", "Channels", "Customer Relationships", "Revenue Streams", "Key Resources", "Key Activities", "Key Partnerships", "Cost Structure"],
            "Revenue Model": ["Pricing Strategy", "Pricing Tiers", "Monetization Plan", "Revenue Experiments", "Pricing Benchmarks"],
            "Unit Economics": ["CAC Model", "LTV Model", "Payback Period", "Gross Margin", "Contribution Margin"],
            "Value Proposition": ["Value Prop Canvas", "Unique Differentiators", "Messaging", "Proof Points"],
            "Go To Market": ["GTM Strategy", "Launch Sequence", "Channel Strategy", "Sales Motion", "Partnership Strategy"],
            "AI Workflows": ["BMC Builder", "Pricing Strategist", "Unit Economics Calculator"],
        },
        "Product": {
            "Product Strategy": ["Product Vision", "Product Principles", "Product Bets", "Competitive Positioning"],
            "Roadmap": ["Now", "Next", "Later", "Icebox", "Roadmap Archive"],
            "MVP": ["MVP Scope", "MVP Design", "MVP Build", "MVP Metrics", "MVP Learnings"],
            "Features": ["Feature Backlog", "Feature Specs", "In Development", "Shipped Features", "Killed Features"],
            "Design": ["Wireframes", "UI Designs", "Prototypes", "Design System", "Brand Assets"],
            "User Research": ["User Interviews", "Usability Tests", "User Feedback", "Analytics Insights", "Feature Requests"],
            "Development": ["Tech Stack", "Architecture Docs", "Sprint Plans", "Bug Reports", "Release Notes"],
            "Analytics": ["Product Metrics", "Retention Data", "Feature Adoption", "Funnel Data", "A-B Tests"],
            "AI Workflows": ["PRD Generator", "Feature Prioritizer", "User Story Writer"],
        },
        "Fundraising": {
            "Fundraising Strategy": ["Funding Rounds Plan", "Use of Funds", "Funding Timeline", "Round Structure", "Dilution Planning"],
            "Pitch Materials": ["Pitch Decks", "One Pagers", "Executive Summary", "Demo Videos", "Pitch Deck Versions"],
            "Investor Pipeline": ["Target Investors", "Warm Intros", "Cold Outreach", "First Meetings", "Partner Meetings", "Term Sheet Stage", "Closed"],
            "Due Diligence": ["Data Room", "Financial Docs", "Legal Docs", "Technical Docs", "Team Docs", "Reference Checks"],
            "Term Sheets": ["Received Term Sheets", "Negotiation Notes", "Signed Term Sheets", "Declined Term Sheets"],
            "Cap Table": ["Current Cap Table", "Option Pool", "SAFE Notes", "Convertible Notes", "Pro Forma"],
            "Grants & Programs": ["Government Grants", "EU Funding", "Accelerator Programs", "Competitions", "Applications"],
            "Investor Relations": ["Investor Updates", "Board Meetings", "Board Decks", "Investor FAQs", "Communications Log"],
            "AI Workflows": ["Pitch Deck Builder", "Investor Researcher", "Investor Update Writer"],
        },
        "Finance": {
            "Financial Modeling": ["Revenue Models", "Expense Models", "Cash Flow Models", "Scenario Models", "Investor Models"],
            "Budgeting": ["Annual Budget", "Monthly Budget", "Department Budgets", "Budget vs Actuals", "Budget Reviews"],
            "Accounting": ["Chart of Accounts", "Invoices", "Receipts", "Payroll", "Monthly Close"],
            "Runway Management": ["Runway Calculator", "Burn Rate Tracker", "Cash Position", "Extension Plans", "Default Alive Model"],
            "Financial Reporting": ["P&L Statements", "Balance Sheets", "Cash Flow Statements", "Board Financial Reports"],
            "Tax & Compliance": ["Tax Returns", "VAT-GST", "R&D Tax Credits", "Compliance Calendar"],
            "Banking": ["Bank Accounts", "Transaction Records", "Credit Lines", "Multi Currency"],
            "AI Workflows": ["Runway Modeler", "Financial Forecast Builder", "Burn Rate Analyzer"],
        },
        "Legal": {
            "Company Formation": ["Incorporation Docs", "Articles of Association", "Shareholder Agreements", "Operating Agreements", "Registered Agents"],
            "IP & Trademarks": ["Trademark Filings", "Patent Applications", "Copyright Registrations", "IP Assignments", "Trade Secrets"],
            "Contracts": ["Customer Contracts", "Vendor Contracts", "Partner Agreements", "NDAs", "MoUs"],
            "Employment Law": ["Employment Contracts", "Contractor Agreements", "Equity Agreements", "IP Assignment Agreements", "Non Competes"],
            "Compliance": ["GDPR", "Data Privacy Policy", "Terms of Service", "Privacy Policy", "Cookie Policy"],
            "Regulatory": ["Licenses & Permits", "Regulatory Filings", "Industry Regulations", "Cross Border Compliance"],
            "AI Workflows": ["Contract Summarizer", "Compliance Checker", "Legal Risk Flagging"],
        },
        "Team & People": {
            "Founding Team": ["Founder Profiles", "Equity Split", "Roles & Responsibilities", "Founder Agreements", "Vesting Schedules"],
            "Hiring": ["Hiring Plan", "Job Descriptions", "Candidate Pipeline", "Interview Kits", "Offer Letters", "Hiring Decisions"],
            "Onboarding": ["Onboarding Plans", "Day 1 Checklists", "Tool Access", "Culture Docs", "90 Day Plans"],
            "Culture": ["Culture Deck", "Core Values", "Operating Principles", "Team Rituals", "Recognition Programs"],
            "Performance": ["OKRs", "Performance Reviews", "1-1 Templates", "Feedback Framework", "PIP Process"],
            "Advisors": ["Advisor Profiles", "Advisor Agreements", "Advisor Equity", "Engagement Plans", "Meeting Notes"],
            "Org Structure": ["Org Charts", "Team Structure", "Reporting Lines", "Future Org Design"],
            "AI Workflows": ["JD Generator", "Culture Doc Builder", "Hiring Scorecard Builder"],
        },
        "Operations": {
            "Company Handbook": ["Mission & Values", "Policies", "Benefits", "Work Guidelines", "Handbook Updates"],
            "SOPs": ["Core Processes", "Department SOPs", "Emergency Procedures", "Runbooks"],
            "Tools & Stack": ["Software Inventory", "Access Management", "Vendor List", "SaaS Subscriptions", "IT Setup Guides"],
            "Meetings": ["All Hands", "Team Standups", "Leadership Meetings", "Board Meetings", "Decisions Log"],
            "Project Management": ["Active Projects", "Project Templates", "Milestones", "Dependencies", "Completed Projects"],
            "Remote Operations": ["Remote Policy", "Async Guidelines", "Time Zone Management", "Virtual Offsites"],
            "AI Workflows": ["Meeting Summarizer", "SOP Generator", "Process Optimizer"],
        },
        "Go To Market": {
            "Launch Strategy": ["Pre Launch", "Launch Week", "Post Launch", "Launch Checklist", "Launch Retrospective"],
            "Positioning": ["Positioning Statement", "Messaging Framework", "Tagline Options", "Value Prop Testing"],
            "Sales Motion": ["Sales Playbook", "Sales Scripts", "Demo Flow", "Objection Handling", "Pricing Conversations"],
            "Early Customers": ["Design Partners", "Pilot Customers", "Logo Customers", "Case Studies", "Testimonials"],
            "Distribution": ["Channel Strategy", "Product Hunt", "Directories", "Communities", "Marketplaces"],
            "PR & Comms": ["Press Releases", "Media Kit", "Journalist Outreach", "Press Coverage", "Crisis Comms"],
            "AI Workflows": ["Launch Plan Builder", "Positioning Advisor", "Press Release Writer"],
        },
        "Customers": {
            "Customer Success": ["Onboarding Flows", "Success Plans", "QBR Templates", "Health Scores", "Expansion Plays"],
            "Support": ["Support Playbooks", "FAQ Library", "Ticket Templates", "Escalation Matrix", "Support Metrics"],
            "Feedback": ["Feature Requests", "Bug Reports", "NPS Data", "CSAT Scores", "Feedback Themes"],
            "Retention": ["Churn Analysis", "Save Plays", "Win Back Campaigns", "Retention Experiments"],
            "Referrals": ["Referral Program", "Advocate List", "Referral Tracking", "Incentive Structure"],
            "AI Workflows": ["Churn Predictor", "CS Playbook Builder", "Feedback Analyzer"],
        },
        "Growth & Marketing": {
            "Growth Strategy": ["AARRR Framework", "Growth Model", "North Star Metric", "Growth Experiments", "Growth Reviews"],
            "Content": ["Blog", "Social Media", "Video", "Newsletters", "Content Calendar"],
            "SEO": ["Keyword Research", "Content SEO", "Technical SEO", "Link Building"],
            "Paid Growth": ["Google Ads", "Meta Ads", "LinkedIn Ads", "Ad Creative"],
            "Community": ["Community Strategy", "Platform Setup", "Ambassador Program", "Engagement Tactics"],
            "AI Workflows": ["Growth Experiment Designer", "Content Generator", "Channel Optimizer"],
        },
        "Partnerships & Ecosystem": {
            "Strategic Partnerships": ["Partner Strategy", "Partner Pipeline", "Partner Agreements", "Partner Reviews"],
            "Accelerators & Incubators": ["Applications", "Active Programs", "Alumni Network", "Program Benefits"],
            "Ecosystem": ["Tech Partners", "Integration Partners", "Distribution Partners", "Community Partners"],
            "Mentors & Network": ["Mentor List", "Intro Requests", "Network Map", "Coffee Chats Log"],
            "AI Workflows": ["Partner Researcher", "Intro Email Writer", "Partnership Deal Builder"],
        },
        "Analytics & Metrics": {
            "North Star Metric": ["NSM Definition", "NSM Tracking", "Input Metrics", "NSM Reviews"],
            "Startup Metrics": ["MRR ARR", "Growth Rate", "Churn Rate", "NPS", "DAU MAU", "Activation Rate"],
            "Investor Metrics": ["Monthly Metrics", "Board Metrics", "Cohort Data", "Benchmark Comparisons"],
            "Dashboards": ["Founder Dashboard", "Investor Dashboard", "Product Dashboard", "Growth Dashboard"],
            "AI Workflows": ["Metrics Narrator", "Investor Update Builder", "Growth Diagnoser"],
        },
        "Knowledge & Learning": {
            "Founder Learning": ["Book Notes", "Course Notes", "Conference Notes", "Podcast Notes"],
            "Startup Playbooks": ["YC Playbooks", "a16z Resources", "First Round Resources", "Custom Playbooks"],
            "Lessons Learned": ["Monthly Reflections", "Failure Analysis", "Pivot History", "Decision Journal"],
            "Research Library": ["Market Research", "Competitor Research", "Technology Research", "Academic Papers"],
            "AI Workflows": ["Learning Summarizer", "Decision Journal Assistant", "Research Curator"],
        },
        "Archive": {
            "Old Pitch Decks": [],
            "Rejected Ideas": [],
            "Pivots History": [],
            "Closed Deals": [],
            "Past Experiments": [],
        },
    }
}


def create_structure(base_path, structure):
    for name, contents in structure.items():
        folder_path = os.path.join(base_path, name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"  ✓ {folder_path}")
        if isinstance(contents, dict):
            create_structure(folder_path, contents)
        elif isinstance(contents, list):
            for subfolder in contents:
                sub_path = os.path.join(folder_path, subfolder)
                os.makedirs(sub_path, exist_ok=True)
                print(f"      ✓ {sub_path}")
                with open(os.path.join(sub_path, ".gitkeep"), "w") as f:
                    pass


def count_folders(structure, count=0):
    for name, contents in structure.items():
        count += 1
        if isinstance(contents, dict):
            count = count_folders(contents, count)
        elif isinstance(contents, list):
            count += len(contents)
    return count


if __name__ == "__main__":
    base = os.getcwd()
    total = count_folders(STRUCTURE)

    print("\n🚀 Startup-OS Folder Generator")
    print(f"📍 Location: {base}")
    print(f"📁 Total folders to create: {total}")
    print("-" * 50)

    create_structure(base, STRUCTURE)

    print("-" * 50)
    print(f"\n✅ Done! {total} folders created.")
    print(f"📂 Open: {base}/Startup-OS\n")
