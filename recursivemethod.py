count=0
def recursion(lst):
    global count
    for ele in lst:
        if isinstance(ele,list):
            recursion(ele)
        else:
            count=count+ele
    return count            
lst=[[1,2,3,4],[4,5,6,7],[7],[8,9,[1,2]]]
print(recursion(lst))