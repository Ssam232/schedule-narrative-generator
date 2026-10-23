# Schedule Narrative Generator

Drafts the monthly schedule progress report from Primavera P6 XER exports. The report can be edited on the page, then downloaded as a Word (.docx) file with its charts, copied into Word or an email, or saved as Markdown.

Live app: https://schedule-narrative-generator.streamlit.app

XER files are read by JavaScript in the visitor's own browser. They are never uploaded to the server, and no AI service is used: the report is written by built-in rules from the schedule data.

## What the report contains

1. **Executive summary**: progress to date (earned value and activity counts), milestones achieved, risks and issues.
2. **Schedule analysis**: forecast milestone dates, float trends across every version loaded (table and chart), delays and their likely causes, critical path changes, schedule risks.
3. **Critical path analysis**: the current critical path, the longest path, near-critical activities, float consumption, delayed activities, a recovery actions table and the first 10 float paths.
4. **Modification log**: every change since the previous update (new and deleted activities, logic, durations, costs, resources, constraints, calendars, names, actual dates), each with its previous value, new value and a blank for the explanation.
5. **Earned value management**: PV, EV, SV, SV% and SPI (SPI = EV ÷ PV, SV% = SV ÷ PV), an S-curve, SPI and SV% trend charts, a monthly forecast, and reporting by bridge, by work package and by element (foundations, piers, columns, girders, deck pours, MSE walls, soil nail walls, commissioning and handover).
6. **Target date risk analysis**: every target date rated high, medium or low from its float to the target, the float trend and its driving path. Moving the **Schedule risk analysis** slider adds a Monte Carlo simulation: the remaining work is rescheduled 1,000 times with every remaining duration varying across the chosen range (up to 25% shorter and 50% longer), giving P50, P80 and P90 dates, the chance of meeting each target date, a probability chart and the activities that drive the uncertainty.
7. **Schedule requirements compliance**: CPM, logic-driven, constraints, open ends and relationships, plus the DCMA 14-point assessment.
8. **Progress this period**, 9. **Look-ahead** and 10. **Basis of the report**.

Highlighted blanks mark the places that need the scheduler's input, such as causes, explanations and recovery actions.

## Inputs

- **Current update** (required), **previous update**, **baseline**, and any number of **earlier updates** for trends. Drop all the files at once and they are sorted by data date.
- Critical activities default to total float of 0 days or less and near-critical activities to 20 working days or less; both can be changed.
- Earned value uses budgeted cost when the baseline is cost loaded, otherwise budgeted labour hours, otherwise original durations.
- Bridge-level and work-package reporting use an activity code (for example "Structure" or "Work Package") when the schedule has one, otherwise WBS levels. Elements are matched by keywords in activity and WBS names, or by an activity code. All of these can be changed under **Report structure**.
- Target dates are the activities with deadline constraints (for example Finish On or Before), the headline milestone and the project Must Finish By date, or a list you choose.
- Float paths come from P6's multiple float path fields when the export has them; otherwise they are calculated from the activity dates and relationships.

A fictional sample bridge project (a baseline and seven monthly updates) loads on first visit so you can see the result.

## Files

- `streamlit_app.py`: serves the generator on Streamlit
- `index.html`: the generator itself (it also works when opened directly in a browser)
- `requirements.txt`: the Streamlit version the app was tested with
- `favicon.png`: browser tab icon

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository and upload these files to it.
2. Sign in at https://share.streamlit.io with GitHub and click **Create app**, then **Yup, I have an app**.
3. Choose the repository and branch, set the main file path to `streamlit_app.py`, optionally pick an app URL, and click **Deploy**.

An app deployed from a public repository can be opened by anyone with its link. From a private repository, use **Share > Make this app public** to share it.

## Updating

Replace `index.html` with a newer version and commit it. The app redeploys on its own.
