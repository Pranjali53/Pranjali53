f = open("demofile2.txt", "w+")
f.write("Now the file has more content!")
f.close()


f = open("demofile2.txt", "r+")
print(f.read())