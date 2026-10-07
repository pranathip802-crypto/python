import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [10000, 15000, 12000, 18000]
customers = [100, 150, 120, 180]
fig, ax1 = plt.subplots() 
ax1.plot(months, sales) 
ax1.set_xlabel("Month") 
ax1.set_ylabel("Sales") 
ax2 = ax1.twinx() 
ax2.plot(months, customers) 
ax2.set_ylabel("Customers") 
plt.show()