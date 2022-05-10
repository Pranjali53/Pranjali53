a=["my name is pranjali i am 17 years old"]
Leangth=0
count_character=0
count_integer=0
count_spaces=0
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if (a[i][j].islower()) or (a[i][j].isupper()):
            count_character+=1
        if (a[i][j].isdigit()):
            count_integer+=1
        if a[i][j]==" ":
            count_spaces+=1
        j+=1
    Leangth+=1
    i+=1
print(count_character)
print(count_integer)
print(count_spaces)
print(Leangth)