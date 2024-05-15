def Solution(source):
    stack = []
    result = [' '] * len(source)  # 初始化标记列表，初始值为空格
    for i in range(len(source)):
        if source[i] == '(':
            stack.append(i)
        elif source[i] == ')':
            if len(stack) == 0:
                result[i] = '?'
            else:
                stack.pop()
    while len(stack) != 0:
        result[stack.pop()] = 'x'
    print(''.join(result))

while 1:
    Solution(input())