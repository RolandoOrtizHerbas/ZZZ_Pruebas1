import numpy as np
import math
import matplotlib.pyplot as plt
x1 = np.array([2.7810836,1.465489372,3.396561688,1.38807019,3.06407232,7.627531214,5.3324441248,6.922596716,8.675418651,7.673756466])
x2 = np.array([2.550537003,2.362125076,4.400293529,1.850220317,3.005305973,2.759262235,2.088626775,1.77106367,-0.242068655,3.508563011])
y= np.array([0,0,0,0,0,1,1,1,1,1])
### print(x1)
### print(x2)
### ax = plt.hist(x1)
###ax = plt.subplot() 
###ax.scatter(x1,x2,marker="x", color="C1")
###plt.show() 
b0i=0.0
b1i=0.0
b2i=0.0
alfa = 0.3
out = b0i + b1i*x1[0]+b2i*x2[0]
pred = 1/(1 + math.exp(-out))    
print("  Inicia proceso de aprendizaje  ")
b0 = b0i + alfa*(y[0] - pred)*pred*(1 - pred)*1
b1 = b1i + alfa*(y[0] - pred)*pred*(1 - pred)*x1[0]
b2 = b2i + alfa*(y[0] - pred)*pred*(1 - pred)*x2[0]
print("==============")
print("i = ",0,"pred=", pred ,"B0=",b0i,"B1=",b1i,"B2=",b2i,"X1=",x1[0],"X2=" , x2[0],"y=",y[0])
print("B0=", b0)
print("B1=", b1)
print("B2=", b2)
b0i=b0
b1i=b1
b2i=b2
for j in range(9):
    ### epocas
    for i in range(1,10):
        ### datos
        out = b0i + b1i*x1[i]+b2i*x2[i]
        pred = 1/(1 + math.exp(-out))
        ###print("============")
        ###print("i = ",i,"pred=", pred ,"B0=",b0i,"B1=",b1i,"B2=",b2i,"X1=",x1[i],"X2=" , x2[i],"y=",y[i])
        #print(x1[i],"," , x2[i],",",y[i])
        b0 = b0i + alfa*(y[i] - pred)*pred*(1 - pred)*1
        b1 = b1i + alfa*(y[i] - pred)*pred*(1 - pred)*x1[i]
        b2 = b2i + alfa*(y[i] - pred)*pred*(1 - pred)*x2[i]  
        ### print("==============")
        #print("B0=", b0)
        #print("B1=", b1)
        #print("B2=", b2)
        b0i=b0
        b1i=b1
        b2i=b2
###  Parametros ya estimados      
print("================================================")
print("B0=", b0)
print("B1=", b1)
print("B2=", b2)  
### Predicciones
print("================================================")
### se completo 10 epocas para determinar los parametros
for i in range(10):
    out = b0 + b1*x1[i]+b2*x2[i]
    pred = 1/(1 + math.exp(-out)) 
    if (pred >= 0.5):
        yp=1
    else:
        yp=0  
    ## print("{:.5f}".format(x1[i]))      
    print("i = ",i,"X1= {:.10f}".format(x1[i]),"X2= {:.10f}".format(x2[i]),"y=",y[i],"Pred= {:.10f}".format(pred), "yp=",yp)
    
    