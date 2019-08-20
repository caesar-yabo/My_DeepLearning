#3 选择排序 ： 第一趟，在待排序记录r1 。。。r(n)中选出最小的记录，将它与r1 交换，第二趟，在待排序记录r2 ~ r(n) 中选出最小的记录，将它与 r2 交换，以此类推，第i趟在待排序记录 r[i]~r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。

#时间复杂度 O(n^2)
#空间复杂度：O(1)
#稳定性：不稳定

def select_sort(slist):
    #外层循环控制循环次数
    for i in range(len(slist)):
        #假设找到的最小元素下标为j
        x = i
        #寻找最小元素的过程
        for j in range(i,len(slist)):
            #假设最小下标的值，大于循环中一个元素，那么就改变最小值的下标
            if slist[j] < slist[x]:
                x = j
        #循环一开始就假设把最小值的下标赋值给变量 x
        # 在不停的循环中，不停的交换两个不一样大小的值
        slist[i],slist[x] = slist[x],slist[i]
    #返回 排好序的列表
    return slist



if __name__ == '__main__':
    arrayList = [4,5,6,7,3,2,6,9,8]
    select_sort(arrayList)
    print(arrayList)