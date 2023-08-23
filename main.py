import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


data = np.genfromtxt('input_files/BOX_EVENT_SERIES.CSV', delimiter=',')

# generate mesh
# find limits
data[data[:, 4] == 1, :]
xmin = data[:, 2].min()
xmax = data[:, 2].max()
ymin = data[:, 3].min()
ymax = data[:, 3].max()
zmin = data[:, 4].min()
zmax = data[:, 4].max()

# create structured grid
dx = 20/1000 #mm
dy = 20/1000 #mm
dz = 5/1000 #mm

# nodes
xmax = xmax - xmin
xmin = 0
ymax = ymax - ymin
ymin = 0
zmax = zmax - zmin
zmin = 0

nx = int(xmax/dx) + 1
ny = int(ymax/dy) + 1
nz = int(zmax/dz) + 1

nodes = np.zeros((nx*ny*nz, 3))

for i in range(0, nz):
    for j in range(0, ny):
        for k in range(0, nx):
            nodes[i*ny*nx+j*nx+k,:] = (k*dx, j*dy, i*dz)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(nodes[:, 0], nodes[:, 1], nodes[:, 2],'.')
plt.show()







