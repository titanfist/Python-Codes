def Insert(l):
    for i in range(len(l)):
        p = i
        while p>0 and l[p]<l[p-1]:
           (l[p],l[p-1])=(l[p-1],l[p])
           p-=1
