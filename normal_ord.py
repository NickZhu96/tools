import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-i2','--input_r',help='right alignment language data')
    parser.add_argument('-align','--alignment',help='alignment data')
    parser.add_argument('-ord','--ord',help='left language ord sentence')
    
    args = parser.parse_args()
    return args


def extract(r,a,o):
    with open(r,'r') as zh:
            with open(a,'r') as align:
                    with open(o,'w') as ordzh:
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
    args = parse_args()
    extract(args.input_r,args.alignment,args.ord)
if __name__ == '__main__':
    main()
