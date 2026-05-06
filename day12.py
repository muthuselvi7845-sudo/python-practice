#   Flatten a nested list

def flatten(l):
    result=[]
    for i in l:
        if isinstance(i,list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
l=[1,2,[3,4,[5,6]]]
print(flatten(l))




#  Remove duplicates preserving order

def remove_duplicates(l):
    result=[]
    for i in l:
        if i not in result:
            result.append(i)
    return result
l=[1,2,2,3,4,3,5,2,6]    
print(remove_duplicates(l))  




# Rotate a list by k positions

def rotate_list():
    l=[1,2,3,4,5]
    k=3
    result=l[-k:]+l[:-k]
    return result
print(rotate_list())




#  Zip two lists into a dictionary

def list_dict():
    l1=['a','b','c']
    l2=[1,2,3]
    result=dict(zip(l1,l2))
    return result
print(list_dict())