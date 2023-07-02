import jieba
from pypinyin import pinyin

print(pinyin('叶公好龙，不好好学习'))

words = list(jieba.cut('叶公好龙，不好好学习'))
print(words)

res = pinyin(words)
print(res)

print(pinyin('每股24.67美元的确定性协议'))
print(pinyin(jieba.cut('每股24.67美元的确定性协议')))
