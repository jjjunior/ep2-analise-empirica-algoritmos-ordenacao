import numpy as np
import matplotlib.pyplot as plt

x = np.array([10,20,40,80,160,320,640,1280,2560,5120])
radix = np.array([0.0001, 0.0, 0.0001, 0.0003, 0.0004, 0.0011, 0.0023, 0.0043, 0.0113, 0.0204])
quick = np.array([0.0, 0.0, 0.0001, 0.0002, 0.0005, 0.0013, 0.0024, 0.0062, 0.0122, 0.0264])

p1 = np.polyfit(x,radix,1)
p2 = np.polyfit(x,quick,1)

yfit=p1[0] * x + p1[1]
yresid= radix - yfit

SQresid = sum(pow(yresid,2))
SQtotal = len(radix) * np.var(radix)

R2 = 1 - SQresid/ SQtotal

print(p1)
print(p2)
print(R2)

plt.plot(x,radix,'o')
plt.plot(x,np.polyval(p1,x),'g--')

plt.plot(x,quick,'o')
plt.plot(x,np.polyval(p2,x),'b--')

plt.show()

