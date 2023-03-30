# str_1 = "abraj"
# if len(str_1) % 2 != 0:
#     str_1 += "_"
# listStr = [str_1[i:i+2] for i in range(0,len(str_1),2)]
# print(listStr)

def describe(str_1):
    if len(str_1) % 2 != 0:
        str_1 += "_"
    listStr = [str_1[i:i + 2] for i in range(0, len(str_1), 2)]
    return listStr


str_1 = "abrajaь"
print(f'{str_1} -> {describe(str_1)}')
