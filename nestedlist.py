def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result
nested_list = ['1',['2',['3','4']],'5']
print(flatten_list(nested_list))
total=sum(int(i) for i in flatten_list(nested_list))
print("Sum:", total)