a=[2,36,44,22,3,4,5,6]
l=[]
i=0
while i<len(a):
    s=' '
    j=0
    d=str(a[i])
    while j<len(d):
        if d[j]=='1':
            s=s+'One '
        if d[j]=='2':
            s=s+'Two '
        if d[j]=='3':
            s=s+'Three '
        if d[j]=='4':
            s=s+'Four '
        if d[j]=='5':
            s=s+'Five '
        if d[j]=='6':
            s=s+'Six '
        if d[j]=='7':
            s=s+'Seven '
        if d[j]=='8':
            s=s+'Eight '
        if d[j]=='9':
            s=s+'Nine '
        if d[j]=='0':
            s=s+'Zero '
        j+=1
    i=i+1
    l.append(s)
print(l)