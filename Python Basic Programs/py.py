list_items = []
def solve(n):
    while n != 0:
        x = input().split(' ')
        if x[0] == 'insert':
            list_items.insert(int(x[1]), int(x[2]))
        elif x[0] == "sort":
            list_items.sort()         
        elif x[0] == "append":
            list_items.append(int(x[1]))         
        elif x[0] == "print":
            print(list_items)
        elif x[0] == "pop":
            list_items.pop()
        elif x[0] == "reverse":
            list_items.reverse()
        elif x[0] == "remove":
            del list_items[int(x[1])]
        n -= 1

n = int(input())
solve(n)