a=input("enter==")
i=0
while i<len(a):
  b=(a[-1::-1])
  i=i+1
if a==b:
  print("palidrome")
else:
  print("not palidrome")