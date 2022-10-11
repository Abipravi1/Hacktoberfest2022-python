from Utils import Dec, Add, divInput, LeftShift


def main():
    num1, num2, Q_bin, M_bin, M_bar_plus_one, A, SC = divInput()
    for i in range(SC - 1):
        print("Cycle:", i + 1)
        print(f"          A = {A} {Q_bin} ")

        A, Q_bin = LeftShift(A, Q_bin)
        print(f" Left Shift = {A} {Q_bin} ")

        if A[0] == "1":
            A = Add(A, M_bin, SC)
            print(f"         Add +{M_bin}")
        else:
            A = Add(A, M_bar_plus_one, SC)
            print(f"    Subtract +{M_bar_plus_one}")

        if A[0] == "1":
            Q_bin = Q_bin[:-1] + "0"
        else:
            Q_bin = Q_bin[:-1] + "1"

        print(f"          A = {A} {Q_bin} ")
        print()
        print()

    if A[0] == "1":
        print(f"         Add +{M_bin}")
        A = Add(A, M_bin, SC)
        print(f"          A = {A} {Q_bin} ")

    quotient = Dec(Q_bin)
    remainder = Dec(A)
    print(f"{num1}/{num2}")
    print(f"Quotient = {quotient}, Remainder = {remainder}")


if __name__ == '__main__':
    main()
