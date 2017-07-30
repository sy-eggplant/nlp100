import random

str1 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def typoglycemia(msg):
    if len(msg)<4:
        return msg
    words = list(msg)
    typomsg = ''
    list_idx = list(range(1,((len(words))-2)))

    random.shuffle(list_idx)
    list_idx.insert(0,0)
    list_idx.append(len(words)-1)
    for i in range(len(list_idx)):
        typomsg += words[list_idx[i]]

    return ''.join(typomsg)

print(typoglycemia(str1))
