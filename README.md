# Schedule Narrative Generator

Drafts a schedule update narrative from Primavera P6 XER exports: executive summary, progress this period, critical path, float, milestones and variance, change in forecast completion, schedule changes, DCMA 14-point checks, a look-ahead and an issues table. The narrative can be edited on the page, then downloaded as a Word (.docx) or Markdown file.

Live app: https://schedule-narrative-generator.streamlit.app

XER files are read by JavaScript in the visitor's own browser. They are never uploaded to the server, and no AI service is used: the narrative is written by built-in rules from the schedule data.

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
