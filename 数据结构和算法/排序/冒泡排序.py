# 2 冒泡排序：它重复的走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来，走访数列的工作是重复的执行到没有再需要交换，也就是说该数列已经完成排序。
#时间复杂度 O(n^2)
#空间复杂度：O(1)
#稳定性：稳定

def bubble_sort(blist):
    count = len(blist)
    for i in range(0,count):
        for j in range(i+1,count):
            if blist[i] > blist[j]:
                blist[i],blist[j] = blist[j],blist[i]
    return blist

print(bubble_sort([4,5,6,7,8,2,3,1,0]))