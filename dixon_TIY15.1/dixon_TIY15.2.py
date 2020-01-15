import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,s=10)

ax.set_title("Cubic Numbers (1-5000)", fontsize=24, c=(0.7, 0.7, 0))
ax.set_xlabel("Value", fontsize=14, c=(0.7, 0.7, 0))
ax.set_ylabel("Cube of the Value", fontsize=14, c=(0.7, 0.7, 0))

ax.tick_params(axis='both', which='major', labelsize=15)
ax.axis([0, 5000, 0, 125000000000])

plt.show()
