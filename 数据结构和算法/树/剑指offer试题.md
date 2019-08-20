#### 1.二维数组中的查找  [^本题考点 *查找*]

​	**题目：在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。**

~~~python
# -*- coding:utf-8 -*-

class Solution:
    # array 二维列表

    # 时间复杂度O(n^2) 291ms
    def Find_1(self, target, array):
        # write code here
        for i in range(len(array)):
            for j in range(len(array[i])):
                if target == array[i][j]:
                    return True
        return False

    # 时间复杂度O(n)
    def Find_2(self, target, array):
        # 行数为二维数组的长度
        row_count = len(array)
        i = 0
        # 列数为任意一列的长度
        column_count = len(array[0])
        j = column_count - 1
        # 当i小于行数（即行数,也就是此时的i,取值0--row_count-1）且列数-1大于等于0（即列数，也将就是此时的j,取值0--column_count-1）的时候，循环
        while i < row_count and 0 < j:
            value = array[i][j]
            if value == target:
                return True
            elif value < target:
                i += 1
            else:
                j -= 1
        return False
~~~

---

#### 2.替换空格 [^本题考点 *字符串*]

​	**题目：请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。**

```python
# -*- coding:utf-8 -*-

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        strLen = len(s)
        # 定义空字符串准备接收
        rep_str = ''
        # 遍历，检测到空格就加上"%20"
        for i in range(strLen):
            if s[i].isspace():
                rep_str += '%'
                rep_str += '2'
                rep_str += '0'
            else:
                rep_str += s[i]
        # 返回辅助字符串
        return rep_str
```

---

#### 3.从尾到头打印链表 [^本题考点 *链表*]

​	**题目：输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。**

~~~python
# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        output = []
    	pTmp = listNode
        while pTmp:
            output.insetr(0, pTmp.val)
            pTmp = pTmp.next
        return output
~~~

---

#### 4.重建二叉树 [^本题考点 *二叉树*]

​	**题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。**

~~~python
# -*- coding:utf-8 -*-

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        if len(pre) != len(tin):
            return None

        # 取出pre的值
        root = pre[0]
        # 新建一个根节点
        rootNode = TreeNode(root)
        # 在tin中找到pos的位置
        pos = tin.index(root)
        # 将tin以pos的位置分为左右两边（除去pos）
        tinLeft = tin[: pos]
        tinRight = tin[pos+1: ]
        # 将pre以pos的位置分为左右两边（除去pos）
        preLeft = pre[1: pos+1]
        preRight = pre[pos+1: ]
        # 将preLeft和tinLeft再次走一遍这个方法，递归下去
        leftNode = self.reConstructBinaryTree(preLeft, tinLeft)
        # 将preRight和tinRight再次走一遍这个方法，递归下去
        rightNode = self.reConstructBinaryTree(preRight, tinRight)
        # 将leftNode赋值给rootNode的左节点
        rootNode.left = leftNode
        # 将rightNode赋值给rootNode的右节点
        rootNode.right = rightNode
        # 返回根节点
        return rootNode
~~~

---

#### 5.用两个栈实现队列 [^本题考点 *队列  栈*]

​	**题目：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。**

```python
# -*- coding:utf-8 -*-

class Solution:
    def __init__(self):
        self.acceptStack = []
        self.outputStack = []

    def push(self, node):
        # 入栈操作，实现队列的Push操作
        self.acceptStack.append(node)

    def pop(self):
        # 要出的列表要是没有东西，就将两个的内容弹出，加入
        if not self.outputStack:
            while self.acceptStack:
                self.outputStack.append(self.acceptStack.pop())
		# 给出一个出栈的返回值，实现队列的POP操作
        if self.outputStack:
            return self.outputStack.pop()
        else:
            return None
```

------

#### 6.旋转数组的最小数字 [^本题考点 *查找*]

​	**题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。**

~~~python
# -*- coding:utf-8 -*-

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here

        # 时间复杂度O(n)
        # minNum = 0
        # for i in range(0, len(rotateArray)):
        #     minNum = minNum if minNum  < rotateArray[i] and minNum != 0 else rotateArray[i]
        #
        # return minNum

        # 最小值，一定比前面的要小
        # 二分法查找数据，找左右的方法是：右边的值大于种植，就说明最小值在左边
        # 时间复杂度O(logn)
        # 若数组大小为0
        if not rotateArray:
            # 返回0
            return 0
        # 左侧索引
        left = 0
        # 右侧索引
        right = len(rotateArray) - 1
        # 当左侧索引小于右侧索引时循环
        while left <= right:
            # 中间值为左侧索引和右侧索引求和再除以2，向下取整
            mid = (left + right) >> 1  # (left + right) // 2
            # 若中间索引对应的值小于它左侧的值，即为要取得值
            if rotateArray[mid] < rotateArray[mid - 1]:
                # 返回目标值
                return rotateArray[mid]
            # 若中间索引对应的值小于右侧索引的值，目标值就在左侧
            elif rotateArray[mid] < rotateArray[right]:
                # 将右侧索引置为中间索引-1
                right = mid - 1
            # 反之
            else:
                # 将左侧索引置为中间索引+1
                left = mid + 1
     
~~~

---

#### 7.斐波那契数列  [^本题考点 *递归，复杂度*]

​	**题目：大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39**

~~~python
# -*- coding:utf-8 -*-

