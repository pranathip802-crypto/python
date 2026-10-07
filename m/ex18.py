import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({    "Month": ["Jan", "Feb", "Mar", "Apr"],
                       "Sales": [10000, 15000, 12000, 18000] })
summary = df.groupby("Department")["Salary"].mean() 
plt.bar(summary.index, summary.values) 
plt.title("Average Salary by Department") 
plt.xlabel("Department") 
plt.ylabel("Average Salary") 
plt.show()