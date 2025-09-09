import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests

# Google Sheets API setup (requires service account JSON file)
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS_FILE = "service_account.json"
SPREADSHEET_NAME = "CRM Sync Demo"

# CRM API (mock for demo)
CRM_API_URL = "https://jsonplaceholder.typicode.com/users"

def fetch_crm_data():
    try:
        response = requests.get(CRM_API_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching CRM data: {e}")
        return []

def write_to_sheets(data):
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open(SPREADSHEET_NAME).sheet1

    # Clear sheet before updating
    sheet.clear()
    sheet.append_row(["ID", "Name", "Email", "Phone"])

    for user in data:
        sheet.append_row([user["id"], user["name"], user["email"], user["phone"]])

if __name__ == "__main__":
    crm_data = fetch_crm_data()
    if crm_data:
        write_to_sheets(crm_data)
        print("✅ CRM data synced to Google Sheets")
