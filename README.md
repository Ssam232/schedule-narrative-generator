# Schedule Narrative Generator

Drafts a schedule update narrative from Primavera P6 XER exports: executive summary, progress this period, critical path, float, milestones and variance, change in forecast completion, schedule changes, DCMA 14-point checks, a look-ahead and an issues table. The narrative can be edited on the page, then downloaded as a Word (.docx) or Markdown file.

Live app: https://schedule-narrative-generator.streamlit.app

XER files are read by JavaScript in the visitor's own browser. They are never uploaded to the server.

## Writing with your company's Microsoft Copilot (optional)

By default the narrative is written by built-in rules, and no AI is involved. If your company gives you Microsoft Copilot, you can have Copilot polish the wording, explain causes from your own notes, and fill in the highlighted blanks. The app checks Copilot's answer before using any of it: every number, date and activity ID must match the schedule, and words like *later* and *earlier* must not be swapped. A paragraph that fails the check keeps its original wording.

### How to use it

1. **Open your work Copilot.** Go to [copilot.cloud.microsoft](https://copilot.cloud.microsoft), or open Copilot in Teams, Outlook or Edge, and sign in with your work email.
2. **Check that it's protected.** Look for the shield icon at the top of the chat. Hovering over it should say enterprise data protection applies. If there's no shield, or you're signed in with a personal account, don't paste schedule data. Not sure project data is allowed in Copilot? Ask your manager or IT once.
3. **Set it up in the app.** Under **AI writing**, choose **Microsoft Copilot**. Pick what to rewrite (the executive summary or the whole narrative) and the tone, and type any notes, such as causes of delay, weather or recovery actions.
4. **Send the prompt.** Click **Copy prompt**, click in Copilot's message box, paste (Ctrl+V, or ⌘V on a Mac) and press Enter. A long narrative is split into parts; send each one and wait for its answer.
5. **Bring the answer back.** Click the copy button under Copilot's answer, paste it into step 3 in the app and click **Check and apply**. Paragraphs that pass are highlighted.
6. **Review, then download.** Read the highlighted paragraphs, use **Revert** on any you don't like, then download the Word file as usual.

If Copilot says the message is too long, choose **Executive summary**, or send the parts one at a time. For a different version, ask Copilot to try again and paste the new answer.

### What goes where

- The app itself still sends nothing anywhere. You copy the prompt and paste it into Copilot yourself, and you can see exactly what's in it under **See exactly what's sent**.
- The prompt contains the narrative text, including project and activity names, dates and your notes. With a work account and the shield showing, Copilot handles it under your company's agreement with Microsoft, and it isn't used to train Microsoft's models.
- Your notes aren't saved by the app.

### Why copy and paste instead of a direct connection

Microsoft's API for calling Copilot from other apps is still in preview. It needs a paid Microsoft 365 Copilot add-on licence for every user, and it needs the company's IT team to register the app and approve its access to each user's mail, chats and files. Copy and paste works with the Copilot Chat that's included with most Microsoft 365 work accounts, without any IT setup.

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
