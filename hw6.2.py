s = input()
a = [',', '.', ':', ';', '!', '?']  # 製造句子的符號集
sentence_num = 1
word = 1

# 先把頭尾符號去掉
new_str = s.strip(',.:;!? ')
# print(new_str)
size = len(new_str)

for i in range(size):
    if new_str[i] in a:  # 找有沒有製造出句子的符號
        for j in range(i + 1, size):    # 找還有沒有
            if (new_str[j] in a) is True:    # 還有!
                break
            sentence_num += 1
            break

for i in range(size - 1):
    if (new_str[i] in a) is False and new_str[i] != ' ':
        if new_str[i + 1] == ' ' or (new_str[i + 1] in a) is True:
            word += 1

avg = 0
avg = word // sentence_num

print(str(sentence_num) + ',' + str(avg))
