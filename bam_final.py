import numpy as np
print("We take two inputs patters, A and C")
print("\n")
input1=np.array([-1,1,-1,1,-1,1,1,1,1,1,-1,1,1,-1,1]).reshape(15,1)#coverting our 5*3 pattern into 15*1 for mathematical ease 
input2=np.array([-1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1]).reshape(15,1)
input3=np.array([-1,1,-1,1,1,1,-1,1,1,1,-1,-1,1,-1,1]).reshape(15,1)#coverting our 5*3 pattern into 15*1 for mathematical ease 
input4=np.array([1,-1,1,1,-1,-1,1,-1,1,1,-1,-1,1,-1,-1]).reshape(15,1)
output1=np.array([-1,1,1]).reshape(1,3)
output4=np.array([-1,1,-1]).reshape(1,3)
output2=np.array([1,1,-1]).reshape(1,3)
output3=np.array([1,-1,1]).reshape(1,3)
print("The input for pattern A is")
print(input1)
print("\n")
print("The target for pattern A is")
print(output1)
print("\n")
print("The input for pattern C is")
print(input2)
print("\n")
print("The target for pattern C is")
print(output2)
print("\n")
print("\n")
print("\n")
inp_final=np.concatenate((input1,input2,input3,input4),axis=1)
out_final=np.concatenate((output1,output2,output3,output4),axis=0)
print("the initial weight for pattern A is:")
print(np.dot(input1,output1))
print("\n")
print("\n")
print("the initial weight for pattern C is:")
print(np.dot(input2,output2))
print("\n")
print("\n")
print("the final weights for pattern A and C is:")
weight=np.dot(inp_final,out_final)
print(weight)
print("\n")
print("\n")
print("\n")
print("\n")
print("Now for the testing phase\nWe multiply the input pattern with the weight matrix calculated above")
print("\nTesting for input pattern A\n")
print(input1.T,"*",weight)
y=np.dot(input1.T,weight)
y[y<0]=-1
y[y>=0]=1
print("y=",y)
print("\n")
print("\nTesting for input pattern C\n")
print(input2.T,"*",weight)
y=np.dot(input2.T,weight)
y[y<0]=-1
y[y>=0]=1
print("y=",y)
print("Since testing input for pattern A and C gives correct target values, testing is successful")
print("\n")
print("\n")
print("\nTesting for output Target A\n")
print(output1,"*",weight.T)
y=np.dot(output1,weight.T)
y[y<0]=-1
y[y>=0]=1
print("y=",y)
print("\n")
print("\nTesting for output Target C\n")
print(output2,"*",weight.T)
y=np.dot(output2,weight.T)
y[y<0]=-1
y[y>=0]=1
print("y=",y)

print("Since testing targets for pattern A and C gives correct input values, testing is successful")

