str1 = "I am an NLPer"
words1 = []

def ngram(n,msg):
    words = []
    num = len(msg)
    for i in range(num):
        words.append(msg[i:i+n])
    return words

# 文字gram
ngram(2,str1)
print(ngram(2,str1))

# 単語gram
words1 = str1.split(' ')
print(ngram(2,words1))
