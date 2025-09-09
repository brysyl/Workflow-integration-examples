# Google Sheets + CRM Sync

This project demonstrates how to sync data from a CRM API into **Google Sheets** automatically.

## 🚀 Features
- Connects to a CRM API (mocked with JSONPlaceholder).
- Fetches user/client data.
- Updates a Google Sheet with the latest info.
- Clears old data before updating.

## 🛠️ Tech Stack
- Python 3.9+
- gspread (Google Sheets API)
- requests

## 📦 Setup
1. Enable Google Sheets API & create a service account JSON key.
2. Share your Google Sheet with the service account email.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python crm_to_sheets.py
   ```

---
