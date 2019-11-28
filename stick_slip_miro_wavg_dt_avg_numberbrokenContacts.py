import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import random
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.datasets import make_classification
from sklearn.calibration import CalibratedClassifierCV, calibration_curve
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.tree import DecisionTreeClassifier


mdata=np.loadtxt("broken_contacts.txt")
data=mdata[:,1]
data1=data.reshape(-1,1)
#for i in range(0, 107999):
    #print("data", i, ":", data1[i,:])
wdata = np.loadtxt("Newwallinfo.txt")

arr=[]
s_arr=[]
th=0.002

##comparing the data
for i in range(0, 299999):
    #print("data", i, ":", data[i,1])
    d = wdata[i, 3]
         #print(d)
        
    if d <th: #defining stick
        #print('0')
   #     arr.append(0)
        s_arr.append(i)
    
    else: #defining slip
        #print('1')
     #   arr.append(1)
        s_arr.append(i)
s=np.array(s_arr)
print('s:',s)
#x=np.array(arr)
#print(x)

##finding the avarages of m(2n+1: n is the number of point which is taken for calculating the sum of the frames before and after 
## of the starting point of the slip events)elements. Then I found that which avarages(re_avg) are bigger than the thresold value and 
## appending them together and found the times frames corresponding to those avarages. Hence, I plotted the re_avg vs time frames

sum_arr=[]      #defining summation array
all_avg=[]      #defining all avarage array
re_avg=[]       #defining required avarage array
ti_frame=[]     #defining time frame of required avarage array
n=100           #for summing
m=2*n+1         #for avarage
for k in range(n,len(s)-n):                        #loop over the length of the array of indices
    for j in range(s[k]-n,s[k]+n):             #loop over the elements on which the avarage calculated
        sum_arr.append(wdata[j,3])               #combining the points for summation
    sum1=np.array(sum_arr)                       #making an array of the points for sum
    #print('len:',len(sum1))
    sum=np.sum(sum1)                             #finding sum
    #print('sum:',sum)
    avg=sum/m                                    #finding avarage
    sum_arr=[]                                   #making the summation array to be 0 not to include same elements twice
    #print(avg)
    all_avg.append(avg)                          #combing all the avarages
    avgarr=np.array(all_avg)                     #making array of all the avarages

#print('avgarr:',avgarr)                         #printing all avarages


time= s[n:len(s)-n]
plt.xlabel('time')
plt.ylabel('avg')
plt.plot(time,avgarr) #plotting avh v/s time
plt.title('Avarage greater than thresold v/s time')
#plt.show() 
print(len(avgarr))

all=[]
st=[]
sl=[]

inst=[]
insl=[]

##comparing top wall velocity with the thresold velocity obtained from the avg velocity graph for stick and slip phase
for i in range(0,len(avgarr)):
    if(avgarr[i]<0.002):
        #print('0')
        st.append(0)
        inst.append(i)
        all.append(0)
    else:
        #print('1')
        sl.append(1)
        insl.append(i)
        all.append(1)
stick=np.array(st)
slip=np.array(sl)
alls=np.array(all)
print(alls)
St_in=np.array(inst)
Sl_in=np.array(insl)

print(len(stick))
print(len(slip))
print('st:',len(St_in))
print('sl:',len(Sl_in))



#r_incom=np.concatenate([r_insl,Sl_in],axis=0)

#print('r_incom',r_incom)


#print('sl_in:',sl_in)

number_sl=int(round(0.8*len(Sl_in)))
number_st=int(round(0.8*len(St_in)))

r_slfirst=Sl_in[0:number_sl] #first 80% from slip
r_stfirst=St_in[0:number_st] #first 80% from stick

l_st=int(round(0.2*len(St_in)))
l_sl=int(round(0.2*len(Sl_in)))

r_instfirst=random.sample(list(r_stfirst),len(r_slfirst)) #same stick as slip

#r_incom=np.concatenate([r_insl,Sl_in],axis=0)
r_sllast=Sl_in[-l_sl:]
r_stlast=St_in[-l_st:]

r_instlast=random.sample(list(r_stlast),len(r_sllast)) #same stick as slip

r_first=np.concatenate([r_instfirst,r_slfirst],axis=0)

r_last=np.concatenate([r_instlast,r_sllast],axis=0)

f_train=[]
for i in range(0,len(r_first)):
    f_train.append(alls[r_first[i]])

Y_train=np.array(f_train)
f_test=[]
for i in range(0,len(r_last)):
    f_test.append(alls[r_last[i]])

Y_test=np.array(f_test)
r_xtrain=[]
for i in range(0,len(r_first)):
    r_xtrain.append(data1[r_first[i]])
       
X_train=np.array(r_xtrain)

r_xtest=[]
for i in range(0,len(r_last)):
    r_xtest.append(data1[r_last[i]])
       
X_test=np.array(r_xtest)
  
#X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20)

dt = DecisionTreeClassifier()
dt.fit(X_train, Y_train)  
#prediction=rfc.predict(X_test)
score = dt.score(X_test,Y_test)
print('dt_score:', score)
y_pred = dt.predict(X_test) 
#print(y_pred)
print('dt:',confusion_matrix(Y_test,y_pred))  
print(classification_report(Y_test,y_pred)) 