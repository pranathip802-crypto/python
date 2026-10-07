import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.DataFrame({    "Month": ["Jan", "Feb", "Mar", "Apr"],
                       "Sales": [10000, 15000, 12000, 18000] })
plt.plot(df["Month"], df["Sales"])
plt.title("Monthly Sales")
plt.xlabel("Month") 
plt.ylabel("Sales") 
plt.show()

summary = df.groupby("Department")["Salary"].mean() 
plt.bar(summary.index, summary.values) 
plt.title("Average Salary by Department") 
plt.xlabel("Department") 
plt.ylabel("Average Salary") 
plt.show()
