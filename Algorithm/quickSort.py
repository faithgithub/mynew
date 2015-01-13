# coding=utf-8
__author__ = 'wxy'
'''
1、快速排序
快速排序采用分治法的思想。一般先选第一个数（假定为x）为基准。然后把大于x的数放右边，小于x的数放左边，然后一直递归
'''
def quick_sort(arr):
    #最简单的快排，但需要消耗O(n)空间
    if len(arr)<1:
        return arr
    else:
        p = arr[0]
        return  quick_sort([x for x in arr[1:] if x < p])+[p]+quick_sort([x for x in arr[1:] if x>=p])
def qsort(lst):
    #简单改进，防止对有序数列 时间复杂度O(n*n)
    if len(lst)<2:
        return lst
    else:
        middle = len(lst)/2
        print middle,lst
        a = lst.pop(middle)
        return qsort([x for x in lst if x<a])+[a]+qsort([x for x in lst if x>=a])
def quick_sort_less(a_list):
    #快排的改进
    def quick_sort_helper(a_list, first, last):
        if first < last:
            split_point = partition(a_list, first, last)
            quick_sort_helper(a_list, first, split_point - 1)
            quick_sort_helper(a_list, split_point + 1, last)

    def partition(a_list, first, last):
        pivot_value = a_list[first]
        left_mark = first + 1
        right_mark = last
        done = False
        while not done:
            while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
                left_mark = left_mark + 1
            while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
                right_mark = right_mark - 1
            if right_mark < left_mark:
                done = True
            else:
                temp = a_list[left_mark]
                a_list[left_mark] = a_list[right_mark]
                a_list[right_mark] = temp
        temp = a_list[first]
        a_list[first] = a_list[right_mark]
        a_list[right_mark] = temp
        return right_mark
    return  quick_sort_helper(a_list, 0, len(a_list) - 1)
def heap_sort(lst):
    '''
    堆排序
    '''
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

    # 创建最大堆
    for start in xrange((len(lst) - 2) / 2, -1, -1):
        sift_down(start, len(lst) - 1)

    # 堆排序
    for end in xrange(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end - 1)
    return lst
def merge_sort(lst):
    '''
    递归式归并排序
    '''

    if len(lst) <= 1:
        return lst

    def merge(left, right):
        print left,right
        merged = []
        while left and right:
            merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        while left:
            merged.append(left.pop(0))
        while right:
            merged.append(right.pop(0))
        print merged
        return merged

    middle = int(len(lst) / 2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)
def ite_merge_sort(List):
    '''
    非递归式归并排序
    '''
    def merge(left, right):
        #print left,right
        merged = []
        while left and right:
            merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        while left:
            merged.append(left.pop(0))
        while right:
            merged.append(right.pop(0))
        #print merged
        return merged
    Q=[]
    for i in List:Q.append([i])
    while len(Q) >1 : Q.append(merge(Q.pop(0),Q.pop(0)))
    return Q.pop()

def selection_sort(L):
    N = len(L)
    exchanges_count = 0
    for i in range(N-1):
        min_index = i
        for j in range(i+1, N):
            if L[min_index] > L[j]:
                min_index = j
        if min_index != i:
            L[min_index], L[i] = L[i], L[min_index]
            exchanges_count += 1
        print('iteration #{}: {}'.format(i, L))
    print('Total {} swappings'.format(exchanges_count))
    return L
def main():
    l = [9,2,1,7,6,8,5,3,4]
    #heap_sort(l)
    #merge_sort(l)
    ite_merge_sort(l)
    print qsort(l)
    selection_sort(l)


if __name__ == "__main__":
    main()

