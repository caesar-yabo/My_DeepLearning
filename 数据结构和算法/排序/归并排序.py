#      当n较大，则应采用时间复杂度为O(nlog2n)的排序方法：快速排序、堆排序或归并排序序。

"""
归并排序：采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并

时间复杂度：O(nlog₂n)
空间复杂度：O(1)
稳定性：稳定

"""

# 归并排序 Merge_Sort

def MergeSort(arrayList):
    arrayLen = len(arrayList)
    #判断输入参数的正确性,如果长度小于1，就说明为1
    if arrayLen <= 1:
        return arrayList
    midIndex = arrayLen//2
    #左边的部分去做 MergeSort
    leftArray = MergeSort(arrayList[:midIndex])
    #右边的去做 MergeSort
    rightArray = MergeSort(arrayList[midIndex:])
    #将左右两边合并，称为一个新的数组，并已经排序成功
    retArray = MergeCore(leftArray,rightArray)
    return retArray

def MergeCore(leftArray,rightArray):
    #首先需要定义两个指针,这两个指针，分别指向这两个数组的第一个元素
    leftIndex = 0
    rightIndex = 0
    #获取两个数组的长度，用于指出上面两个指针的边界是什么
    leftLen = len(leftArray)
    rightLen = len(rightArray)
    #定义一个返回的列表,这一步就代表空间复杂度至少是 O(n)
    retList = []
    #循环两个数组寻找最小值加入到返回值的数组中
    while leftIndex < leftLen and rightIndex < rightLen:
        if leftArray[leftIndex] < rightArray[rightIndex]:
            retList.append(leftArray[leftIndex])
            leftIndex += 1
        else:
            retList.append(rightArray[rightIndex])
            rightIndex += 1
    #下面的代码是将剩余的数组中内容放置在返回的数组中
    retList.extend(leftArray[leftIndex:])

    # while leftIndex < leftLen:
    #     retList.append(leftArray[leftIndex])
    #     leftIndex += 1

    retList.extend(rightArray[rightIndex:])

    # while rightIndex < rightLen:
    #     retList.append(rightArray[rightIndex])
    #     rightIndex += 1
    return retList


if __name__ == '__main__':
    # 14,33,27,10,35,19,42,44

    retList = MergeSort([14,33,27,10,35,19,42,44])
    print(retList)













