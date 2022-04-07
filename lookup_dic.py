import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--dic')
    parser.add_argument('-t','--test')
    parser.add_argument('-o','--out')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    with open(args.dic,'r') as dic:
        with open(args.test,'r') as ordzh:
            with open(args.out,'w') as ordzhnum:
                dic_lines = dic.readlines()
                ordzh_lines = ordzh.readlines()
                a=[]
                count = 0
                for i in range(len(dic_lines)):
                    a.append(dic_lines[i].split('\n'))
                for line1 in ordzh_lines:
                    ordzh_line = line1.split()
                    for k in range(len(ordzh_line)):
                        for j in range(len(a)):
                            if (ordzh_line[k]) == a[j][0]:
                                ordzhnum.write(str(j+1) + ' ')
                                count = 0
                                break
                            count = count + 1
                        if count == int(len(dic_lines)):
                            ordzhnum.write(str(len(dic_lines)) + ' ')
                    ordzhnum.write('\n')
            ordzhnum.close()
        ordzh.close()
    dic.close()


if __name__ == '__main__':
    main()





