import math as m
import matplotlib.pyplot as p
n=int(input("Enter number of Test cases:"))
#Next 6 variables are constant variables for the spring with varying parameters.
w=500
RS=35
dw=6
nc=10
G=84000
g=9.81
c1=0
c2=0
c3=0
cc1=[]
ic1=[]
cc2=[]
ic2=[]
cc3=[]
ic3=[]
print("********Diameter of the Wire********")
diaw=[]
delta1=0
deflection1=[]
frequency1=[]
con1=(64*w*(RS**3)*nc)/(G)
for i in range(1,n+1):
    dw=i
    delta1=((con1)/(dw**4))
    if delta1>=0 and delta1<=20:
        diaw.append(dw)
        deflection1.append(delta1)
        omega=m.sqrt((g)/delta1)
        frequency1.append(omega)
    else:
        c1+=1
        ic1.append(i)
        cc1.append(delta1)
print("Out of boundary count:",c1,"\n",cc1,"\n",ic1)
print("Diaw",diaw)
print("deflection",deflection1)
print("Frequency",frequency1)
print("********Radius of the Spring********")
rads=[]
delta2=0
deflection2=[]
frequency2=[]
dw=6
con2=(64*w*nc)/((G)*(dw**4))
for i in range(1,n+1):
    RS=i
    delta2=((con2)*(RS**3))
    if delta2>=0 and delta2<=20:
        rads.append(RS)
        deflection2.append(delta2)
        omega2=m.sqrt((g)/delta2)
        frequency2.append(omega2)
    else:
        c2+=1
        ic2.append(i)
        cc2.append(delta2)
print("Out of boundary count:",c2,"\n",cc2,"\n",ic2)
print("Rads",rads)
print("deflection",deflection2)
print("Frequency",frequency2)
print("********Number of coils of the Spring********")
coil=[]
delta3=0
deflection3=[]
frequency3=[]
RS=35
con3=(64*w*(RS**3))/(G*(dw**4))
for i in range(1,n+1):
    nc=i
    delta3=((con3)*(nc))
    if delta3>=0 and delta3<=100:
        coil.append(nc)
        deflection3.append(delta3)
        omega3=m.sqrt((g)/delta3)
        frequency3.append(omega3)
    else:
        c3+=1
        ic3.append(i)
        cc3.append(delta3)
print("Out of boundary count:",c3,"\n",cc3,"\n",ic3)
print("Number of Coils",coil)
print("deflection",deflection3)
print("Frequency",frequency3)
#1
p.subplot(3,2,1)
p.plot(diaw,deflection1,marker="o",color='k',label="Deflection")
p.title('Diameter of the Wire vs Deflection')
p.xlabel('Diameter of the wire')
p.ylabel('Deflection(in mm)')
p.legend()
p.subplot(3,2,2)
p.plot(diaw,frequency1,marker="*",color='g',label="Frequency")
p.title('Diameter of the Wire vs Frequency')
p.xlabel('Diameter of the wire')
p.ylabel('Frequency(in Hz)')
p.legend()
#2
p.subplot(3,2,3)
p.plot(rads,deflection2,marker="o",color='k',label="Deflection")
p.title("Radius of the Spring vs Deflection")
p.xlabel('Radius of the Spring')
p.ylabel('Deflection(in mm)')
p.legend()
p.subplot(3,2,4)
p.plot(rads,frequency2,marker="*",color='g',label="Frequency")
p.title("Radius of the Spring vs Frequency")
p.xlabel('Radius of the Spring')
p.ylabel('Frequency(in Hz)')
#3
p.subplot(3,2,5)
p.plot(coil,deflection3,marker="o",color='k',label="Deflection")
p.title('Number of coils of the Spring vs Deflection')
p.xlabel('Number of coils of the Spring ')
p.ylabel('Deflection(in mm)')
p.legend()
p.subplot(3,2,6)
p.plot(coil,frequency3,marker="*",color='g',label="Frequency")
p.title('Number of coils of the Spring vs Frequency')
p.xlabel('Number of coils of the Spring ')
p.ylabel('Frequency(in Hz)')
p.legend()
p.show()
