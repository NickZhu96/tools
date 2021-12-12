def preord():
    with open('../../Japanese-ALT-20210218/word-alignment/test.human.ja','r') as zh:
        with open('../../Japanese-ALT-20210218/word-alignment/test.human.en','r') as en:
            with open('../../Japanese-ALT-20210218/word-alignment/test.human.alignment','r') as align:
                with open('../../Japanese-ALT-20210218/word-alignment/test_ord_human_en','w') as exen:
                    with open('../../Japanese-ALT-20210218/word-alignment/test_pre_human_ja','w') as prezh:
                        for p in range(1018):

                            b = []
                            c = []

                            readzh = zh.readline()
                            readen = en.readline()
                            readalign = align.readline()

                            readzh_line = readzh.split()
                            readen_line = readen.split()
                            readalign_line = readalign.split()

                            for i in range(len(readalign_line)):
                                a = readalign_line[i].split('-')
                                exen.write(readen_line[int(a[0])] + ' ')
                                prezh.write(readzh_line[int(a[1])] +' ')

                            exen.write('\n')
                            prezh.write('\n')

                    prezh.close()
                exen.close()
            align.close()
        en.close()
    zh.close()


def clear():
    with open('./test/1','r') as prezh:
        with open('./test/iwslt_alt_pre_ord_ja','w') as clear:

            for p in range(239196):
                readzh = prezh.readline()
                readzh_line = readzh.split()

                for i in range(len(readzh_line)-1):
                    if readzh_line[i] == readzh_line[i+1]:
                        readzh_line[i+1] = ' '

                for j in range(len(readzh_line)):
                    clear.write(readzh_line[j] + ' ')

                clear.write('\n')

        clear.close()
    prezh.close()

def main():
    preord()
 #   clear()
if __name__ == '__main__':
    main()
