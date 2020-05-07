import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x**3
z = x**2

# fig,axs = plt.subplot()
""" figure = plt.figure()

axes_cube = figure.add_axes([0.1,0.1,0.8,0.8])

axes_cube.plot(x,y,"o-b")
axes_cube.set_xlabel("X Axis")
axes_cube.set_ylabel("Y Axis")
axes_cube.set_title("Cube")

axes_squere = figure.add_axes([0.15,0.6,0.25,0.25])

axes_squere.plot(x,z,"o-r")
axes_squere.set_xlabel("X Axis")
axes_squere.set_ylabel("Y Axis")
axes_squere.set_title("Squere") """

""" figure = plt.figure()

axes = figure.add_axes([0,0,1,1])

axes.plot(x,z, label="Squere")
axes.plot(x,y, label="Cube")
axes.legend(loc=4)
 """

fig,axes = plt.subplots(nrows=2,ncols=1, figsize=(8,8))
axes[0].plot(x,y)
axes[0].set_title("Cube")

axes[1].plot(x,z)
axes[1].set_title("Squere")

plt.tight_layout()
fig.savefig("figure1.pdf")

plt.show()
