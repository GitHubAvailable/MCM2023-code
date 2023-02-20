import matplotlib.pyplot as plt
import numpy as np
import re

def get_info(info):
    string=info
    return re.split("\n",string)

k=28

BOLTZMANN_CONSTANT=1.380649*(10)**(-23)
m=350
T=110
vertical_shift=1900


report_hard_mode=[]

with open("number_of_hard_mode.txt",'r') as f_obj:
    text=f_obj.read()
    result=get_info(text)
    report_hard_mode=np.array([int(i) for i in result][::-1])


x=np.arange(202,561,1) # contest number

y_b=10**(-33.085)*((m/(2*np.pi*BOLTZMANN_CONSTANT*T))**(3/2)) * (4*np.pi*((x-202)**2)*np.e**(-(m*(x-202)) / (2*k*T))) + vertical_shift
y2=610000/(x-190)+600
y3=14510*np.e**(0.01*(233-x))
y_final=list(y_b[0:260-202])+list(y3[260-202:360-202])+list(y2[360-202:])


plt.figure()
plt.plot(x,report_hard_mode)
plt.plot(x,y_final)

plt.xlim(202,560)
plt.ylim(0,16000)
plt.show()

