import pandas as pd

# Load scheme performance data
funds = pd.read_csv("data/processed/scheme_performance_clean.csv")

# Get user input
risk = input("Enter Risk Appetite (Low / Moderate / High): ").strip().capitalize()

# Filter by risk grade
recommended = funds[funds["risk_grade"].str.capitalize() == risk]

# If no matching funds
if recommended.empty:
    print("\nNo funds found for this risk level.")
else:
    # Sort by Sharpe Ratio
    recommended = recommended.sort_values("sharpe_ratio", ascending=False)

    print("\nTop 3 Recommended Funds\n")
    print(
        recommended[
            ["scheme_name", "fund_house", "risk_grade", "sharpe_ratio"]
        ].head(3)
    )