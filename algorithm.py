
#Creating a function with argument -> sequence of unsorted values
def quick_sort(sequence):
    length = len(sequence)

    #skiping sequences wich are 0 or 1
    if length <= 1:
        return sequence
    else:
        #Defining our pivot wich will be the last number of the sequence
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    #Partitions items around the picked pivot
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    #Calling the algorithm, we do this over and over until the logic breaks
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([10, 80, 30, 90, 40, 50, 70]))
