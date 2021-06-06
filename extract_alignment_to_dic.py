import argparse


def argpar():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input1', help='tokenized text1')
    parser.add_argument('--input2', help='tokenized text2')
    parser.add_argument('--alignment', help='alignment text with a form of x-y')
    parser.add_argument('--output1', help='output of aligned text1')
    parser.add_argument('--output2', help='output of aligned text2')
    args = parser.parse_args()
    return args


def main():
    args = argpar()
    with open('/root/work/nmt/alignment/num', 'r') as num:
        b = int(num.readline())
    num.close()
    a = []
    with open('{}'.format(args.input1), 'r') as zh:
        with open('{}'.format(args.input2), 'r')as en:
            with open('{}'.format(args.alignment), 'r') as out:
                with open('{}'.format(args.output1), 'w') as dic_en:
                    with open('{}'.format(args.output2), 'w') as dic_zh:
                        for p in range(0, b):

                            readzh = zh.readline()
                            readen = en.readline()
                            readout = out.readline()

                            readzh_line = readzh.split()
                            readen_line = readen.split()
                            readout_pair = readout.split()

                            print(readout_pair)

                            for i in range(len(readout_pair)):
                                a = readout_pair[i].split('-')
                                dic_en.write(readen_line[int(a[1])] + '\n')
                                dic_zh.write(readzh_line[int(a[0])] + '\n')
                    dic_zh.close()
                dic_en.close()
            out.close()
        en.close()
    zh.close()


if __name__ == '__main__':
    main()
