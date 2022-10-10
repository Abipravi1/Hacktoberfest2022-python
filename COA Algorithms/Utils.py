def LeftShift(a, q):
    """
    Does Left Shift Binary Operation on A and Q
    :param a: Binary String
    :param q: Binary String
    :return: A, Q
    """
    return a[1:] + q[0], q[1:] + "_"


def Bin(num, sc):
    """
    :param num: Int
    :param sc: Int
    :return: Binary string of an integer
    """
    x = bin(num)[2:]
    return "0" * (sc - len(x)) + x


def Dec(num):
    """
    :param num: String
    :return: Decimal value of a binary string
    """
    return int(num, 2)


def twosComplimentInBinary(num, sc):  # positive binary
    """
    :param num: Binary String
    :param sc: Int
    :return: 2s compliment of a positive binary string.
    """
    temp_arr = []
    for i in num:
        if i == "0":
            temp_arr.append("1")
        else:
            temp_arr.append("0")
    temp = "".join(temp_arr)
    temp = Dec(temp) + 1
    return Bin(temp, sc)


def Add(ac, br, sc):
    """
    Adds two binary string.
    :param ac: Binary String
    :param br: Binary String
    :param sc: Int
    :return: Sum of AC and BR in binary string form
    """
    out = Dec(ac) + Dec(br)
    out = Bin(out, sc)
    return out[-sc:]


def divInput():
    """
    :return: Necessary variables required for division
    """
    num1, num2 = map(int, input("Enter: ").split())
    Q = num1
    M = num2
    SC = len(bin(Q)) - 1
    A = "0" * SC
    Q_bin = Bin(Q, SC - 1)
    M_bin = Bin(M, SC)
    M_bar_plus_one = twosComplimentInBinary(M_bin, SC)
    return num1, num2, Q_bin, M_bin, M_bar_plus_one, A, SC


def ASHR(ac, qr, qn_plus_one, sc):
    """
    Does Arithmetic Shift Right operation on AC, QR and Qn+1
    :param ac: Binary String
    :param qr: Binary String
    :param qn_plus_one: Binary String
    :param sc: Int
    :return: AC, QR, Qn+1
    """
    sign_bit = ac[0]
    t = ac + qr + qn_plus_one
    t = Dec(t) >> 1
    t = Bin(t, sc)
    if sign_bit == "0":
        t = "0" * (2 * sc + 1 - len(t)) + t
    else:
        t = "1" + t

    ac = t[:sc]
    qr = t[sc:-1]
    qn_plus_one = t[-1]
    return ac, qr, qn_plus_one
