nums = [1,1,1,2,2,3]
k = 2
values = {}
res=[]
for num in nums:
    if num not in values:
        values[num]= 1
    else:
        values[num]= values[num] +1 
        
for i in range(k):
    max_value_key = max(values, key=values.get)
    values.pop(max_value_key)
    res.append(max_value_key)
