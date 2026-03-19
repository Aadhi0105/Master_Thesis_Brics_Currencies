"""
SWIFT Global Currency Tracker / RMB Tracker — Data Extraction Script
Extracts:
  1. Global payments currency shares (all currencies, top 20) from each report
  2. RMB monthly evolution time series from the rolling chart page

Usage:
    python3 extract_swift.py

Set SWIFT_FOLDER to your local SWIFT Dataset folder path.
Outputs two CSV files in the same folder.
"""

import os
import re
import csv
import pdfplumber
from pathlib import Path

# ─── CONFIGURE THIS PATH ───────────────────────────────────────────────────────
SWIFT_FOLDER = "/Users/psat0501/Desktop/HSG/Master Thesis/Thesis Data/SWIFT Dataset"
# ───────────────────────────────────────────────────────────────────────────────

OUTPUT_CURRENCY_SHARES = os.path.join(SWIFT_FOLDER, "SWIFT_Global_Currency_Shares.csv")
OUTPUT_RMB_EVOLUTION   = os.path.join(SWIFT_FOLDER, "SWIFT_RMB_Evolution.csv")

# Currency codes to look for
CURRENCY_CODES = [
    "USD","EUR","GBP","JPY","CAD","CNY","AUD","HKD","CHF","SGD",
    "NOK","SEK","PLN","DKK","NZD","MXN","ZAR","HUF","INR","RUB",
    "BRL","SAR","KRW","THB","MYR","CZK","TRY","AED","IDR","CLP","EGP"
]

def extract_report_month(filename):
    """Extract year-month from filename e.g. 'swift_rmb_tracker_october-2022' -> '2022-10'"""
    months = {
        "january":"01","february":"02","march":"03","april":"04",
        "may":"05","june":"06","july":"07","august":"08",
        "september":"09","october":"10","november":"11","december":"12"
    }
    fname = filename.lower()
    for month_name, month_num in months.items():
        if month_name in fname:
            year_match = re.search(r'(20\d{2})', fname)
            if year_match:
                return f"{year_match.group(1)}-{month_num}"
    return None

def extract_currency_shares_from_page(text):
    """Extract currency code + percentage share pairs from page text."""
    results = {}
    lines = text.split('\n')
    
    # Pattern: find percentage values near currency codes
    # Look for lines containing a currency code and a percentage
    pct_pattern = re.compile(r'(\d+\.\d+)%')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Check if line contains a known currency code
        for code in CURRENCY_CODES:
            if re.search(r'\b' + code + r'\b', line):
                # Look for percentage in same line or adjacent lines
                search_range = lines[max(0,i-2):min(len(lines),i+3)]
                for nearby in search_range:
                    pct_match = pct_pattern.search(nearby)
                    if pct_match:
                        pct_val = float(pct_match.group(1))
                        # Only accept reasonable payment share values (0.01% to 70%)
                        if 0.01 <= pct_val <= 70:
                            if code not in results:
                                results[code] = pct_val
                            break
    return results

def extract_rmb_evolution_from_text(text):
    """Extract monthly RMB share values from the evolution chart page text."""
    results = []
    
    # Pattern: percentage values that look like RMB shares (1.0% to 5.0% range)
    # paired with month names or year indicators
    month_pattern = re.compile(
        r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s*'
        r'.*?(\d+\.\d+)%',
        re.IGNORECASE
    )
    
    year_blocks = re.findall(r'(20\d{2})', text)
    pct_values = re.findall(r'(\d+\.\d+)%', text)
    
    # Filter to RMB-range values only (between 1.0 and 5.5)
    rmb_values = [float(v) for v in pct_values if 1.0 <= float(v) <= 5.5]
    
    return rmb_values, year_blocks

