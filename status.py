import dns.resolver
import pandas as pd

# तुझा dataset Excel मधून लोड कर
df = pd.read_excel("emails.xlsx")

def check_mx(domain):
    try:
        records = dns.resolver.resolve(domain, 'MX')
        return "Deliverable"
    except:
        return "Undeliverable"

df["Domain"] = df["Emails"].str.split("@").str[1]   # Email मधून domain काढ
df["DeliverabilityStatus"] = df["Domain"].apply(lambda x: check_mx(str(x)))

df.to_excel("emails_checked.xlsx", index=False)
print("✅ Result saved in emails_checked.xlsx")
