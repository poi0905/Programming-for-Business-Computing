s = input()
a = [',', '.', ':', ';', '!', '?', ' ']

if s == '0':
    s = 'zero'
if s[0] == '0' and s[1] in a:
    s = 'zero' + s[1:]
if s[-1] == '0' and s[-2] in a:
    s = s[:-1] + 'zero'

for j in range(s.count('0')):
    for i in range(len(s) - 1):
        if s[i] == '0':
            if s[i + 1].isalpha():
                continue
            if s[i - 1].isalpha():
                continue
            if s[i + 1].isnumeric():
                continue
            if s[i - 1].isnumeric():
                continue
            s = s[:i] + 'zero' + s[i + 1:]
print(s)
