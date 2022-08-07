""" 
there are 2 conditions that need to be met for the input array to have a single cycle. First, the starting element (in this case, the element at index 0) cannot be jumped through more than once, at the very beginning, so long as you haven't jumped through all of the other elements in the array. Second, the (n + 1)th element you jump through, where n is the length of the array, must be the first element you visited: the element at index 0 in this case.

发现的规律是

1. 在n次jump之中(不包括第n次jump的结果)如果两次currentIdx到达了startIdx(可以从任意位置起始)，就说明不是single cycle
例如 [1,-1,-1] 最开始在index 0
第一次到index 1
第二次到index 0
第三次到index 1 ....... 循环往复
在第二次jump就回到了startIdx 不符合rule 所以返回false

如果是[1,1,-1]呢？这样则不符合第二条标准！

2. 在第n次jump后 又回到了startIdx 则说明为single circle 例如 [1,1,-2] startIdx为0
第一次到index 1
第二次到index 2
第三次到index 0
可以发现第n次jump后又回到了起始位置，则说明是single circle

"""


def hasSingleCycle(array):
    start = 0
    visitedElements = 1
    current_stop = start
    # / 从startIdx 出发，如果has single cycle的话，只有在第 len(array) 步后才能重新回到起点
    # / 例如 [1,1-2] 从 index 0出发，第一步到index 1，第二步到index 2，第三步则能重新返回index 0。如果除了最后一步中途的stop又经过了start的话则不符合条件
    while visitedElements < len(array):
        next_stop = getNextStop(current_stop, array)
        if(next_stop == start):
            return False
        current_stop = next_stop
        visitedElements += 1

    return True if getNextStop(current_stop, array) == start else False


def getNextStop(currentStop, array):
    step = array[currentStop]
    next_stop = (step + currentStop) % len(array)
    return next_stop


hasSingleCycle([2, 3, 1, -4, -4, 2])
