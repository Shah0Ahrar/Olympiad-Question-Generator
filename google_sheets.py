
import gspread
from google.oauth2.service_account import Credentials

CREDENTIALS_FILE = "google_credentials.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
client = gspread.authorize(creds)
SHEET_NAME = "Olympiad_Questions_Ratings"
spreadsheet = client.open(SHEET_NAME).sheet1

def save_rating(question, rating):
    spreadsheet.append_row([question, rating])
    print("✅ Rating saved successfully!")
