# print(mlt.__version__)
import numpy as np
import matplotlib.pyplot as plt

# ypoints = np.array([0,6,8,5,3])
# ypoints = np.array([])

# plt.plot(ypoints , "o:r")
# plt.show()
# plot()function is used to draw points in a diagram.
# By default the plot function draws a line from point to point.
# parameter 1 is an array contaning the points on the x-axis.
# parameter 2 is an array contaning the points on the y-axis.

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

# plt.plot(xpoints,ypoints ,'o:g', ms=20, mec='r', mfc ='r')
# plt.show()
# you can use the keyword argumment marker to emphasize each point with a specific marker.
# font1 ={
#         'family':'serif',
#         'color' :'blue',
#         'size' : 20
# }
# font2 ={
#         'family':'serif',
#         'color' :'darkred',
#         'size' : 15
# }


# plt.plot(x,y,marker='o')
# plt.title("Sports Watch data", fontdict=font1, loc='left')
# plt.xlabel("Average pulse", fontdict=font2)
# plt.ylabel("Calories Burnage",fontdict=font2)
# plt.grid(axis='y')
# plt.scatter(x,y)
# plt.show()
