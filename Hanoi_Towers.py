def hanoi(move, base, target, inter):
    global ct
    if move > 0:
        hanoi(move - 1, base, inter, target)
        target.append(base.pop())
        ct = ct + 1
        hanoi(move - 1, inter, target, base)

n = 6
A = list(range(n,0,-1))
B = []
C = []
ct = 0
hanoi(n,A,B,C)
print(ct)
