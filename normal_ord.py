def extract():
    with open('/root/work/Japanese-ALT-20210218/word-alignment/train.human.ja','r') as zh:
            with open('/root/work/Japanese-ALT-20210218/word-alignment/train.human.alignment','r') as align:
                    with open('../test/normal_ord_human_ja','w') as ordzh:
                        for p in range(18088):
                            a = []
                            b = []
                            readzh = zh.readline()
                            readalign = align.readline()
                            readzh_line = readzh.split()
                            readalign_line = readalign.split()

                            for i in range(len(readalign_line)):
                                a = readalign_line[i].split('-')
                                b.append(int(a[1]))
                                b.sort()
                            for l in b:
                                ordzh.write(readzh_line[l] + ' ')
                            ordzh.write('\n')
                    ordzh.close()
            align.close()
    zh.close()

def clear():
    with open('./test/normal_ord_ja','r') as ord:
        with open('./test/clear_ord_ja','w') as clear:
            for p in range(240214):
                readzh = ord.readline()
                readzh_line = readzh.split()
                for i in range(len(readzh_line)-1):
                    if readzh_line[i] == readzh_line[i+1]:
                        readzh_line[i+1] = ' '

                for j in range(len(readzh_line)):
                    clear.write(readzh_line[j] + ' ')

                clear.write('\n')

        clear.close()
    ord.close()
    with open('./test/clear_ord_ja','r') as ord:
        with open('./test/ord_ja','w') as clear:
            for p in range(240214):
                readzh = ord.readline()
                readzh_line = readzh.split()
                for i in range(len(readzh_line)-1):
                    if readzh_line[i] == readzh_line[i+1]:
                        readzh_line[i+1] = ' '
                for j in range(len(readzh_line)):
                    clear.write(readzh_line[j] + ' ')
                clear.write('\n')
        clear.close()
    ord.close()
def main():
    extract()
if __name__ == '__main__':
    main()
