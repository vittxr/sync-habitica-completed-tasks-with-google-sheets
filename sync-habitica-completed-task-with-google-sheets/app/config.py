import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    APP_NAME = "sync-habitica-completed-tasks-with-google-sheets"
    GOOGLE_SHEETS_CREDENTIALS_PATH = "gsheets_creds.json"

    HABITICA_BASE_URL = "https://habitica.com/api/"
    HABITICA_API_KEY = os.getenv("HABITICA_API_KEY")
    HABITICA_USER_ID = os.getenv("HABITICA_USER_ID")

    GS_SPREADSHEET_ID = os.getenv("GS_SPREADSHEET_ID")
    GS_SPREADSHEET_DB_SHEET = "db"

    HABITICA_GSHEET_COLUMNS = [
        ("todo", "text"),
        ("notes", "notes"),
        ("tags", "tags"),
        ("checklist", "checklist"),
        ("steak", "streak"),
        ("repeat", "repeat"),
        ("priority", "priority"),
        ("startDate", "startDate"),
        ("created_at", "createdAt"),
        ("updated_at", "updatedAt"),
        ("date_completed", "dateCompleted"),
    ]


config = Config()
