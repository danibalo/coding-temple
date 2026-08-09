import pandas as pd
import matplotlib.pyplot as plt
messy = pd.DataFrame({
    "product": ["Widget A", "Widget B", "widget a", "Widget C","Widget B", "widget A", " widget C", "Widget D", None, "Widget A"],
    "sales": ["150", "200", "175", "300", "200", "180", "250", "abc", "100", "-50"],
    "date": ["2025-01-01", "2025-01-01", "2025-01-02", "2025-01-02", "2025-01-03", "2025-01-03", "2025-01-04", "2025-01-04", "2025-01-05", "2025-01-05"],
     "region": ["North", "South", "north", "East", "South","West", "east", "North", "South", "West"],

})
# print(f"Raw data: \n{messy}")
# print(f"Missing values: \n{messy.isnull().sum()}")
messy["product"] = messy["product"].str.strip().str.title()
messy["region"] = messy["region"].str.strip().str.title()
messy["date"] = pd.to_datetime(messy["date"], errors="coerce")
messy["sales"] = pd.to_numeric(messy["sales"], errors="coerce")
messy.loc[messy["sales"] <=0, "sales"] = pd.NA
# print(f"Missing values After cleaning: \n{messy.isnull().sum()}")
# print(messy)
sales_by_product = messy.groupby("product")["sales"].sum()
#print(sales_by_product)
sales_by_product = messy.groupby("product")["sales"].sum()
#print(sales_by_date)
sales_by_date = messy.groupby("date")["sales"].sum()
#Analyze and visualize
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].bar(sales_by_product.index, sales_by_product.values, color="steelblue")
axes[0].set_title("Total Sales by product")
axes[0].set_ylabel("total sales")
axes[0].set_xlabel("product")
axes[0].tick_params(axis="x", rotation=45)
axes[1].plot(sales_by_date.index, sales_by_date.values, color="orange", marker="o")
axes[1].tick_params(axis="x", rotation=45)
axes[1].set_title("Sales by date")
axes[1].set_ylabel("total sales")
axes[1].set_xlabel("dates")
axes[1].grid(True)
axes[2].hist(
    messy["sales"].dropna(),
    bins=5,
    color="green",
    edgecolor="black"

)
axes[2].set_title("Sales Distribution")
axes[2].set_xlabel("Sales")
axes[2].set_ylabel("Frequency")
plt.tight_layout()
plt.savefig("sales analysis")
plt.show()

