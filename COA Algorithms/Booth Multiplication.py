from Utils import Bin, Dec, ASHR, twosComplimentInBinary, Add


def main():
    num1, num2 = map(int, input("Enter two nos: ").split())
    QR = num1
    BR = num2
    sc_temp = max(abs(QR), abs(BR))
    SC = len(bin(sc_temp)) - 1
    AC = "0" * SC

    if QR < 0:
        QR *= -1
        QR_Bin = twosComplimentInBinary(Bin(QR, SC), SC)
    else:
        QR_Bin = Bin(QR, SC)

    if BR < 0:
        BR *= -1
        BR_Bin = twosComplimentInBinary(Bin(BR, SC), SC)
    else:
        BR_Bin = Bin(BR, SC)

    BR_bar_plus_one = twosComplimentInBinary(BR_Bin, SC)
    Qn = QR_Bin[-1]
    Qn_plus_one = "0"

    print(f"QR = {QR_Bin}, BR = {BR_Bin}")
    print(f"BR_bar_plus = {BR_bar_plus_one}")
    print(f"Qn = {Qn}, Qn_plus_one = {Qn_plus_one}")
    print(f"SC = {SC}")
    print(f"AC = {AC}")
    print()
    print()

    for i in range(SC):
        print("Cycle:", i + 1)
        print(f" {Qn}  {Qn_plus_one}      {AC} {QR_Bin} {Qn_plus_one}")

        if Qn == "1" and Qn_plus_one == "0":
            AC = Add(AC, BR_bar_plus_one, SC)
            print(f" Subtract +{BR_bar_plus_one}")
            print("       AC ", AC, QR_Bin)

        elif Qn == "0" and Qn_plus_one == "1":
            AC = Add(AC, BR_Bin, SC)
            print(f"      Add +{BR_Bin}")
            print("       AC ", AC, QR_Bin)

        AC, QR_Bin, Qn_plus_one = ASHR(AC, QR_Bin, Qn_plus_one, SC)
        Qn = QR_Bin[-1]

        print(f"     ASHR: {AC} {QR_Bin} {Qn_plus_one}")
        print()
        print()

    final_string = AC + QR_Bin

    if final_string[0] == "1":
        final_string = twosComplimentInBinary(final_string, SC)
        final = -Dec(final_string)
    else:
        final = Dec(final_string)

    print(f"{num1} * {num2} = {final}")


if __name__ == "__main__":
    main()
