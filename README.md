# Summary 

I developed this script because Habitica automatically deletes completed tasks after 30 days. Since I want to keep track of older completed tasks, this project lets you synchronize all completed tasks with Google Spreadsheet.

# Prerequisites

You need to obtain Google and Habitica credentials. See the ./_docs folder for instructions.

# How it works
 
1. Get the 2nd row of the Google Sheet to determine the last task’s completion date.
2. Use this completion date to filter Habitica tasks, so only newly completed tasks are appended to the Google Sheet.
3. If there are no tasks in the Google Sheet yet, all tasks will be appended.

# Setup cronjob

You can run this Python script manually using `python3 main.py` or `uv run python main.py`. Using UV is better because it uses the Python version installed inside the `.venv` folder, which is defined in the `.python-version` file.

However, configuring a cron job is a much better option. You can set it up on your own PC or on a VM, but in this case I chose to use GitHub Actions. You can follow the guide in `_docs/github_actions_cronjob.md`.

# Run manually 

Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

1. uv sync
2. uv run python main.py

# Limitations: 

Google Sheets has a limit of 20 million cells per spreadsheet ([source](https://workspaceupdates.googleblog.com/2026/09/doubled-cell-limits-in-google-sheets-now-generally-available.html)).

Since this script exports 11 columns per task, each task occupies 11 cells. This means you could export approximately **1.82 million tasks** before reaching the limit.

I won't handle this edge case. If you think it might be a problem, fork this project and implement your own solution.
 
# Refs

## Habitica

1. https://habitica.com/apidoc/
2. https://habitica.fandom.com/wiki/Guidance_for_Comrades#X-Client_Header
3. https://habitica.com/apidoc/#api-Task-GetUserTasks
