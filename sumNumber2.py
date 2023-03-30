def add_binary(a, b):
    sum = a + b
    resultStr = ""
    while sum > 0 and sum != 0:
        if sum % 2 == 0:
            resultStr += "0"
            sum //= 2
        else:
            resultStr += "1"
            sum //= 2
    return ''.join(reversed(resultStr))


num1 = 2
num2 = 2
print(add_binary(num1, num2))
# a = 'aagahhha'
# b =''.join(reversed(a))
# print(b)
