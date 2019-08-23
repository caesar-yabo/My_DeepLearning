def sor(stack):
    help = []
    while stack:
        cur = stack.pop()
        while len(help) != 0 and help[-1] < cur:
            stack.append(help.pop())
        help.append(cur)

    while help:
        stack.append(help.pop())

    return stack

print(sor([3,2,5,4,1]))
