import pandas as pd

# Cleaned file load करा


# README content तयार करा
readme_content = f"""
# 📄 Data Cleaning Delivery Note

## 1. Scope of Work
- Provided dataset: Clean_data.xlsx
- Task: Cleaning and validating email addresses + extracting domains

---

## 2. Cleaning Performed
- Removed duplicates
- Trimmed spaces and special characters from emails
- Standardized all email addresses to lowercase
- Extracted domain part from each email
- Checked MX deliverability for domains

---

## 3. Assumptions & Guesswork
- No guesswork applied
  - If email/domain was invalid → marked as Invalid
  - If MX record not found → marked as Undeliverable
- Did not auto-correct typos (e.g., gmal.com → kept as is)

---



---

## 5. Output Files
- emails_cleaned.xlsx → Final cleaned dataset with validation status
"""

# README.txt फाईलमध्ये लिहा
with open("README.txt", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("✅ README.txt तयार झालं आहे.")
