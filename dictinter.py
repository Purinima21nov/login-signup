d={"a":[2,3,4],"b":(5,6,7),"c":{6,7,8}}
sum=0
for i in d:
    if type(d[i])==type([]):
        for k in d[i]:
            sum+=k
    if type(d[i])==type(()):
        for k in d[i]:
            sum+=k
    if type(d[i])==type({}):
        for j in d[i]:
            sum+=j
print(sum)