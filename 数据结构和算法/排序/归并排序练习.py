

def MergeSort(array):
    arrayLen = len(array)
    if arrayLen <= 1:
        return array
    midIndex = arrayLen // 2
    leftArray = MergeSort(array[:midIndex])
    rightArray = MergeSort(array[midIndex:])
    return MergeCore(leftArray,rightArray)

def MergeCore(leftArray,rightArray):
    left = 0
    right = 0
    leftLen = len(leftArray)
    rightLen = len(rightArray)
    retList = []
    while left < leftLen and right < rightLen:
        if leftArray[left] < rightArray[right]:
            retList.append(leftArray[left])
            left += 1
        else:
            retList.append(rightArray[right])
            right += 1
    retList.extend(leftArray[left:])
    retList.extend(rightArray[right:])
    return retList


if __name__ == '__main__':
    retList = MergeSort([14,33,27,10,35,19,42,44])
    print(retList)
