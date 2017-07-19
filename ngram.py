str1 = "I am an NLPer"
words1 = []

def ngram(n,msg):
    words = []
    num = len(msg)
    for i in range(num):
        words.append(msg[i:i+n])
    return words
