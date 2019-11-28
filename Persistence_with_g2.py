import numpy as np
import matplotlib
from matplotlib import pyplot as plt

for i in range(2,3):
    file=open('PD/'+str(i)+'.txt','r')
    file2=file.read()
    file3=file2.replace('(0,','')
    file4=file3.replace('))','')
    file5=file4.replace(' (','')
    file6=file5.replace('[','')
    file7=file6.replace(']','')
    file8=file7.replace(' ','')
    file9=file8.replace('inf','0')
    data=file9.split(',')
    data1=np.asarray(data)
    birth=[]
    death=[]
    for j in range(0,72):
        birth.append(abs(float(data1[2*j])))
    birthh=np.array(birth)
    for k in range(1,73):
        death.append(abs(float(data1[2*k-1])))
    deathh=np.array(death)
    plt.figure()
    plt.plot(birthh,deathh,'bo',markersize=2)
    plt.plot(np.arange(0.0,255.0,0.5), np.arange(0.0,255.0,0.5),'r--')
    plt.axis('scaled')
    plt.axis([0, 150 , 0, 150])
    plt.xlabel('Birth')
    plt.ylabel('Death')
    plt.title('time'+str(i))
    plt.savefig('Persistence_image/' + str(i), dpi=800)
    plt.close()
    plt.show()
