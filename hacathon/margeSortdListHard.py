lists = [[1,4,5],[1,3,4],[2,6]]
List=[]
i=0
while i<len(lists):
    j=0
    while j<len(lists[i]):
        List.append(lists[i][j])
        j+=1
    i+=1
List.sort()
print(List)
