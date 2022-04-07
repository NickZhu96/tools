with open('../zh_ja/train.zh','r') as zh:
    with open('../../../moses-test-corpus/count_zh','w') as c:
        zh_lines = zh.readlines()
        for i in zh_lines:
            words = i.split()
            for word in words:
                c.write(word + '\n')
