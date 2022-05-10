my_files=open("people1-exercise.txt","r")
file_data =my_files.readlines()
c=0
i=0
while i<len(file_data):
    c+=1
    i+=1
print(c)
my_files.close()