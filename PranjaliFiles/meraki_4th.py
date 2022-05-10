my_files=open("question3.txt","r")
file_data=my_files.read()
Delhi=open("delhi.txt","w")
Shimla=open("shimla.txt","w")
Other=open("others.txt","w")
new=file_data.split("\n")
i=0
while i<len(new):
    if "delhi" in new[i]:
        Delhi.write(new[i])
        Delhi.write("\n")
    elif "shimla" in new[i]:
        Shimla.write(new)
        Shimla.write("\n")    
    else:
        Other.write(new[i])
        Other.write("\n")
    i+=1
Delhi.close()
Shimla.close()
Other.close()
my_files.close()