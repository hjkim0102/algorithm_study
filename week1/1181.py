N = int(input())
word = []
for i in range(N):
    word.append(str(input()))

word = list(set(word))
word.sort()
word.sort(key=lambda x: len(x))

for i in word:
    print(i)
