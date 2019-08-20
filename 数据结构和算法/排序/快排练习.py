# def QuickSort(array,left=0,right=None):
#     arrayLen = len(array)
#     if arrayLen <= 1:
#         return array
#     if right == None:
#         right = arrayLen - 1
#     if left < right:
#         pivot = partition(array,left,right)
#         QuickSort(array, left, pivot-1)
#         QuickSort(array, pivot+1, right)
#
# def partition(array,left,right):
#     i = left -1
#     for j in range(left,right):
#         if array[j] < array[right]:
#             array[j],array[i+1] = array[i+1],array[j]
#             i += 1
#     array[right],array[i+1] = array[i+1],array[right]
#     return i+1

# def QuickSort(array,left=0,right=None):
#     arrayLen = len(array)
#     if arrayLen <= 1:
#         return array
#     if right == None:
#         right = arrayLen -1
#     if left < right:
#         pivot = partition(array,left,right)
#         QuickSort(array,left,pivot-1)
#         QuickSort(array,pivot+1,right)
#
# def partition(array,left,right):
#     i = left-1
#     for j in range(left,right):
#         if array[j] < array[right]:
#             array[j],array[i+1] = array[i+1],array[j]
#             i += 1
#     array[right],array[i+1] = array[i+1],array[right]
#     return i+1

def QuickSort(array,left=0,right=None):
    arrayLen = len(array)
    if arrayLen <= 1:
        return array
    if right == None:
        right = arrayLen - 1
    if left < right:
        pivot = partition(array,left,right)
        QuickSort(array,left,pivot-1)
        QuickSort(array,pivot+1,right)

def partition(array,left,right):
    i = left-1
    for j in range(left,right):
        if array[j] < array[right]:
            array[j],array[i+1] = array[i+1],array[j]
            i += 1
    array[right],array[i+1] = array[i+1],array[right]
    return i+1







if __name__ == '__main__':
    array = [12,44,56,78,3,5,6,22,33]
    QuickSort(array)
    print(array)
