#!/usr/bin/python

import matplotlib.pyplot    as  plt 

#  taking cordinates

x2=[2,11,5,4,9,1]
x3=[3,10,6,4,7,8]

y2=[7,12,3,6,8,2]
y3=[7,2,2,23,4,5]

#  defining  x axis as  distance

plt.xlabel("DISTANCE")
plt.ylabel("TIME")
plt.title("calculating  DIstance and time factor")
plt.bar(x2,y2,label="rain")
plt.bar(x3,y3,label="rivers")
#  showing  label under  plot  option
plt.legend()
plt.grid(c='g')
plt.show()
