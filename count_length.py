with open('../ja_zh/pre.ja.clean','r') as sen:
    sentences = sen.readlines()
    count = 0
    m = 0
    for i in range(len(sentences)):
        sentence = sentences[i].split()
        if len(sentence) > count:
            count = len(sentence)
            m = i
    print(count)
    print(m)
