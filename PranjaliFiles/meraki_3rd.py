my_files=open("file-qustion3.txt","w")
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
i=0
while i<len(banks_list):
    my_files.write(banks_list[i])
    my_files.write("\n")
    i+=1
print(my_files)
my_files.close()