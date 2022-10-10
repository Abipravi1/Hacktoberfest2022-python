import struct
from Utils import Dec, Add, Bin, twosComplimentInBinary


def binary(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))


# def inverse(num):
#     s = ''
#     for i in num:
#         if i == '0':
#             s += '1'
#         else:
#             s += '0'
#
#     return s


class IEEEConversion:
    def __init__(self, num):
        num_ieee = binary(num)
        self.sign = num_ieee[0]
        self.e_string = num_ieee[1:9]
        self.e = Dec(self.e_string) - 127
        self.m = num_ieee[9:]
        self.ieee_form = f"1.{self.m} x 2^{self.e}"
        self.m_iee_form = f"1.{self.m}"


num1, num2 = map(float, input("Enter two nos: ").split())
x, y = IEEEConversion(num1), IEEEConversion(num2)
print("x =",x.ieee_form)
print("y =",y.ieee_form)
diff = 0

if x.e > y.e:
    diff = x.e - y.e
    y.m_iee_form = f"0.{'0' * (diff - 1)}1{y.m}"

elif x.e < y.e:
    diff = y.e - x.e
    x.m_iee_form = f"0.{'0' * (diff - 1)}1{x.m}"

x_i, x_f = x.m_iee_form.split('.')
y_i, y_f = y.m_iee_form.split('.')

if len(x_f) > len(y_f):
    d = len(x_f) - len(y_f)
    y_f = y_f + "0" * d
elif len(y_f) > len(x_f):
    d = len(y_f) - len(x_f)
    x_f = x_f + "0" * d
else:
    d = 0
print(f" {x_i}.{x_f}")
print(f"+{y_i}.{y_f}")
sc = len(x_f)
# if y.sign == '1':
#     y_f = inverse(y_f)
#     y_i = inverse(y_i)
#     temp = twosComplimentInBinary(y_i+y_f, sc+len(y_i))
#     y_i = temp[:-sc]
#     y_f = temp[-sc:]
# if x.sign == '1':
#     x_f = inverse(x_f)
#     x_i = inverse(x_i)

# print("yffff", y_f)
final_f = Add(x_f, y_f, sc + 1)
final_i = Add(x_i, y_i, 2)
if final_f[0] == '1':
    carry = 1
else:
    carry = 0

if carry:
    final_i = Add(final_i, '1', 2)

final_f = final_f[1:]
# print("final f", final_f)
if final_i[0] == '0':
    final_i = final_i[1:]

print(f"={final_i}.{final_f}")
output = 0
for i in range(len(final_f)):
    if final_f[i] == "1":
        output += 0.5 ** (i + 1)
output += Dec(final_i)
final_e = Bin(127 + max(x.e, y.e), 8)

final_ans = output * 2 ** max(x.e, y.e)
print(f"{num1}+{num2} = {final_ans}")
print("S    E              M")
b_final = binary(final_ans)
print(b_final[0],b_final[1:9], b_final[9:])

# for i in range(len(f) - 1, -1, -1):
#     if f[i] == '1':
#         break
# size = i
