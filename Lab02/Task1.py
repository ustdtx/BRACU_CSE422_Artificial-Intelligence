#task1
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

print(population[0],fitness(population[0]))
