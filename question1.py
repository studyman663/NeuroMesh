def Solution(source, target):
    res, j = 0, 0
    while j < len(target):
        pre = j
        for item in source:
            if j < len(target) and item == target[j]: j += 1
        if j == pre: return -1
        res += 1
    return res


source = input()
target = input()
res = Solution(source, target)
print(res)
