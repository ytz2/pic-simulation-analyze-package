#! /usr/bin/env python
import numpy as np
from pylab import *


ne=1
ni=1
no=6

#zz=150
x_range=[1000,1001]
z_range=[100,101]

evx=np.random.normal(0., 0.001, ne)
ex=np.linspace(x_range[0],x_range[1],ne)
ey=np.zeros(ne)
ez=np.linspace(z_range[0],z_range[1],ne)
#ez[:]=zz
evy=np.random.normal(0., 0.001, ne)
evz=np.random.normal(0., 0.01, ne)

ivx=np.random.normal(0., 0.001, ni)
ivy=np.random.normal(0., 0.001, ni)
ivz=np.random.normal(0., 0.01, ni)
ix=np.linspace(x_range[0],x_range[1],ni)
iy=np.zeros(ni)
iz=np.linspace(z_range[0],z_range[1],ni)
#iz[:]=zz

#ovx=np.random.normal(0., 0.001, no)
#ovy=np.random.normal(0., 0.001, no)
#ovz=np.random.normal(0, 0.01, no)
#ox=np.linspace(x_range[0],x_range[1],no)
#oy=np.zeros(no)
#oz=np.linspace(z_range[0],z_range[1],no)
#oz[:]=zz

ovx=np.array([0.,0.,0.,0.,0.,0.])
ovy=np.array([0.,0.,0.,0.,0.,0.])
ovz=np.array([-0.02,0.015,-0.015,0.02,-0.015,0.02])
ox=np.array([800,800,1000,1000,1200,1200])
oy=np.zeros(6)
oz=np.array([200,-200,200,-200,200,-200])

f=open("initialization.txt",'w')
for i in xrange(ne):
    for item in [ex[i],ey[i],ez[i],evx[i],evy[i],evz[i]]:
        f.write("%s " % item)
    f.write("\n")

for i in xrange(ni):
    for item in [ix[i],iy[i],iz[i],ivx[i],ivy[i],ivz[i]]:
        f.write("%s " % item)
    f.write("\n")
        
for i in xrange(no):
    for item in [ox[i],oy[i],oz[i],ovx[i],ovy[i],ovz[i]]:
        f.write("%s " % item)
    f.write("\n")

f.close()
