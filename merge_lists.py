def merge_sorted_lists(list1, list2):
    i = 0
    j = 0
    result = []
    
    # Compare elements from both lists and add the smaller one to result
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
            
    # If there are remaining elements in list1, add them
    while i < len(list1):
        result.append(list1[i])
        i += 1

    # If there are remaining elements in list2, add them
    while j < len(list2):
        result.append(list2[j])
        j += 1
        
    return result

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

print(merge_sorted_lists(list1, list2))
