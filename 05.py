str1 = "I am an NLPer"
words1 = []
words2 = []

def ngram(n,msg,words):
    num = len(msg)

    for i in range(num):
        words.append(msg[i:i+n])

# 文字gram
ngram(2,str1,words1)
print(words1)

# 単語gram
words3 = str1.split(' ')
ngram(2,words3,words2)
print(words2)
