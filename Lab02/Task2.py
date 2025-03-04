import random
population=[]
for i in range(4):
    g=''
    for j in range(3):
        x=random.randint(1,99)
        if x<10:
            g+='0'+str(x)
        else:
            g+=str(x)
    population.append(g)

x=random.randint(0,3)
g1=population[x]
y=None
while y==None:
    temp=random.randint(0,3)
    if temp!=x:
        y=temp
g2=population[y]

l=len(g1)
x=random.randint(1,l-2)
y=random.randint(x+1,l-1)
c1=g1[0:x]+g2[x:y]+g1[y:]
c2=g2[0:x]+g1[x:y]+g2[y:]
print("Parent1: ",g1,'\n'
      "Parent2: ",g2,"\n"
      "Cross1:  ",c1,"\n"
      "Cross2:  ",c2)