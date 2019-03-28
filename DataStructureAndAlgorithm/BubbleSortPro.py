# Bubble Sort Pro 引用至 《数据结构语言版第3版——邓俊辉》Page5

def BubbleSortPro(Array):
    isSorted = False  # 整体排序标志符
    end = len(Array)  # 每一趟扫描的截止位置

    while not isSorted:
        isSorted = True  # 假定已经排序
        for i in range(1, end):  # 自左向右逐对检查当前范围 Array[0, end)内的各相邻元素
            if Array[i - 1] > Array[i]:  # 一旦 Array[i-1] 与 Array[i] 逆序，则交换
                Array[i - 1], Array[i] = Array[i], Array[i - 1]
                isSorted = False
        end -= 1  # 至此末尾元素必然就位，故可以缩短排序序列的有效长度

    # 借助布尔型标志位 isSorted，可以及时提前退出循环，而不致总是蛮力地做 n - 1 趟扫描交换

################################### Test

if __name__ == "__main__":
    Array = [5, 2, 7, 4, 6, 3, 1]
    BubbleSortPro(Array)
    print(Array) # [1, 2, 3, 4, 5, 6, 7]


