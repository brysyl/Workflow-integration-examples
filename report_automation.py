import os
import requests
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# 🌐 Mock API endpoint
API_URL = "https://jsonplaceholder.typicode.com/users"

# 📂 Output folder
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_data():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")
        return []

def save_csv(data):
    if not data:
        return
    df = pd.DataFrame(data)
    csv_path = os.path.join(OUTPUT_DIR, "report.csv")
    df.to_csv(csv_path, index=False)
    print(f"✅ CSV report saved: {csv_path}")

def save_pdf(data):
    if not data:
        return
    pdf_path = os.path.join(OUTPUT_DIR, "report.pdf")
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "Weekly Report")

    # Summary
    c.setFont("Helvetica", 12)
    c.drawString(50, 720, f"Total Records: {len(data)}")

    # Top 3 Users
    c.drawString(50, 700, "Top 3 Users:")
    y = 680
    for i, user in enumerate(data[:3], start=1):
        c.drawString(70, y, f"{i}. {user.get('name', 'N/A')}")
        y -= 20

    c.save()
    print(f"✅ PDF report saved: {pdf_path}")

if __name__ == "__main__":
    data = fetch_data()
    save_csv(data)
    save_pdf(data)
