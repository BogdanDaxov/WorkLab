import RPi.GPIO as a
import time as b
def binar(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]
def adc(k):
    a.output(dac,binar(k))
    return(k)
a.setmode(a.BCM)
dac =[8,11,7,1,0,5,12,6]
led =[2,3,4,17,27,22,10,9]
comp=14
tri=13
a.setup(led,a.OUT)
a.setup(dac ,a.OUT)
a.setup(tri,a.OUT,initial=a.HIGH)
a.setup(comp,a.IN)
try:
    while (True):
        r=0
        c=0
        for i in range(0,8):
            f=adc(r+2**(7-i))
            b.sleep(0.0006)
            if a.input(comp)==0:
                r=r+2**(7-i)
            else:
                r=r
        print(binar(r),"V=",r/255*3.3)
        a.output(led,binar(r))
finally:
    a.output(dac,0)
    a.cleanup(dac)
    a.output(tri,0)
    a.cleanup(tri)
    a.output(led,0)
    a.cleanup(led)