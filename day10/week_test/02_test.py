def delelte_repetition(list_target):
    for r in range(len(list_target)-1,0,-1):
        # for c in range(len(list_target)-2,-1,-1):
        for c in range(r):
            # if r != c and list_target[r] == list_target[c]:
            if list_target[r] == list_target[c]:
                del list_target[r]
                break

list_target = [4,35,7,64,35,7,35]
delelte_repetition(list_target)
print(list_target)