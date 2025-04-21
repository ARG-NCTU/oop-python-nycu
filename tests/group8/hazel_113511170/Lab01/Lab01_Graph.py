import matplotlib.pyplot as plt

#EX01
fig=plt.figure(figsize=(8,6))
plt.title("The Variation of Vx with respect to Vsupply in Exp.01 ")
plt.xlabel("Vsupply (V)")
plt.ylabel("Vx (V)")
x=[0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]
y=[0.0050,0.0066,0.0065,0.229,0.672,1.0922,1.5561,2.0204,2.2043,3.2122]
plt.subplot(1,1,1)
plt.plot(x,y)
plt.scatter(x, y, color='blue', marker=".", s=200, label="Data Points")
for i in range(10):
    plt.text(0.5*i+0.2,y[i]+0.1,"({}, {})".format(i*0.5+0.5,y[i]),fontsize=6)
plt.grid()
plt.savefig("ex01.png")

#EX02-1

fig01=plt.figure(figsize=(8,6))
plt.title("The Variation of Vx with respect to Button Status without LED")
plt.xlabel("Button Status")
plt.ylabel("Vx (V)")
x=[0,2]
y=[4.9592,0.0083]
plt.xticks([0.5,2.5],["Released","Pressed"])
plt.scatter(x, y, color='blue', marker="*", s=100, label="Vsupply=5V")
for i in range(2):
    plt.text(x[i]+0.2,y[i]+0.1,y[i],fontsize=10)
plt.bar(x,y)
plt.legend()

w=[1,3]
z=[3.2566,0.0077]
plt.scatter(w, z, color='red', marker="*", s=100, label="Vsupply=3.3V")
plt.bar(w,z)
for i in range(2):
    plt.text(w[i]+0.2,z[i]+0.1,z[i],fontsize=10)
plt.legend()
plt.savefig("ex02-1.png")


#EX02-2
fig02=plt.figure(figsize=(8,6))
plt.title("The Logic Status with respect to Button Status with LED in PULL-UP Circuit")
plt.xlabel("Button Status")
plt.ylabel("Logic State(1 signifies the LED is bright)")
x=[0,2]
y=[1,0]
plt.xticks([0.5,2.5],["Released","Pressed"])
plt.yticks([0,1],["0","1"])
plt.scatter(x, y, color='blue', marker="*", s=100, label="Vsupply=5V")
plt.bar(x,y)
plt.legend()

w=[1,3]
z=[1,0]
plt.scatter(w, z, color='red', marker="*", s=100, label="Vsupply=3.3V")
plt.bar(w,z)
plt.legend()
plt.savefig("ex02-2.png")

#EX03
fig03=plt.figure(figsize=(8,6))
plt.title("The Logic Status with respect to Control Signal")
plt.xlabel("Button Status")
plt.ylabel("Logic State(1 signifies the LED is bright)")
x=[0,2]
y=[1,0]
plt.xticks([0.5,2.5],["Released","Pressed"])
plt.yticks([0,1],["0","1"])
plt.scatter(x, y, color='blue', marker="*", s=100, label="Pull-up")
plt.bar(x,y)
plt.legend()

w=[1,3]
z=[0,1]
plt.scatter(w, z, color='red', marker="*", s=100, label="Pull-down")
plt.bar(w,z)
plt.legend()
plt.savefig("ex03.png")

#EX04
fig03=plt.figure(figsize=(8,6))
plt.title("The Logic Status with respect to Static IO Button")
plt.xlabel("Button Status D0")
plt.ylabel("Logic State(1 signifies the LED is bright)")
x=[0,2]
y=[1,0]
plt.xticks([0.5,2.5],["Released","Pressed"])
plt.yticks([0,1],["0","1"])
plt.scatter(x, y, color='blue', marker="*", s=100, label="Pull-up")
plt.bar(x,y)
plt.legend()

w=[1,3]
z=[0,1]
plt.scatter(w, z, color='red', marker="*", s=100, label="Pull-down")
plt.bar(w,z)
plt.legend() 
plt.savefig("ex04.png")

#EX05
fig04=plt.figure(figsize=(8,6))
plt.title("The Logic Status with respect to Static IO Button")
plt.xlabel("Button Status D0")
plt.ylabel("Logic State D1 ")
x=[0,2]
y=[1,0]
plt.xticks([0.5,2.5],["Released","Pressed"])
plt.yticks([0,1],["0","1"])
plt.scatter(x, y, color='blue', marker="*", s=100, label="Pull-up")
plt.bar(x,y)
plt.legend()

w=[1,3]
z=[0,1]
plt.scatter(w, z, color='red', marker="*", s=100, label="Pull-down")
plt.bar(w,z)
plt.legend() 
plt.savefig("ex05.png")

plt.show()
