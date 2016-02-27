import numpy
from numpy import array
import string
import math
def dealline(rdlin,sepin):
    rdlsplit=rdlin.split(sepin)
    x0=string.atof(rdlsplit[1])
    y0=string.atof(rdlsplit[2])
    x1=string.atof(rdlsplit[3])
    y1=string.atof(rdlsplit[4])
    return x0,y0,x1,y1

f=open(r"bz2000b.txt","r")
rdl=f.readline()
x0,y0,x1,y1=dealline(rdl,"\t")
B=array([[1,0,x0,-1*y0],\
         [0,1,y0,x0]])
L=array([[x1],\
         [y1]])
rdl=f.readline()
while(rdl):
    x0,y0,x1,y1=dealline(rdl,"\t")
    b=array([[1,0,x0,-1*y0],\
         [0,1,y0,x0]])
    l=array([[x1],\
         [y1]])
    B=numpy.vstack((B,b))
    L=numpy.vstack((L,l))
    rdl=f.readline()
f.close()
BB=numpy.matrix(B)
LL=numpy.matrix(L)
print (BB.T*BB).I*(BB.T*LL)
XX=(BB.T*BB).I*(BB.T*LL)
DX=XX[0,0]
DY=XX[1,0]
KC=XX[2,0]
KS=XX[3,0]
K=(KC**2+KS**2)**0.5
rad=math.atan(KS/KC)
dd=rad/math.pi*180.*60.*60.0
print("DX:{0}\nDY:{1}\nK:{2}\nDegree:{3}".format(DX,DY,K,dd))
print BB*XX-LL
