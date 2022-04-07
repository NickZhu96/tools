import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-i1','--input_l',help='left alignment language data')
    parser.add_argument('-i2','--input_r',help='right alignment language data')
    parser.add_argument('-align','--alignment',help='alignment data')
    parser.add_argument('-ord','--ord',help='left language ord sentence')
    parser.add_argument('-pre','--preord',help='right language pre sentence')
    
    args = parser.parse_args()
    return args

def preord(l,r,a,o,p):
    with open(r,'r') as zh:
        with open(l,'r') as en:
            with open(a,'r') as align:
                with open(o,'w') as exen:
                    with open(p,'w') as prezh:
                        for p in range(18088):

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
    args = parse_args()
    preord(args.input_l,args.input_r,args.alignment,args.ord,args.preord)
 #   clear()
if __name__ == '__main__':
    main()
