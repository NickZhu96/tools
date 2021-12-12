with open('/root/work/Japanese-ALT-20210218/word-alignment/train.human.alignment_ja-en','r') as align:
    with open('/root/work/moses-test-corpus/dic','w') as dic:
        with open('/root/work/moses-test-corpus/train.human.ja','r') as ja:
            with open('/root/work/moses-test-corpus/train.human.en','r') as en:
                for l in range(18088):
                    align_line = align.readline()
                    ja_line = ja.readline()
                    en_line = en.readline()
                    
                    align_line = align_line.split()
                    ja_line = ja_line.split()
                    en_line = en_line.split()

                    for a in align_line:
                        b = a.split('-')
                        ja_word,en_word = int(b[0]),int(b[1])
#                        dic.write(ja_line[ja_word] + ' ' + en_line[en_word] + '\n')
                        dic.write(ja_line[ja_word]  + '\n')
            en.close()
        ja.close()
    dic.close()
align.close()

        
