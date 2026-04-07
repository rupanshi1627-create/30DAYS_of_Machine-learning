#c)  Perform TWO complete iterations of Batch Gradient Descent. 
# Show the updated weights after each iteration.
#we have given 2 initial--weights w₀ = 2.0, w₁ = 0.1 and learning rate η = 0.01.

#FLOW --Predict>error>square error>derivative>new weights update>repeat
#below code

import numpy as np #to handle number and arrays

 #define data--given in question
x = np.array([22,25,28,30,33])
y = np.array([3.1,4.0,5.2,6.5,7.8])

#initial values
w0=2.0
w1=0.1
lr=0.01  #step size
n=len(x) #total data points

#loop (iterations)
for i in range(2):#why 2?--bcz it is in question that 2 iterations
    y_pred = w0 + w1 * x
    #Error
    error=y - y_pred

    #cost function
    cf=(y_pred-y)**2
    
    #Derivative
    dw0 = np.sum(error) / n
    dw1 = np.sum((error) * x) / n
    
    #Updated weights
    w0 = w0 - lr * dw0
    w1 = w1 - lr * dw1
    
    #print iteration for what is happening after each oteration
    print(f"Iteration {i+1}: w0={w0}, w1={w1}")



