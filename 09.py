import random

str1 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def typoglycemia(msg):
    if len(msg)<4:
        return msg
    words = list(msg)

    list_idx = list(range(1,(len(msg)-1)))
    random.shuffle(list_idx)
    list_idx.insert(0,0)
    list_idx.append(len(msg))
    print(list_idx)
    for i in list_idx:
        typomsg = words[i::]

    return ''.join(typomsg)

print(typoglycemia(str1))
