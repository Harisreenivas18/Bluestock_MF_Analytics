import pandas as pd
import numpy as np

# Load NAV history
nav = pd.read_csv("data/processed/nav_history_clean.csv")

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Sort values
nav = nav.sort_values(["amfi_code", "date"])

# Daily Returns
nav["daily_return"] = nav.groupby("amfi_code")["nav"].pct_change()

print(nav.head())

# Save updated file
nav.to_csv("data/processed/nav_history_clean.csv", index=False)

print("Daily returns computed successfully.")