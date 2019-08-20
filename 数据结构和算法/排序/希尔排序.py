#4 希尔排序 ： 希尔排序 是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰好被分成一组，算法终止

#时间复杂度 O(n^2)
#空间复杂度：O(nlogn)
#稳定性：不稳定

def shell_sort(slist):
    count = len(slist)
    step = 2
    group = count // step
    while group>0:
        for i in range(group):
            j = i + group
            while j < count:
                key = slist[j]
                k = j - group
                while k >= 0:
                    if slist[k] > key:
                        slist[k+group] = slist[k]
                        slist[k] = key
                    k = k - group
                j = j + group
        group = group // step
    return slist

# print(shell_sort([4,5,7,3,2,6,9,8,0]))

def ShellSort(arrList):
    arrayLen = len(arrList)
    h = 1
    while h < arrayLen//3:
        h = h * 3 + 1
        #插入排序的方法，判断是不是后一个比前一个要小
        #如果是则交换
    while h >= 1:
        for i in range(h,arrayLen):
            j = i
            while j >= h and arrList[j] < arrList[j-h]:
                arrList[j] ,arrList[j-h] = arrList[j-h],arrList[j]
                j -= h
        h  //= 3


if __name__ == '__main__':
    arrList = [14,33,27,10,35,19,42,44]
    ShellSort(arrList)
    print(arrList)

