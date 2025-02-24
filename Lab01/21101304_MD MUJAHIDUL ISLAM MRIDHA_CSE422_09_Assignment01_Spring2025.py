file= open("Input file.txt", "r")
content = file.read()
lines=content.split('\n')
graph={}
heuristic={}
for i in lines:
  l=i.split(' ')
  if l[0] not in graph:
    graph[l[0]]=[]
    heuristic[l[0]]=int(l[1])
    r=len(l)
    for j in range(2,r,2):
      graph[l[0]].append((l[j],int(l[j+1])))

def aStar(start,goal,graph,heu):
  visited=[]
  pQueue={}
  parent={}
  dist={}
  pQueue[start]=heu[start]
  parent[start]=None
  dist[start]=0
  min=heu[start]
  minV=start
  while goal not in visited or pQueue!={}:
    node=minV

    for i in graph[node]:
      if i[0] not in visited:
        parent[i[0]]=node
        dist[i[0]]=dist[node]+i[1]
        pQueue[i[0]]=dist[i[0]]+heu[i[0]]
    pQueue.pop(node)
    visited.append(node)
    min=float('inf')
    for i in pQueue.keys():
      if pQueue[i]<min:
        min=pQueue[i]
        minV=i

  path=[goal]
  curr=goal
  while parent[curr]!=None:
    path.append(parent[curr])
    curr=parent[curr]
  pathStr=''
  for i in range(len(path)-1,-1,-1):
    if i!=0:
      pathStr+= path[i]+' -> '
    else:
      pathStr+= path[i]

  print('Path: ',pathStr)
  print("Total Distance: ", dist[goal])





  return None

start=input("Start node: ")
dest= input('Destination: ')

aStar(start,dest,graph,heuristic)
