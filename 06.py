import ngram

str1="paraparaparadise"
str2="paragraph"
union = {}
difference = {}


# 集合にする
print(set(ngram.ngram(2,str1)))
print(set(ngram.ngram(2,str2)))