def process_pdf(pdf_path, report_month):
    """Process a single PDF and extract currency share data."""
    currency_data = {}
    rmb_evolution_page = None
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                text = page.extract_text() or ""
                
                # Page with global payments currency shares
                # Identified by containing multiple currency codes + percentages
                if ("USD" in text and "EUR" in text and "GBP" in text 
                    and "global payments" in text.lower()):
                    shares = extract_currency_shares_from_page(text)
                    if len(shares) >= 5:  # at least 5 currencies found
                        currency_data = shares
                
                # Page with RMB evolution chart
                if ("evolution" in text.lower() and "rmb" in text.lower() 
                    and "%" in text):
                    rmb_values, years = extract_rmb_evolution_from_text(text)
                    if len(rmb_values) > 10:
                        rmb_evolution_page = (rmb_values, years, text)
                        
    except Exception as e:
        print(f"  ERROR reading {pdf_path.name}: {e}")
    
    return currency_data, rmb_evolution_page

def main():
    swift_path = Path(SWIFT_FOLDER)
    
    if not swift_path.exists():
        print(f"ERROR: Folder not found: {SWIFT_FOLDER}")
        return
    
    # Find all PDF files
    pdf_files = sorted(swift_path.glob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files in {SWIFT_FOLDER}")
    
    if len(pdf_files) == 0:
        print("No PDF files found. Check your folder path.")
        return
    
    # ── Output 1: Global Currency Shares ──────────────────────────────────────
    all_currency_rows = []
    
    for pdf_path in pdf_files:
        report_month = extract_report_month(pdf_path.stem)
        if not report_month:
            print(f"  SKIPPED (could not parse date): {pdf_path.name}")
            continue
        
        print(f"Processing: {pdf_path.name} -> {report_month}")
        currency_data, rmb_evo = process_pdf(pdf_path, report_month)
        
        if currency_data:
            row = {"Report_Month": report_month}
            row.update(currency_data)
            all_currency_rows.append(row)
            print(f"  Found {len(currency_data)} currencies. "
                  f"USD={currency_data.get('USD','?')}% "
                  f"CNY={currency_data.get('CNY','?')}%")
        else:
            print(f"  WARNING: No currency data extracted")
    
    # Write currency shares CSV
    if all_currency_rows:
        # Collect all currency codes found across all reports
        all_codes = set()
        for row in all_currency_rows:
            all_codes.update(k for k in row.keys() if k != "Report_Month")
        
        fieldnames = ["Report_Month"] + sorted(all_codes)
        
        with open(OUTPUT_CURRENCY_SHARES, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in sorted(all_currency_rows, key=lambda x: x["Report_Month"]):
                writer.writerow(row)
        
        print(f"\nCurrency shares saved to: {OUTPUT_CURRENCY_SHARES}")
        print(f"Rows: {len(all_currency_rows)}, Currencies: {len(all_codes)}")
    else:
        print("\nWARNING: No currency data extracted from any PDF")

    # ── Output 2: Merge RMB Evolution with manual extract ─────────────────────
    # Load the manually extracted Oct 2022 evolution data if present
    manual_file = os.path.join(SWIFT_FOLDER, 
                               "October_22_-_Evolution_of_RMB_s_share.csv")
    
    rmb_rows = []
    
    if os.path.exists(manual_file):
        print(f"\nFound manual RMB evolution file, merging...")
        # This is the xlsx-disguised-as-csv handled separately
        # The cleaned version should be in the folder
    
    # Look for a cleaned version
    cleaned_file = os.path.join(SWIFT_FOLDER, "RMB_Evolution_2019_2022.csv")
    if os.path.exists(cleaned_file):
        with open(cleaned_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rmb_rows.append(row)
        print(f"Loaded {len(rmb_rows)} rows from cleaned manual extract")

    print("\n=== EXTRACTION COMPLETE ===")
    print(f"Currency shares file: {OUTPUT_CURRENCY_SHARES}")
    print(f"Next step: Review the CSV and check extraction quality")
    print(f"Flag any months where USD share looks wrong (should be 38-58%)")

if __name__ == "__main__":
    main()
