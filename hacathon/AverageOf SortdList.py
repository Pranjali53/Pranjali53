f=[1,5,2,4,3]
f.sort()
print(f)
i=0
c=0
sum=0
while i<len(f):
  c=c+1
  sum=sum+f[i]
  i=i+1
print(sum/c)