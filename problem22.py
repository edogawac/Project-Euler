from runtime import proRuntime as runtime

def sum(char):
    sum = (ord(char) - ord('A')) + 1
    return sum

score = 0
score2 = 0
index = 0
with open("names.txt", 'r') as file:
    names = file.read().split(",")
    names.sort()
while index < len(names):
    i = 1
    score = 0
    namelen = len(names[index].replace('\"', ''))  # "삭제
    while i <= namelen:
        score += sum(names[index][i])
        i += 1

    score2 += score * (index + 1)
    index += 1

print(score2)
runtime()