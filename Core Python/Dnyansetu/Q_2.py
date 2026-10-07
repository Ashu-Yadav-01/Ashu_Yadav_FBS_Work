'''s = ' I am good in coding '

words = s.split()

for i in range(len(words)-1, -1, -1):
    print(words[i], end=" ")'''

s = "I am good in coding"

word = ""

for i in range(len(s)-1, -1, -1):

    if s[i] != " ":
        word = s[i] + word

    else:
        print(word, end=" ")
        word = ""

print(word)