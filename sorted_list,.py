l = [1,829,293,3383,383,38332,12,583,28,50,92,495,82,592,193]

print("orig list", l)

counts = 0

for nums in l:
    counts = counts + nums
    
    
avy = counts/len(l)

print("sum = ", counts)

print("average = ",avy)

l.sort()
    
print("the sorted list",l)  