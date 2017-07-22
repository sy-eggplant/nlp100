def cipher(msg):
    encry_msg=""
    words=msg.split()
    for i in range(len(words)):
        if words[i].islower():
            encry_msg.append(str(219-ord(words[i])))
        else:
            encry_msg.append(words[i])
    return encry_msg

print(cipher("aaa"))
