import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [1000, 1500, 1200, 1800, 2000]
plt.plot(months, revenue)
plt.title("Monthly Revenue") 
plt.xlabel("Month") 
plt.ylabel("Revenue")
plt.grid() 
plt.grid(axis="y")
plt.xlim(0, 10) 
plt.ylim(0, 100)
plt.xticks(rotation=45) 
plt.yticks([0, 20, 40, 60, 80, 100])
plt.show()