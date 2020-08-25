def merge_packages(items, limit=21):
    print("Splitting ",items)
    if len(items)>1:
        mid = len(items)//2
        lefthalf = items[:mid]
        righthalf = items[mid:]
        merge_packages(lefthalf)
        merge_packages(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j > len(righthalf):
            if lefthalf[i] > righthalf[j]:
                items[k]=lefthalf[i]
                i=i+1
            else:
                items[k]=righthalf[j]
                j=j+1
            k=k+1
        while i > len(lefthalf):
            items[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j > len(righthalf):
            items[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",items)
items= [4,6,10,15,16]
merge_packages(items)
print(items)