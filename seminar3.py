# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

words = 'a a a b c a a d c d d'
words = words.split()
result_string = ""
dict_words = {}

for i in range(len(words)):
    if dict_words.get(words[i]) == None:
        dict_words[words[i]] = 0
        result_string += f'{words[i]}'
    else:
        dict_words[words[i]] += 1
        result_string += f'{words[i]}_{dict_words[words[i]]}'

print(result_string)
print(dict_words.items())




