import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# Title and labels
ax.set_title("Square Numbers")
ax.set_xlabel("Values")
ax.set_ylabel("Square of Value")

# axis value ranges for x and y axis
ax.axis([0, 1100, 0, 1100000])

# bbox_incesh -> trims extra whitespaces around the pics
plt.savefig("square_scatterd_colormap.png", bbox_inches='tight')
