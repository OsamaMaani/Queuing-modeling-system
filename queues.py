# Queueing Modeling System 
import numpy as np
import matplotlib.pyplot as plt

arrivalRate = 10; serviceRate = 4; numOfCus = 40; counter =0; counterT=0; helper =0.0; time =0.0
arrAn = []; arrSn=[]; arrWaiting =[]; arrHelper=[]; arrHelperT=[]; arrCusQ=[]
#STEP 1
#Generating some random values for lambda and mu.
arrA = np.random.poisson(arrivalRate,numOfCus)
arrS =  np.random.exponential(serviceRate,numOfCus)
#STEP 2
#Generating the time for each customer 
#and the time for the service according to his/her lambda & mu. 
for i in range(40):
  arrAn.append( float(1)/float(arrA[i]))
  arrSn.append(float(1)/float(arrS[i]))
  arrHelperT.append(0.0)
#STEP 3
#Creating an array arrHelper that will store the starting point for every customer
for i in range(40):
    counter+=arrAn[i]
    arrHelper.append(counter)
#STEP 4    
#Creating an array arrHelperT to have items
#representing the final time that the customer leaves at.
for i in range(40):
    if i== 0 :
        arrHelperT[0] = arrHelper[0]+arrSn[0] 
    else :     
        if arrHelperT[i-1]>arrHelper[i]:
            arrHelperT[i]=arrSn[i]+arrHelperT[i-1]
        else :
            arrHelperT[i] = arrHelper[i]+arrSn[i]   
#STEP 5              
#Creating an array that each element of it represents the time each customer 
# will have to wait in the queue.
for i in range(40): 
    time = arrHelperT[i]-(arrHelper[i]+arrSn[i])
    print(time)
    if time < 0:
        arrWaiting.append(0)
    else :
        arrWaiting.append(time)
print(arrWaiting)        
#STEP 6
#Creating an array to represent the number of customers of the queue 
# at every point
for i in range(40):
    for j in range(i+1,40):
        if arrHelperT[i]>arrHelper[j] :
           helper+=1
    arrCusQ.append(helper)
    helper =0                 
#Graphing some relations
plt.figure(1)
plt.plot(arrCusQ)
plt.xlabel("Number of customers at the queue at each point")
plt.figure(2)
plt.plot(arrWaiting)
plt.xlabel("The time waited by each customer")
plt.figure(3)
plt.plot(arrHelper)
plt.xlabel("The time at which each customer comes")
plt.show()