class Solution:
    # 时间复杂度 O(n)
    def Fibonacci_1(self, n):
        # write code here
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return a
    
    # 递归，时间复杂度 O(2^n)
    def Fibonacci_2(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n > 1:
            num = Fibonacci(n-1) + Fibonacci(n-2)
            return num
        return None

# lambda 表达式版
fibonacci = lambda n: n if n < 2 else fibonacci(n-1) + fibonacci(n-2)
~~~

---

#### 8.跳台阶 [^本题考点 *逻辑分析*]

​	**题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。**

~~~python
# -*- coding:utf-8 -*-

'''
分析：
	假设有n级台阶，青蛙从最后的第n级开始往前跳，有可能是跳1级台阶，之后还有n-1级台阶，也就是f(n-1)中可能性；也有可能跳2级台阶，之后还有n-2级台阶，也就是f(n-2)种可能性。所以从n级开始跳的跳法就有 f(n) = f(n-1) + f(n-2)种，这就类似于斐波那契数列，只不过是从1,2开始
'''
class Solution:
    # 简单版
    def jumpFloor_1(self, number):
        if number == 1:
            return 1
        if number == 2:
            return 2
        reg = 0
        a = 1
        b = 2
        for i in range(2, number):
            reg = a + b
            a = b
            b = reg
        return reg
    # 简化版
    def jumpFloor_2(self, number):
        a, b = 1, 1
        for i in range(number):
            a, b = b, a+b
        return a

# lambda 表达式版
fibonacci = lambda n: n if n <= 2 else fibonacci(n-1) + fibonacci(n-2)
~~~

---

#### 9.变态跳台阶 [^本题考点 *逻辑分析*]

​	**题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。**

~~~python
# -*- coding:utf-8 -*-

'''
分析：
	假设有n级台阶，青蛙从最后的第n级开始往前跳，可能性为：
	f(n) = f(n-1) + f(n-2) + ... + f(2) + f(1)		---> ①
	青蛙从最后的第n-1级开始往前跳，可能性为：
	f(n-1) = f(n-2) + f(n-3) + ... + f(2) + f(1)	---> ②
	将②式代入①式得：
	f(n) = 2f(n-1)
'''
class Solution:
    # 简单版
    def jumpFloorII_1(self, number):
        if number == 1:
            return 1
        if number == 2:
            return 2
        ret = 1
        a = 1
        for i in range(2, number+1):
            ret = 2*ret
            a = ret
        return ret
   	# 简化版
    def jumpFloorII_2(self, number):
        a, b = 1, 2
        for i in range(number-1):
            a, b = b, b*2
        return a
~~~

---

#### 10.矩形覆盖 [^本题考点 *逻辑分析*]

​	**题目：我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？**

~~~python
# -*- coding:utf-8 -*-

'''
	也是斐波那契数列的变形
'''

class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        a, b = 1, 2
        for i in range(number-1):
            a, b = b, a+b
        return a
~~~

---

#### 11.包含min函数的栈 [^本题考点 *栈*]

​	**题目：定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。**

~~~python
# -*- coding:utf-8 -*-

'''
如果用固定空间做不出时间上的优化，就用空间换时间
'''


# 第一种是self.stack和self.minValue的长度时刻保持一致
class Solution:
    def __init__(self):
        self.stack = []
        self.minValue = []
        
    def push(self, node):
        self.stack.append(node)
        if self.minValue:
            if node < self.minValue[-1]:
                self.minValue.append(node)
            else:
                self.minValue.append(self.minValue[-1])
        else:
            self.minValue.append(node)
            
    def pop(self):
        if not self.stack:
            return None
        self.minValue.pop()
        return self.stack.pop()

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def min(self):
        if not self.minValue:
            return None
        return self.minValue[-1]

# 第二种是当self.minValue中的值重复就不再添加，但是删除的时候进行一下判断，即self.stack和self.minValue值相等再弹出self.minValue中的值
class Solution:
    def __init__(self):
        self.stack = []
        self.minValue = []

    def push(self, node):
        self.stack.append(node)
        if self.minValue:
            if node <= self.minValue[-1]:
                self.minValue.append(node)
        else:
            self.minValue.append(node)
            
    def pop(self):
        if not self.stack:
            return None
        if self.stack[-1] == self.minValue[-1]:
            self.minValue.pop()
        return self.stack.pop()

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def min(self):
        if not self.minValue:
            return None
        return self.minValue[-1]
~~~

---

#### 12.栈的压入、弹出序列 [^本题考点 *栈*]

​	**题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）**

~~~python
# -*- coding:utf-8 -*-

class Solution:
    def IsPopOrder(self, pushV, popV):
        # 语法错误，返回错误
        if not pushV or len(pushV) != len(popV):
            return False
        stack = []
        '''
        1,2,3,4,5
        4,5,3,2,1 √
        4,3,5,1,2 ×  因为若是4为首位出栈的话，123必定还在栈中，无论5什么时候入栈和出栈，都不可能出现1在2前面的现象，所以错误
        '''
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        # 不能合理实现辅助列表和要判断的列表之间全部清空
        if len(stack):
            # 返回错误
            return False
        # 都满足，返回正确
        return True
~~~

---

#### 13.数组中只出现一次的数字 [^本题考点 *数组*]

​	**一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。**

~~~python
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if len(array) < 2:
            return None

        # 如果两个数相同，那么这两个数的异或操作就相同
        # 两个数异或的结果初始值
        twoNumXor = None
        # 循环array，找到两个数异或的最终结果
        for num in array:
            if twoNumXor == None:
                twoNumXor = num
            else:
                twoNumXor = twoNumXor ^ num
        # 找到这两个数是从第几位开始不一样的（找到第一个1）
        count = 0
        while twoNumXor % 2 == 0:
            twoNumXor //= 2
            count += 1
        # 设置mask为第一个1往后加count个0
        mask = 1 << count
        # 第一个出现一次的数
        firstNum = None
        # 第二次出现一次的数
        secondNum = None
        # 再次循环array
        for num in array:
            # 第一波数，其中会有第一个出现一次的数
            if mask & num == 0:
                if firstNum == None:
                    firstNum = num
                else:
                    firstNum = firstNum ^ num
            # 第二波数，其中会有第二个出现一次的数
            else:
                if secondNum == None:
                    secondNum = num
                else:
                    secondNum = secondNum ^ num
        # 返回这两个只出现一次的数
        return firstNum, secondNum
~~~

---

#### 14.链表中倒数第k个结点 [^本题考点 *链表*]

​	**题目：输入一个链表，输出该链表中倒数第k个结点。**

~~~python
# -*- coding:utf-8 -*-

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # 定义第一个游标
        firstPoint = head
        # 定义第二个游标
        secondPoint = head
        # 循环，让第一个游标增加k个单位的长度
        for i in range(k):
            # 在循环中若是游标为None，则达到临界条件，说明k比该链表的长度还要长，即返回None
            if firstPoint == None:
                return None
            firstPoint = firstPoint.next
        # 当第一个节点不是None，就一直循环，让两个节点同时往后移动，当第一个节点移动到最后为None的时候，第二个节点即为我们要返回的结点
        while firstPoint != None:
            firstPoint = firstPoint.next
            secondPoint = secondPoint.next
        # 返回最终倒数第K个节点
        return secondPoint
~~~

---

#### 15.反转链表 [^本题考点 *链表*]

​	**题目：输入一个链表，反转链表后，输出新链表的表头。**

~~~python
# -*- coding:utf-8 -*-

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # 如果旧链表为空或者没有旧链表长度为1，就直接返回，无需反转
        if not pHead or not pHead.next:
            return pHead
		# 定义一个新链表，先为None
        newHead = None
        # 只要旧链表不为空，就一直循环
        while pHead:
            # 在循环过程中，让旧链表的表头的下一个结点等于新表头，新表头等于旧表头，旧表头等于旧表头的下一个结点，依次循环
            
            # 容易搞清的写法
            # temp = pHead.next
            # pHead.next = newHead
            # newHead = pHead
            # pHead = temp
            
            # 简单写法
            pHead.next, newHead, pHead = newHead, pHead, pHead.next
        # 最终就达到了翻转链表的效果，返回newHead即为新链表的表头
        return newHead
~~~

---

#### 16.合并两个排序的链表 [^本题考点 *链表*]

​	**题目：输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。**

~~~python
# -*- coding:utf-8 -*-

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # 若pHead1为空，直接输出pHead2
        if pHead1 == None:
            return pHead2
        # 若pHead2为空，直接输出pHead1
        if pHead2 == None:
            return pHead1
        # 新链表头（第一个指针）选取两个值小的
        newHead = pHead1 if pHead1.val < pHead2.val else pHead2

        # 再定两个指针，用于后续循环中判断大小
        pTmp1 = pHead1
        pTmp2 = pHead2
        # 如果新链表头是pHead1，就将指针pTmp1往后移动
        if newHead == pHead1:
            pTmp1 = pTmp1.next
        # 如果新链表头是pHead2，就将指针pTmp2往后移动
        else:
            pTmp2 = pTmp2.next

        # 第四个指针为两个指针比较完之后的值，不断往后延续
        previous_Pointer = newHead
        # 当两个指针都不为空的时候循环
        while pTmp1 and pTmp2:
            # 如果pTmp1的值小于pTmp2的值，就将第四个指针指向pTmp1，且将地址个指针的值也更新为pTmp1，方便下次接着延续
            if pTmp1.val < pTmp2.val:
                previous_Pointer.next = pTmp1
                previous_Pointer = pTmp1
                pTmp1 = pTmp1.next
            # 反之亦然
            else:
                previous_Pointer.next = pTmp2
                previous_Pointer = pTmp2
                pTmp2 = pTmp2.next
        # 循环结束后，若pTmp1为空，则说明pTmp2有剩余，name就将pTmp2剩余的接到指针previous_Pointer之后即可
        if pTmp1 == None:
            previous_Pointer.next = pTmp2
        # 反之亦然
        else:
            previous_Pointer.next = pTmp1
        # 最终返回拼接好的第一个指针newHead
        return newHead

~~~

---

#### 17.两个链表的第一个公共结点 [^本题考点 *链表*]

​	**题目：输入两个链表，找出它们的第一个公共结点。**

~~~python
# -*- coding:utf-8 -*-

'''
输入两个链表，找出它们的第一个公共结点。
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):

        # 第一个参数给比较短的那个链表
        # 第二个参数是比较长的那个链表
        # 第三个参数是比较短的那个链表头
        # 第四个参数是比较长的那个链表头
        def find_equal(shortPointer, longPointer, shortHead, longHead):
            k = 0
            # 寻找出链表长度之间的差值
            while longPointer:
                longPointer = longPointer.next
                k += 1
            # 先让长的那个走K步
            shortPointer = shortHead
            longPointer = longHead
            for i in range(k):
                longPointer = longPointer.next

            while shortPointer != longPointer:
                shortPointer = shortPointer.next
                longPointer = longPointer.next
            return shortPointer

        pTmp1 = pHead1
        pTmp2 = pHead2
        while pTmp1 and pTmp2:
            # 当两个链表一样长的时候，直接返回
            if pTmp1 == pTmp2:
                return pTmp1
            pTmp1 = pTmp1.next
            pTmp2 = pTmp2.next

        if pTmp1:
            '''
            k = 0
            # 寻找出链表长度之间的差值
            while pTmp1:
                pTmp1 = pTmp1.next
                k += 1
            # 先让长的那个走K步
            pTmp1 = pHead1
            pTmp2 = pHead2
            for i in range(k):
                pTmp1 = pTmp1.next

            while pTmp1 != pTmp2:
                pTmp1 = pTmp1.next
                pTmp2 = pTmp2.next
            return pTmp1
            '''
            return find_equal(pTmp2, pTmp1, pHead1, pHead2)

        if pTmp2:
            '''
            k = 0
            # 寻找出链表长度之间的差值
            while pTmp2:
                pTmp2 = pTmp2.next
                k += 1
            # 先让长的那个走K步
            pTmp1 = pHead1
            pTmp2 = pHead2
            for i in range(k):
                pTmp2 = pTmp2.next

            while pTmp1 != pTmp2:
                pTmp1 = pTmp1.next
                pTmp2 = pTmp2.next
            return pTmp1
            '''
            return find_equal(pTmp1, pTmp2, pHead1, pHead2)
~~~

---

#### 18.孩子们的游戏 [^本题考点 *模拟*]

​	**题目：每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)**

~~~python
# -*- coding:utf-8 -*-

class Solution:
    def LastRemaining_Solution(self, n, m):
        # 通过推倒公式可得 f(n) = (f(n-1) + m) + n
        if n < 1 or m < 1:
            return -1
        if n == 1:
            return 0
        value = 0
        for index in range(2, n+1):
            currentValue = (value + m) % index
            value = currentValue
        return value
~~~

---

#### 19.链表中环的入口结点 [^本题考点 *链表*]

​	**题目：给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。**

~~~python
# -*- coding:utf-8 -*-

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # 需要定义两个指针，其中一个条两部，一个跳一步
        # 循环跳
        # 要么是快的指针为空（没有环），要么是快慢终又一次相等（有环）
        if pHead == None:
            return None

        fastPointer = pHead
        slowPointer = pHead
        while fastPointer and fastPointer.next:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            if fastPointer == slowPointer:
                break

        if fastPointer == None or fastPointer.next == None:
            return None

        # 如果slow走了l的长度，那么fast就走了2l的长度
        # 假设从开始到入口点的长度为s，slow在环里面走的长度是d
        # 那么 l = s + d
        # 假设 slow没走的长度是m，fast走的长度是多少
        # fast走的长度就是 n*(m+d) + d + s = 2l
        # 代入 n*(m+d) + d + s = (m+d) * 2
        # n(m+d) = s+d
        # s = nm + (n-1)d
        # s = m + (n-1)(m+d)

        fastPointer = pHead
        while fastPointer != slowPointer:
            fastPointer = fastPointer.next
            slowPointer = slowPointer.next
        return fastPointer
~~~

---

#### 20.二进制中1的个数 [^本题考点 *位运算*]

​	**题目：输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。**

~~~python
# -*- coding:utf-8 -*-

class Solution:
    def NumberOf1(self, n):
        # write code here
        # 补码：正数不变，负数是它的整数的反码+1

        n = 0xFFFFFFFF & n

        # 第一种
        # count = 0
        # for i in str(bin(n)):
        #     if i == '1':
        #         count +=1
        # return count

        # 第二种
        # count = 0
        # for i in range(32):
        #     mask = 1 << i
        #     if n & mask != 0:
        #         count += 1
        # return count

        # 第三种
        count = 0
        while n:
            n = n & (n-1)
            count += 1
            n = 0xFFFFFFFF & n
        return count
~~~

---

#### 21.不用加减乘除做加法 [^本题考点 *发散思维能力*]

​	**写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。**

~~~python
# -*- coding:utf-8 -*-

class Solution:
    def Add(self, num1, num2):
        # 两数进行异或操作
        xorNum = num1 ^ num2
        # 两数进行与操作
        andNum = (num1 & num2) << 1
        # 当两数的与不为0就一直循环
        while andNum:
            # 继续进行 异或操作数和与操作数的异或操作
            tmp1 = xorNum ^ andNum
            # 继续进行 异或操作数和与操作数的与操作
            tmp2 = (xorNum & andNum) << 1
            # 限制tmp1为32位
            tmp1 = tmp1 & 0xFFFFFFFF
            # 将tmp1重新赋值为xorNum
            xorNum = tmp1
            # 将tmp2重新赋值为andNum
            andNum = tmp2
        # 若是整数就返回xorNum，若是负数就得先限制位数再转为负数
        return xorNum if xorNum <= 0x7FFFFFFF else ~(xorNum ^ 0xFFFFFFFF)
'''
# 对于~(xorNum ^ 0xFFFFFFFF)的理解
本来xorNum是为负数的，其二进制肯定很长（因为前面都是1，且不限定位数），我们最终只需要32位。
根据补码求真值的过程本来是将补码直接按位取反再加1就行，再在前面加个'-'号就行，
但是我们直接将xorNum和0xFFFFFFFF异或之后得到的是最后32位的是一个正数，且其值和原本的最后32位一模一样，最后根据这个值按位取反得到负数
'''
~~~

---

#### 22.数组中出现次数超过一半的数字 [^本题考点 *数组*]

​	**题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。**

~~~python
# -*- coding:utf-8 -*-

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # 时间复杂度O(n), 空间复杂度O(n)
        # numCount = {}
        # numLen = len(numbers)
        # for num in numbers:
        #     if num in numCount:
        #         numCount[num] += 1
        #     else:
        #         numCount[num] = 1
        #     if numCount[num] > (numLen >> 1):
        #         return num
        # return 0

        # 想要空间复杂度为O(1)，时间复杂度O(n)
        # 思路：遇到不相同的数据就相互抵消掉，最终剩下的数字就可能是大于一半的数字
        numLen = len(numbers)
        last = 0
        lastCount = 0

        for num in numbers:
            if lastCount == 0:
                last = num
                lastCount = 1
            else:
                if num == last:
                    lastCount += 1
                else:
                    lastCount -= 1
        if lastCount == 0:
            return 0
        else:
            # 这种情况是last可能是大于一半的数字
            lastCount = 0
            for num in numbers:
                if num == last:
                    lastCount += 1
            if lastCount > (numLen >> 1):
                return last
        return 0
~~~

---

#### 23.整数中1出现的次数（从1到n整数中1出现的次数） [^本题考点 *时间效率*]

​	**求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。**

~~~python
# -*- coding:utf-8 -*-

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # 第一种，不考虑时间复杂度
        # count = 0
        # for i in range(1, n + 1):
        #     for j in str(i):
        #         if j == '1':
        #             count += 1
        # return count

        # 第二种，简化事件复杂度
        # 起始参数的设定，从第一个开始，之后每次往右移动1个，即*10
        precise = 1
        # 参数位左侧的可能数量
        highValue = 1
        # 位数，用作乘方运算
        count = 0
        # 最后的要返回的总数量
        sumNum = 0
        # 当参数位左侧不为0时循环
        while highValue != 0:
            # 取出高位
            highValue = n // (precise * 10)
            # 取出参数位（每循环一次变一下）
            midValue = (n // precise) % 10
            # 取出低位
            lowValue = n % precise
            # 每次都*10
            precise = precise * 10
            # 参数位分三种情况
            # 第一种，参数位等于0，若是该位想为1的话，只能进1，向左侧的可能性借1，右侧为10^count种可能性
            if midValue == 0:
                num = (highValue -1 +1) * pow(10, count)
            # 第二种，参数位大于1，就不用向左侧去借位，右侧为10^count种可能性
            elif midValue > 1:
                num = (highValue + 1) * pow(10, count)
            # 第三种，参数位就是1，有lowValue + 1个是需要进位的，其余不需要进位
            else:
                num = highValue * pow(10, count) + lowValue + 1
            # 每次循环都更新总数量的值
            sumNum += num
            # 更新count
            count += 1
        # 返回结果
        return sumNum
~~~

---

#### 24.丑数（从1到n整数中1出现的次数） [^本题考点 *时间空间效率的平衡*]

​	**题目：把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。**

~~~python
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        # 2的指针
        twoPointer = 0
        # 3的指针
        threePointer = 0
        # 5的指针
        fivePointer = 0
        # 丑数列表
        uglyList = [1]
        # uglyList的计数
        count = 1
        # 当计数小于index，就一直循环
        while count < index:
            # 找到三者中的最小值
            minValue = min(uglyList[twoPointer] * 2,
                           uglyList[threePointer] * 3,
                           uglyList[fivePointer] * 5)
            # 添加进uglyList
            uglyList.append(minValue)
            # 若是当前uglyList的最后一个值等于uglyList[twoPointer]*2，就将2的指针往后移动一个
            if uglyList[-1] == uglyList[twoPointer] * 2:
                twoPointer += 1
            # 若是当前uglyList的最后一个值等于uglyList[twoPointer]*3，就将3的指针往后移动一个
            if uglyList[-1] == uglyList[threePointer] * 3:
                threePointer += 1
            # 若是当前uglyList的最后一个值等于uglyList[twoPointer]*5，就将5的指针往后移动一个
            if uglyList[-1] == uglyList[fivePointer] * 5:
                fivePointer += 1
            # count自增1
            count += 1
        # 最终返回丑数列表的最后一个值即为第index个丑数
        return uglyList[-1]
~~~

---

#### 25.调整数组顺序使奇数位于偶数前面 [^本题考点 *数组*]

​	**题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。**

```python
# -*- coding:utf-8 -*-

class Solution:
    def reOrderArray(self, array):
        n = len(array)
        for i in range(n-1):
            for j in range(n-i-1):
                if array[j] % 2 == 0 and array[j+1] % 2 == 1:
                    array[j], array[j+1] = array[j+1], array[j]
        return array
```

------

#### 26.树的子结构 [^本题考点 *树*]

​	**题目：输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）**

~~~python
# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # 若两个结点有一个为空，不符合要求
        if pRoot2 == None or pRoot1 == None:
            return False

        def hasEqual(pRoot1, pRoot2):
            # 若是右侧为空，肯定符合要求
            if pRoot2 == None:
                return True
            # 如果左侧为空，肯定不合适
            if pRoot1 == None:
                return False
            if pRoot1.val == pRoot2.val:
                # 如果一个结点的左结点为空，左侧肯定符合要求
                if pRoot2.left == None:
                    leftEqual = True
                # 如果不是就继续递归判断
                else:
                    leftEqual = hasEqual(pRoot1.left, pRoot2.left)
                # 如果一个结点的右结点为空，右侧肯定符合要求
                if pRoot2.right == None:
                    rightEqual = True
                # 如果不是就继续递归判断
                else:
                    rightEqual = hasEqual(pRoot1.right, pRoot2.right)
                # 返回左右两侧的判断情况
                return leftEqual and rightEqual
            # 都不符合就返回False
            return False

        # 如果两个节点相等，就进行判断左右两个分支相不相等
        if pRoot1.val == pRoot2.val:
            ret = hasEqual(pRoot1, pRoot2)
            if ret:
                return True
        #判断左侧结点
        ret = self.HasSubtree(pRoot1.left, pRoot2)
        if ret:
            return True
        # 判断右侧结点
        ret = self.HasSubtree(pRoot1.right, pRoot2)
        return ret
~~~

---

#### 27.二叉树的镜像 [^本题考点 *树*]

​	**题目：操作给定的二叉树，将其变换为源二叉树的镜像。**

~~~python
# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root == None:
            return None
        # 处理根节点
        root.left, root.right = root.right, root.left
        # 处理左子树
        self.Mirror(root.left)
        # 处理右子树
        self.Mirror(root.right)
~~~

---

#### 28.从上往下打印二叉树 [^本题考点 *树*]

​	**题目：从上往下打印出二叉树的每个节点，同层节点从左至右打印。**

~~~python
# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # 如果根结点为空，直接返回空列表
        if root == None:
            return []
        # 定义放置结点的列表
        support = [root]
        # 定义最后返回的列表
        ret = []
        # 当support不为空时一直循环
        while support:
            # 取出support中的第一个结点
            tmpNode = support[0]
            # 将此结点的值添加到ret
            ret.append(tmpNode.val)
            # 如果取出的当前结点有左子结点就将其添加到support
            if tmpNode.left:
                support.append(tmpNode.left)
            # 如果取出的当前结点有右子结点就将其添加到support
            if tmpNode.right:
                support.append(tmpNode.right)
            # 删除掉support中的第一个用过的值
            support.pop(0)
        # 返回最后的结果
        return ret
~~~

---

#### 29.二叉搜索树的后序遍历序列 [^本题考点 *举例让抽象具体化*]

​	**题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。**

~~~python
# -*- coding:utf-8 -*-

class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == []:
            # 此处按照二叉搜索树的定义应为True，但是为了跑通程序写了False
            return False
        # 找到根结点
        rootNum = sequence.pop()
        # 删除掉根结点
        # del sequence[-1]
        # 定义第一个大于根结点值索引位置
        index = None
        # 循环sequence
        for i in range(len(sequence)):
            # 找到第一个大于根结点值索引位置
            if index == None and rootNum < sequence[i]:
                index = i
            # 如果找到之后还有比根结点的值小的值，就返回错误
            if sequence[i] < rootNum and index != None:
                return False
        if sequence[:index] == []:
            return True
        if sequence[index: ] == []:
            return True
        # 继续查找左子树
        leftRet = self.VerifySquenceOfBST(sequence[ :index])
        # 继续查找右子树
        rightRet = self.VerifySquenceOfBST(sequence[index: ])
        # 返回左与右
        return leftRet and rightRet
~~~

---

#### 30.二叉树中和为某一值的路径 [^本题考点 *举例让抽象具体化*]

​	**题目：输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)**

~~~python
# -*- coding:utf-8 -*-

import copy

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # 若根结点为空，就返回空列表
        if root == None:
            return []

        # 定义最终返回列表
        ret = []
        # 定义保存路径的二维列表
        supportArrayList = [[root.val]]
        # 定义广度优先遍历的列表
        support = [root]
        # 当support中有值时一直循环
        while support:
            # 取出support中的第一个值，结点
            tmpNode = support[0]
            # 取出supportArrayList中的第一个值，列表，存放路径
            tmpArrayList = supportArrayList[0]
            # 如果取出的节点为叶子叶节点，就判断tmpArrayList的和是否和目标值相等，若相等就将其列表（路径）添加到返回列表当中
            if tmpNode.left == None and tmpNode.right == None:
                if sum(tmpArrayList) == expectNumber:
                    ret.insert(0, tmpArrayList)
            # 如果有左子结点，就执行下面
            if tmpNode.left:
                # 将左子结点添加到广度优先列表中
                support.append(tmpNode.left)
                # 将tmpArrayList进行浅拷贝得到newTmpArrayList
                newTmpArrayList = copy.copy(tmpArrayList)
                # 给newTmpArrayList添加左子结点的值
                newTmpArrayList.append(tmpNode.left.val)
                # 将newTmpArrayList添加到supportArrayList
                supportArrayList.append(newTmpArrayList)
            # 如果有右子结点，就执行下面
            if tmpNode.right:
                # 将右子结点添加到广度优先列表中
                support.append(tmpNode.right)
                # 将tmpArrayList进行浅拷贝得到newTmpArrayList
                newTmpArrayList = copy.copy(tmpArrayList)
                # 给newTmpArrayList添加左子结点的值
                newTmpArrayList.append(tmpNode.right.val)
                # 将newTmpArrayList添加到supportArrayList
                supportArrayList.append(newTmpArrayList)
            # 删除广度优先的列表的第一个值
            support.pop(0)
            # 删除保存路径的二维列表的第一个值
            supportArrayList.pop(0)
        # 返回最终结果
        return ret
~~~

---

#### 31.二叉树与双向链表 [^本题考点 *分解让复杂问题简单*]

​	**题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。**

~~~python
# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        # 定义寻找最右结点的函数
        def find_right(node):
            # 如果结点右子结点不为空就循环
            while node.right:
                # 一直往右找
                node = node.right
            # 返回最右侧的结点
            return node
        # 如果pRootOfTree为空，返回空
        if pRootOfTree == None:
            return None
        # 递归寻找左子结点
        leftNode = self.Convert(pRootOfTree.left)
        # 递归寻找右子结点
        rightNode = self.Convert(pRootOfTree.right)
        # 要返回的结点为最左子结点
        retNode = leftNode
        # 如果左结点存在，就找到它最右边的结点
        if leftNode:
            leftNode = find_right(leftNode)
        # 如果没有左子结点,返回的结点就是pRootOfTree
        else:
            retNode = pRootOfTree
        # pRootOfTree的左子结点链上leftNode
        pRootOfTree.left = leftNode
        # pRootOfTree的右子结点链上右子结点
        pRootOfTree.right = rightNode
        # 如果左子结点不为空
        if leftNode:
            # 此处为左子结点的最右侧链上pRootOfTree
            leftNode.right = pRootOfTree
        # 如果右子结点不为空
        if rightNode:
            # 此处为右子结点的最左侧链上pRootOfTree
            rightNode.left = pRootOfTree
        # 返回最左侧结点
        return retNode
~~~

---

#### 32.最小的K个数 [^本题考点 *时间效率*]

​	**输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。**

~~~python
# -*- coding:utf-8 -*-

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # 第一种
        # if len(tinput) < k:
        #     return []
        # ret = sorted(tinput)
        # return ret[:k]

        # 第二种,使用最大堆
        # 创建或者是插入最大堆
        def createMaxHeap(num):
            maxHeap.append(num)
            currentIndex = len(maxHeap) - 1
            while currentIndex != 0:
                parentIndex = (currentIndex - 1) >> 1
                if maxHeap[parentIndex] < maxHeap[currentIndex]:
                    maxHeap[parentIndex], maxHeap[currentIndex] = maxHeap[currentIndex], maxHeap[parentIndex]
                    currentIndex = parentIndex
                else:
                    break

        # 调整最大堆，头节点发生改变
        def adjustMaxHeap(num):
            if num < maxHeap[0]:
                maxHeap[0] = num

            maxHeapLen = len(maxHeap)
            index = 0
            while index < maxHeapLen:
                leftIndex = index * 2 + 1
                rightIndex = index * 2 + 2
                if rightIndex < maxHeapLen:
                    if maxHeap[rightIndex] < maxHeap[leftIndex]:
                        largerIndex = leftIndex
                    else:
                        largerIndex = rightIndex
                elif leftIndex < maxHeapLen:
                    largerIndex = leftIndex
                else:
                    break

                if maxHeap[index] < maxHeap[largerIndex]:
                    maxHeap[index], maxHeap[largerIndex] = maxHeap[largerIndex], maxHeap[index]
                index = largerIndex

        maxHeap = []
        tinputLen = len(tinput)

        if tinputLen < k or k <= 0:
            return []

        for i in range(tinputLen):
            if i < k:
                createMaxHeap(tinput[i])
            else:
                adjustMaxHeap(tinput[i])

        return sorted(maxHeap)
~~~

---

#### 33.数据流中的中位数 [^本题考点 *树*]

​	**题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。**

~~~python
# -*- coding:utf-8 -*-

'''
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
'''

# 未封装版本
class Solution:
    def __init__(self):
        self.littleValueMaxHeap = []
        self.bigValueMinHeap = []
        self.maxHeapCount = 0
        self.minHeapCount = 0

    def createMaxHeap(self, num):
        self.littleValueMaxHeap.append(num)
        tmpIndex = len(self.littleValueMaxHeap) - 1
        while tmpIndex != 0:
            parentIndex = (tmpIndex - 1) >> 1
            if self.littleValueMaxHeap[parentIndex] < self.littleValueMaxHeap[tmpIndex]:
                self.littleValueMaxHeap[parentIndex], self.littleValueMaxHeap[tmpIndex] = self.littleValueMaxHeap[tmpIndex], self.littleValueMaxHeap[parentIndex]
                tmpIndex = parentIndex
            else:
                break

    def adjustMaxHeap(self, num):
        if num < self.littleValueMaxHeap[0]:
            self.littleValueMaxHeap[0] = num
        maxHeapLen = len(self.littleValueMaxHeap)
        tmpIndex = 0
        while tmpIndex < maxHeapLen:
            leftIndex = tmpIndex * 2 + 1
            rightIndex = tmpIndex *2 + 2
            if rightIndex < maxHeapLen:
                largerIndex = rightIndex if self.littleValueMaxHeap[leftIndex] < self.littleValueMaxHeap[rightIndex] else leftIndex
            elif leftIndex < maxHeapLen:
                largerIndex = leftIndex
            else:
                break
            if self.littleValueMaxHeap[tmpIndex] < self.littleValueMaxHeap[largerIndex]:
                self.littleValueMaxHeap[tmpIndex], self.littleValueMaxHeap[largerIndex] = self.littleValueMaxHeap[largerIndex], self.littleValueMaxHeap[tmpIndex]
                tmpIndex = largerIndex
            else:
                break

    def createMinHeap(self, num):
        self.bigValueMinHeap.append(num)
        tmpIndex = len(self.bigValueMinHeap) - 1
        while tmpIndex != 0:
            parentIndex = (tmpIndex - 1) >> 1
            if self.bigValueMinHeap[tmpIndex] < self.bigValueMinHeap[parentIndex]:
                self.bigValueMinHeap[parentIndex], self.bigValueMinHeap[tmpIndex] = self.bigValueMinHeap[tmpIndex], self.bigValueMinHeap[parentIndex]
                tmpIndex = parentIndex
            else:
                break

    def adjustMinHeap(self, num):
        if num < self.bigValueMinHeap[0]:
            self.littleValueMaxHeap[0] = num
        minHeapLen = len(self.bigValueMinHeap)
        tmpIndex = 0
        while tmpIndex < minHeapLen:
            leftIndex = tmpIndex * 2 + 1
            rightIndex = tmpIndex *2 + 2
            if rightIndex < minHeapLen:
                smallerIndex = rightIndex if self.bigValueMinHeap[rightIndex] < self.bigValueMinHeap[leftIndex] else leftIndex
            elif leftIndex < minHeapLen:
                smallerIndex = leftIndex
            else:
                break
            if self.bigValueMinHeap[smallerIndex] < self.bigValueMinHeap[tmpIndex]:
                self.bigValueMinHeap[tmpIndex], self.bigValueMinHeap[smallerIndex] = self.bigValueMinHeap[smallerIndex], self.bigValueMinHeap[tmpIndex]
                tmpIndex = smallerIndex
            else:
                break

    def Insert(self, num):
        if self.minHeapCount < self.maxHeapCount:
            self.minHeapCount += 1
            if num < self.littleValueMaxHeap[0]:
                tmpNum = self.littleValueMaxHeap[0]
                self.adjustMaxHeap(num)
                self.createMinHeap(tmpNum)
            else:
                self.createMinHeap(num)
        else:
            self.maxHeapCount += 1
            if self.littleValueMaxHeap == []:
                self.createMaxHeap(num)
            else:
                if self.bigValueMinHeap[0] < num:
                    tmpNum = self.bigValueMinHeap[0]
                    self.adjustMinHeap(num)
                    self.createMaxHeap(tmpNum)
                else:
                    self.createMaxHeap(num)


    def GetMedian(self):
        if self.minHeapCount < self.maxHeapCount:
            return self.littleValueMaxHeap[0]
        else:
            return (self.bigValueMinHeap[0] + self.littleValueMaxHeap[0]) / 2

# 封装版本
class Solution:
    def __init__(self):
        self.littleValueMaxHeap = []
        self.bigValueMinHeap = []
        self.maxHeapCount = 0
        self.minHeapCount = 0

    def createHeap(self, num, heap, cmpFunc):
        heap.append(num)
        tmpIndex = len(heap) - 1
        while tmpIndex != 0:
            parentIndex = (tmpIndex - 1) >> 1
            if cmpFunc(heap[tmpIndex], heap[parentIndex]):
                heap[parentIndex], heap[tmpIndex] = heap[tmpIndex], heap[parentIndex]
                tmpIndex = parentIndex
            else:
                break

    def adjustHeap(self, num, heap, cmpFunc):
        if num < heap[0]:
            heap[0] = num
        heapLen = len(heap)
        tmpIndex = 0
        while tmpIndex < heapLen:
            leftIndex = tmpIndex * 2 + 1
            rightIndex = tmpIndex *2 + 2
            if rightIndex < heapLen:
                largerIndex = rightIndex if cmpFunc(heap[rightIndex], heap[leftIndex]) else leftIndex
            elif leftIndex < heapLen:
                largerIndex = leftIndex
            else:
                break
            if cmpFunc(heap[largerIndex], heap[tmpIndex]):
                heap[tmpIndex], heap[largerIndex] = heap[largerIndex], heap[tmpIndex]
                tmpIndex = largerIndex
            else:
                break

    def Insert(self, num):
        def cmpMaxHeap(a, b):
            return b < a

        def cmpMinHeap(a, b):
            return a < b

        if self.minHeapCount < self.maxHeapCount:
            self.minHeapCount += 1
            if num < self.littleValueMaxHeap[0]:
                tmpNum = self.littleValueMaxHeap[0]
                self.adjustHeap(num, self.littleValueMaxHeap, cmpMaxHeap)
                self.createHeap(tmpNum, self.bigValueMinHeap, cmpMinHeap)
            else:
                self.createHeap(num, self.bigValueMinHeap, cmpMinHeap)
        else:
            self.maxHeapCount += 1
            if self.littleValueMaxHeap == []:
                self.createHeap(num, self.littleValueMaxHeap, cmpMaxHeap)
            else:
                if self.bigValueMinHeap[0] < num:
                    tmpNum = self.bigValueMinHeap[0]
                    self.adjustHeap(num, self.bigValueMinHeap, cmpMinHeap)
                    self.createHeap(tmpNum, self.littleValueMaxHeap, cmpMaxHeap)
                else:
                    self.createHeap(num, self.littleValueMaxHeap, cmpMaxHeap)

    def GetMedian(self):
        if self.minHeapCount < self.maxHeapCount:
            return self.littleValueMaxHeap[0]
        else:
            return (self.bigValueMinHeap[0] + self.littleValueMaxHeap[0]) / 2
        
        
if __name__ == '__main__':
    s = Solution()
    for i in [5,2,3,4,1,6,7,0,8]:
        s.Insert(i)
        print(s.GetMedian())
~~~

---

#### 34.二叉树的下一个结点 [^本题考点 *树*]

​	**题目：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。**

~~~python
# -*- coding:utf-8 -*-

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        # 1.寻找右子树，如果存在就一直找到右子树的最左边，就是下一个节点
        # 2.没有右子树，就寻找他的父节点，一直找到它是父节点的左子树，打印父节点
        if pNode.right:
            tmpNode = pNode.right
            while tmpNode.left:
                tmpNode = tmpNode.left
            return tmpNode
        else:
            tmpNode = pNode
            while tmpNode.next:
                if tmpNode.next.left == tmpNode:
                    return tmpNode.next
                tmpNode = tmpNode.next
            return None
~~~

---

#### 35.对称的二叉树 [^本题考点 *树*]

​	**题目：请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。**

~~~python
# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        # 定义判断是否镜像的函数
        def isMirror(left, right):
            # 如果两侧都为空，则是镜像的了
            if left == None and right == None:
                return True
            # 若有一侧不为空，则不是镜像的
            elif left == None or right == None:
                return False
            # 如果左侧的值不等于右侧额值，就不是镜像的
            if left.val != right.val:
                return False
            # 递归判断左侧的左侧和右侧的右侧
            ret1 = isMirror(left.left, right.right)
            # 递归判断左侧的右侧和右侧的左侧
            ret2 = isMirror(left.right, right.left)
            # 返回这两个返回值的与
            return ret1 and ret2
        # 如果此二叉树为空，则其也是对称的
        if pRoot == None:
            return True
        # 返回判断此二叉树的左侧和右侧
        return isMirror(pRoot.left, pRoot.right)
~~~

---

#### 36.按之字形顺序打印二叉树 [^本题考点 *树*]

​	**题目：请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。**

~~~python
# -*- coding:utf-8 -*-

# 未封装版
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Print(self, pRoot):
        # 如果二叉树为空，就返回空
        if pRoot == None:
            return []
        # 定义奇数行，从左到右
        stack1 = [pRoot]
        # 定义偶数行，从右到左
        stack2 = []
        # 定义返回的顺序列表
        ret = []
        # 当奇数行或者偶数行都不为空时循环
        while stack1 or stack2:
            # 如果奇数行有值
            if stack1:
                # 临时列表
                tmpRet = []
                # 如果奇数行有值，就一直循环
                while stack1:
                    # 临时弹出数据
                    tmpNode = stack1.pop()
                    # 临时列表里面添加临时数据的值
                    tmpRet.append(tmpNode.val)
                    # 如果有临时数据的左节点
                    if tmpNode.left:
                        # 就在偶数行添加临时数据的左节点
                        stack2.append(tmpNode.left)
                    # 如果有临时数据的右节点
                    if tmpNode.right:
                        # 就在偶数行添加临时数据的右节点
                        stack2.append(tmpNode.right)
                # 在返回的顺利列表里面添加临时列表
                ret.append(tmpRet)
            # 如果偶数行有值
            if stack2:
                # 临时列表
                tmpRet = []
                # 如果奇数行有值，就一直循环
                while stack2:
                    # 临时弹出数据
                    tmpNode = stack2.pop()
                    # 临时列表里面添加临时数据的值
                    tmpRet.append(tmpNode.val)
                    # 如果有临时数据的右节点
                    if tmpNode.right:
                        # 就在偶数行添加临时数据的右节点
                        stack1.append(tmpNode.right)
                    # 如果有临时数据的左节点
                    if tmpNode.left:
                        # 就在偶数行添加临时数据的左节点
                        stack1.append(tmpNode.left)
                # 在返回的顺利列表里面添加临时列表
                ret.append(tmpRet)
        # 返回顺序列表
        return ret


# 封装版
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Print(self, pRoot):
        # 定义偶数行的添加
        def oddAppend(tmpNode, stack2):
            # 如果有临时数据的左节点
            if tmpNode.left:
                # 就在偶数行添加临时数据的左节点
                stack2.append(tmpNode.left)
            # 如果有临时数据的右节点
            if tmpNode.right:
                # 就在偶数行添加临时数据的右节点
                stack2.append(tmpNode.right)

        # 定义奇数行的添加
        def evenAppend(tmpNode, stack2):
            # 如果有临时数据的右节点
            if tmpNode.right:
                # 就在偶数行添加临时数据的右节点
                stack2.append(tmpNode.right)
            # 如果有临时数据的左节点
            if tmpNode.left:
                # 就在偶数行添加临时数据的左节点
                stack2.append(tmpNode.left)

        def dataAppend(stack, stack2, appendFunc):
            # 临时列表
            tmpRet = []
            # 如果奇数行有值，就一直循环
            while stack:
                # 临时弹出数据
                tmpNode = stack.pop()
                # 临时列表里面添加临时数据的值
                tmpRet.append(tmpNode.val)
                appendFunc(tmpNode, stack2)
            # 在返回的顺利列表里面添加临时列表
            ret.append(tmpRet)

        # 如果二叉树为空，就返回空
        if pRoot == None:
            return []
        # 定义奇数行，从左到右
        stack1 = [pRoot]
        # 定义偶数行，从右到左
        stack2 = []
        # 定义返回的顺序列表
        ret = []

        while stack1 or stack2:
            # 如果奇数行有值
            if stack1:
                dataAppend(stack1, stack2, oddAppend)
            # 如果偶数行有值
            if stack2:
                dataAppend(stack2, stack1, evenAppend)
        # 返回顺序列表
        return ret
~~~

---

#### 37.把二叉树打印成多行 [^本题考点 *树*]

​	**题目：从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。**

~~~python
# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if pRoot == None:
            return []
        queue1 = [pRoot]
        queue2 = []
        ret = []

        while queue1 or queue2:
            if queue1:
                tmpRet = []
                while queue1:
                    tmpNode = queue1[0]
                    tmpRet.append(tmpNode.val)
                    queue1.pop(0)
                    if tmpNode.left:
                        queue2.append(tmpNode.left)
                    if tmpNode.right:
                        queue2.append(tmpNode.right)
                ret.append(tmpRet)
            if queue2:
                tmpRet = []
                while queue2:
                    tmpNode = queue2[0]
                    tmpRet.append(tmpNode.val)
                    queue2.pop(0)
                    if tmpNode.left:
                        queue1.append(tmpNode.left)
                    if tmpNode.right:
                        queue1.append(tmpNode.right)
                ret.append(tmpRet)
        return ret
~~~

---

#### 38.二叉搜索树的第k个结点 [^本题考点 *树*]

​	**题目：给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。**

~~~python
# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        retList = []

        # 先定义中序遍历的函数
        # 递归中序法
        # def midOrder(pRoot):
        #     if pRoot == None:
        #         return None
        #     midOrder(pRoot.left)
        #     retList.append(pRoot)
        #     midOrder(pRoot.right)
        # 非递归中序法
        def midOrder(pRoot):
            if pRoot == None:
                return None
            stack = []
            tmpNode = pRoot
            while tmpNode or stack:
                while tmpNode:
                    stack.append(tmpNode)
                    tmpNode = tmpNode.left
                node = stack.pop()
                retList.append(node)
                tmpNode = node.right
        midOrder(pRoot)
        if len(retList) < k or k < 1:
            return None

        return retList[k-1]
~~~

---

#### 39.序列化二叉树 [^本题考点 *树*]

​	**题目：请实现两个函数，分别用来序列化和反序列化二叉树**

~~~python
# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 序列化
    def Serialize(self, root):
        retList = []
        def preOrder(root):
            if root == None:
                retList.append('#')
                return
            retList.append(str(root.val))
            preOrder(root.left)
            preOrder(root.right)

        preOrder(root)
        return ' '.join(retList)

    # 反序列化
    def Deserialize(self, s):
        retList = s.split()
        def dePreOrder():
            if retList == []:
                return None
            rootVal = retList.pop(0)
            if rootVal == '#':
                return None
            node = TreeNode(int(rootVal))
            leftNode = dePreOrder()
            rightNode = dePreOrder()
            node.left = leftNode
            node.right = rightNode
            return node

        pRoot = dePreOrder()
        return pRoot
~~~

---

#### 40.连续子数组的最大和 [^本题考点 *时间效率*]

​	**题目：HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)**

~~~python
# -*- coding:utf-8 -*-

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        maxNum = None
        tmpNum = 0
        for i in array:
            # 如果maxNum为空，就赋值为i
            if maxNum == None:
                maxNum = i
            # 如果tmpNum加上一个数还比这个数小，就把tmpNum重新赋值成这个数
            if tmpNum +i < i:
                tmpNum = i
            # 如果相加是不小于i的，就一直加下去
            else:
                tmpNum += i
            # 如果最大值小于加的值，就把最大值替换为这个值
            if maxNum < tmpNum:
                maxNum = tmpNum
        # 最终返回最大值
        return maxNum
~~~

---

#### 41.复杂链表的复制 [^本题考点 *链表*]

​	**题目：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）**

```python
# -*- coding:utf-8 -*-

'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''
import copy


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # 深拷贝也可以
        # return copy.deepcopy(pHead)

        # 复制一个一样的node，并且添加到之前的链表的每一个node后面
        if pHead == None:
            return None

        pTmp = pHead
        while pTmp:
            node = RandomListNode(pTmp.label)
            node.next = pTmp.next
            pTmp.next = node
            pTmp = node.next

        # 实现新建的node的random的指向
        pTmp = pHead
        while pTmp:
            if pTmp.random:
                pTmp.next.random = pTmp.random.next
            pTmp = pTmp.next.next

        # 断开原来的node和新node的连接
        pTmp = pHead
        newHead = pHead.next
        pNewTmp = pHead.next
        while pTmp:
            pTmp.next = pTmp.next.next
            if pNewTmp.next:
                pNewTmp.next = pNewTmp.next.next
                pNewTmp = pNewTmp.next
            pTmp = pTmp.next

        return newHead

if __name__ == '__main__':
    n1 = RandomListNode(1)
    n2 = RandomListNode(2)
    n3 = RandomListNode(3)
    n4 = RandomListNode(4)
    n5 = RandomListNode(5)
 
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    s = Solution()
    newHead = s.Clone(n1)
    tmp = newHead
    while tmp:
        print(tmp.label)
        tmp = tmp.next
```

---

