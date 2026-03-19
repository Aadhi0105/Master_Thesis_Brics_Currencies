import os
import re
import csv
import pdfplumber
from pathlib import Path

SWIFT_FOLDER = "/Users/psat0501/Desktop/HSG/Master Thesis/Thesis Data/SWIFT Dataset"
OUTPUT_CURRENCY_SHARES = os.path.join(SWIFT_FOLDER, "SWIFT_Global_Currency_Shares.csv")

CURRENCY_CODES = [
    "USD","EUR","GBP","JPY","CAD","CNY","AUD","HKD","CHF","SGD",
    "NOK","SEK","PLN","DKK","NZD","MXN","ZAR","HUF","INR","RUB",
    "BRL","SAR","KRW","THB","MYR","CZK","TRY","AED","IDR","CLP","EGP"
]

MONTHS = {
    "january":"01","february":"02","march":"03","april":"04",
    "may":"05","june":"06","july":"07","august":"08",
    "september":"09","october":"10","november":"11","december":"12"
}

def extract_report_month(filename):
    fname = filename.lower()
    for month_name, month_num in MONTHS.items():
        if month_name in fname:
            year_match = re.search(r'(20\d{2})', fname)
            if year_match:
                return f"{year_match.group(1)}-{month_num}"
    return None

def extract_currency_shares(text):
    """Extract currency shares from the global payments page."""
    results = {}
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    for i, line in enumerate(lines):
        for code in CURRENCY_CODES:
            if re.search(r'\b' + code + r'\b', line):
                # Search surrounding lines for percentage
                search_lines = lines[max(0, i-3):min(len(lines), i+4)]
                for nearby in search_lines:
                    pct_match = re.search(r'(\d+\.\d+)%', nearby)
                    if pct_match:
                        val = float(pct_match.group(1))
                        if 0.01 <= val <= 70 and code not in results:
                            results[code] = val
                            break
    return results

def is_global_payments_page(text):
    """Check if this page contains the main currency share chart."""
    text_lower = text.lower()
    has_usd = 'usd' in text_lower
    has_eur = 'eur' in text_lower
    has_pct = '%' in text
    has_payments = 'payments' in text_lower
    has_global = 'global' in text_lower or 'international' in text_lower
    return has_usd and has_eur and has_pct and has_payments and has_global

def process_pdf(pdf_path):
    best_shares = {}
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text() or ""
                if is_global_payments_page(text):
                    shares = extract_currency_shares(text)
                    # Keep the extraction with the most currencies found
                    if len(shares) > len(best_shares):
                        best_shares = shares
    except Exception as e:
        print(f"  ERROR: {e}")
    return best_shares

# ── Main extraction ────────────────────────────────────────────────────────────
pdf_files = sorted(Path(SWIFT_FOLDER).glob("*.pdf"))
print(f"Found {len(pdf_files)} PDF files\n")

all_rows = []
failed = []

for pdf_path in pdf_files:
    report_month = extract_report_month(pdf_path.stem)
    if not report_month:
        print(f"SKIPPED (no date): {pdf_path.name}")
        continue
    
    print(f"Processing {report_month} — {pdf_path.name}")
    shares = process_pdf(pdf_path)
    
    if shares and 'USD' in shares:
        row = {"Report_Month": report_month}
        row.update(shares)
        all_rows.append(row)
        print(f"  OK — {len(shares)} currencies | USD={shares.get('USD','?')}% | CNY={shares.get('CNY','?')}%")
    else:
        failed.append(pdf_path.name)
        print(f"  WARNING — extraction failed or no USD found")

# Sort by date
all_rows.sort(key=lambda x: x["Report_Month"])

# Collect all currency codes
all_codes = set()
for row in all_rows:
    all_codes.update(k for k in row.keys() if k != "Report_Month")
fieldnames = ["Report_Month"] + sorted(all_codes)

# Write output
with open(OUTPUT_CURRENCY_SHARES, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in all_rows:
        writer.writerow(row)

print(f"\n{'='*60}")
print(f"EXTRACTION COMPLETE")
print(f"Rows extracted: {len(all_rows)}")
print(f"Date range: {all_rows[0]['Report_Month']} to {all_rows[-1]['Report_Month']}")
print(f"Currencies found: {sorted(all_codes)}")
print(f"Output: {OUTPUT_CURRENCY_SHARES}")
if failed:
    print(f"\nFailed files ({len(failed)}):")
    for f in failed:
        print(f"  - {f}")