import matplotlib.pyplot as plt
import numpy as np
#import math
import re

def get_info(info):
    string=info
    return re.split("\n",string)

def load_info(info,table):
    for i in range(0,len(info),1):
        table[info[i][0]].append(int(info[i][7]))
    #return table

k=28

BOLTZMANN_CONSTANT=1.380649*(10)**(-23)
m=800
T=270
vertical_shift=15000

#print(math.e, math.gamma(4))

report_cases=[]

with open("number_of_report_cases.txt",'r') as f_obj:
    text=f_obj.read()
    result=get_info(text)
    report_cases=np.array([int(i) for i in result][::-1])


x=np.arange(202,561,1) # contest number
#print(report_cases)
#y=(180000)*((x-202)**((k/2)-1)*math.e**(-0.8*(x-202)/2)) / (2**(k/2)*math.gamma(k/2))+20000
#chi-square
#max 361908
y_b=10**(-31.6875)*((m/(2*np.pi*BOLTZMANN_CONSTANT*T))**(3/2)) * (4*np.pi*((x-192.5)**2)*np.e**(-(m*(x-192.5)) / (2*k*T))) + vertical_shift
#best -31.6875, shift 20000, m=800, T=270, horizontal-192.5
y2=10000000/(x-202)-9500
y3=361908*np.e**(0.015*(228-x))-6000
y_final=list(y_b[0:266-202])+list(y3[266-203:338-202])+list(y2[338-202+1:])
#y4=0.53*y2+0.47*y3
#y5=y4+y
#36190800

plt.figure()
#plt.plot(x,y)
plt.plot(x,report_cases)
#plt.plot(x,y2)
#plt.plot(x,y3)
#plt.plot(x,y4)
#plt.plot(x,y_b)
plt.plot(x,y_final)
#plt.plot(x,y5)
plt.xlim(202,560)
plt.ylim(0,370000)
plt.show()

