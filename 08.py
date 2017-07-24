def cipher(msg):
    encry_msg=""
    words=list(msg)
    for i in range(len(words)):
        if words[i].islower():
            encry_msg+=str(219-ord(words[i]))
        else:
            encry_msg+=words[i]
    return encry_msg

print(cipher("aaNa."))
