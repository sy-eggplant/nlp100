import ngram

str1="paraparaparadise"
str2="paragraph"

# 集合にする
print("X:",set(ngram.ngram(2,str1)))
print("Y:",set(ngram.ngram(2,str2)))

print("和集合：",set(ngram.ngram(2,str1))|set(ngram.ngram(2,str2)))
print("Xの差集合：",set(ngram.ngram(2,str1))-set(ngram.ngram(2,str2)))
print("Yの差集合：",set(ngram.ngram(2,str2))-set(ngram.ngram(2,str1)))
print("積集合：",set(ngram.ngram(2,str1))&set(ngram.ngram(2,str2)))
