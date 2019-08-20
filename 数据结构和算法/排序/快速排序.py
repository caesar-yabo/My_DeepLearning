
"""

 快速排序：是目前基于比较的内部排序中被认为是最好的方法，当待排序的关键字是随机分布时，快速排序的平均时间最短；

通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列
时间复杂度：O(nlog₂n)
空间复杂度：O(nlog₂n)
稳定性：不稳定

"""
#快排的主函数，传入参数为一个列表，左右两端的下标
def QuickSort(array,leftIndex=0,rightIndex=None):
    #数组的长度
    arrayLen = len(array)
    #长度为1 的话 或者 空 的话 直接返回 数组
    if arrayLen <= 1:
        return array
    #程序一开始 如果没有给一个最右边的索引值导入话，那么我们就给它 赋值一个 就是数组的最右边的 那个索引值。
    if rightIndex == None:
        rightIndex = arrayLen - 1
    # 保护条件，只有满足  左边索引小于右边索引的时候 再开始排序
    if leftIndex < rightIndex:
        #找到 基准的 索引值 传入参数，通过Partitions函数，获取k下标值
        pivot = partition(array,leftIndex,rightIndex)
        #递归前后半区 对基准前面不部分继续快排
        QuickSort(array,leftIndex,pivot - 1)
        #对基准后半积分继续快排
        QuickSort(array,pivot + 1,rightIndex)

def partition(array,leftIndex,rightIndex):

    pivotValue = array[rightIndex]
    #将最左侧的 索引值 给 i
    i  = leftIndex
    #将最右侧的 索引的前一个 给j
    j = rightIndex -1
    #当left下标，小于right下标的情况下，此时判断二者移动是否相交，若未相交，则一直循环
    while i < j:
        # 当left对应的值大于锚点 基准点 参考值，就一直向左移动
        while j > leftIndex and array[j] > pivotValue:
            j -= 1
        #当left对应的值小于基准点参考值，就一直向右移动
        while i < rightIndex and array[i] <= pivotValue:
            i += 1
        #若移动完，二者仍未相遇则交换下标对应的值
        if i < j:
            array[j],array[i] = array[i],array[j]
            i+=1
            j-=1
    #若移动完，已经相遇，则交换right对应的值和参考值
    array[i],array[rightIndex] = array[rightIndex],array[i]
    # 返回 一个 索引值
    return i

# 《算法导论》中的快排程序
def partition2(array,leftIndex,rightIndex):
    #设置一个 左边的指针位置 为 左侧的 前一个
    i = leftIndex -1
    #遍历 除 基准数之外的 数
    for j in range(leftIndex,rightIndex):
        #比较 遍历的数 和 基准数 ，若是小于基准数 则 换到数组前面去
        if array[j] < array[rightIndex]:
            #交换位置，将遍历的比 基准数小的数 放到 我们指针 的 后一个上，然后 这个时候指针向后移一位。当遍历的数大于我们的基准数的时候，不移动，而且 指针也不发生变化，那么 当我们遍历完一圈以后，把 我们的基准数 放到 索引i 的后一个 位置，那么就形成了 一个 基准数 左边都是比它小的数，基准数右边 都是比它大的数 这样的模式。然后要把 索引 i 的后一个位置 作为基准数 与 原基准数 交换位置，进而可以第二次来 遍历比较。
            array[j],array[i+1] = array[i+1],array[j]
            i += 1
    #遍历完了以后，将 left 位置上的数 和 最后一个 数  即 right 上的数互换位置，就 重置 基准数了。
    array[rightIndex],array[i+1] = array[i+1],array[rightIndex]
    #返回基准的下标
    return i+1



if __name__ == '__main__':
    array = [14,33,27,10,35,19,42,44]
    QuickSort(array)
    print(array)





