#!/usr/bin/python

import matplotlib.pyplot    as  plt 

#  taking cordinates

x=[2,5]
x1=[5,8]
x2=[2,11,5,4,9,1]
x3=[3,10,6,4,7,8]

y=[4,8]
y1=[3,9]
y2=[7,12,3,6,8,2]
y3=[7,2,2,23,4,5]

#  defining  x axis as  distance

plt.xlabel("DISTANCE")
plt.ylabel("TIME")
plt.title("calculating  DIstance and time factor")
#  plotting  x and y in terms of line 
plt.plot(x,y,label="road_track")
plt.plot(x1,y1,label="Train_track")
#  ploting  in terms of spoting 
plt.scatter(x2,y2,label="mines",color='red',marker='*',s=200)
plt.scatter(x3,y3,label="rocks",s=10)
#  showing the graph
#  showing  label under  plot  option
plt.legend()
plt.grid(c='g')
plt.show()
