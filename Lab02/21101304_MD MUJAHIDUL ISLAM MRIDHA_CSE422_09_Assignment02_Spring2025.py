#Task1
import random
priceChange=[-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5]
max=0

population=[]
for i in range(4):
    p=[]
    for i in range(3):
        x=random.randint(1,99)
        p.append(x)
    population.append(p)

def fitness(gene):
    money=1000
    loss=gene[0]
    profit=gene[1]
    size=gene[2]
    for i in priceChange:
        invest=money*(size/100)
        money=money-invest
        if i<(loss*-1):
            invest-=invest*(loss/100)
        elif i>(profit):
            invest+=invest*(profit/100)
        else:
            invest+=invest*(i/100)
        money+=invest



    return money-1000

for i in population:
    if fitness(i)>max:
        max=fitness(i)

def recombinationAndMutation(population):
    child=[]
    for i in range(10):
        p1=population[random.randint(0,3)]
        p2='run'
        while p2=='run':
            x=population[random.randint(0,3)]
            if x!=p1:
                p2=x
        s=random.randint(1,2)
        c1=p1[0:s]+p2[s:]
        c2=p2[0:s]+p1[s:]
        child.append(c1)
        child.append(c2)
    for i in child:
        m=random.randint(0,100)
        if m<11:
            j=random.randint(0,2)
            i[j]=random.randint(1,99)
    sortedChild=sorted(child,key=fitness,reverse=True)[:4]

    return sortedChild

for i in range(10):
    population=recombinationAndMutation(population)


print("Best Strategy: ",population[0])

#Task2
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

    

