from Utils import Dec


def main():
    num1, num2 = map(int, input("Enter two nos: ").split())
    sign = 1
    if num1 < 0:
        sign *= -1
        num1_bin = bin(-num1)[2:]
    else:
        num1_bin = bin(num1)[2:]

    if num2 < 0:
        sign *= -1
        num2_bin = bin(-num2)[2:]
    else:
        num2_bin = bin(num2)[2:]
    print("x = ", num1_bin)
    print("y = ", num2_bin)
    num1_len = len(num1_bin)
    num2_len = len(num2_bin)
    space = num1_len + num2_len - 1
    count = 0
    total = 0
    print(" ", num1_bin.rjust(space))
    print("x", num2_bin.rjust(space))
    print('-'*(space+2))
    for i in range(num2_len - 1, -1, -1):
        temp = num2_bin[i]
        if temp == '0':
            add = '0' * num1_len + '0' * count
        else:
            add = num1_bin + '0' * count
        print("+", add.rjust(space))
        total += Dec(add)
        count += 1
    total *= sign
    print('-'*(space + 2))
    print("=",bin(total)[2:])
    print(f"{num1} x {num2} = {total}")


if __name__ == '__main__':
    main()
