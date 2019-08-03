Art1,Bat=map(int,input().split())
Cat=list(map(int,input().split()))
purt=list(map(int,input().split()))
qurt=[]
aat=0
for i in range(Art1):
    xt=purt[i]/Cat[i]
    qurt.append(xt)
while Bat>=0 and len(qurt)>0:
    mindex=qurt.index(max(qurt))
    if Bat>=Cat[mindex]:
        aat=aat+purt[mindex]
        Bat=Bat-Cat[mindex]
    Cat.pop(mindex)
    purt.pop(mindex)
    qurt.pop(mindex)
print(aat)
