import matplotlib.pyplot as plt
class_a = [85, 90, 78, 92, 88]
class_b = [80, 85, 75, 90, 85]
plt.hist(class_a, bins=5, alpha=0.5, label="Class A") 
plt.hist(class_b, bins=5, alpha=0.5, label="Class B") 
plt.legend() 
plt.show()