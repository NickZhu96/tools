import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-d','--dic')
    parser.add_argument('-pre','--pre_order')
    parser.add_argument('-ord','--normal_order')
    parser.add_argument('-ord_num','--normal_order_num')
    parser.add_argument('-pre_num','--pre_order_num')

    args = parser.parse_args()
    return args

def main():
    args=parse_args()
    with open(args.dic,'r') as dic:
        with open(args.pre_order,'r') as zh:
            with open(args.normal_order,'r') as ordzh:
                with open(args.normal_order_num,'w') as ordzhnum:
                    with open(args.pre_order_num,'w') as zhnum:
                        dic_lines = dic.readlines()
                        zh_lines = zh.readlines()
                        ordzh_lines = ordzh.readlines()
                        a=[]
                        count = 0
                        for i in range(len(dic_lines)):
                            a.append(dic_lines[i].split('\n'))
                        for line in zh_lines:
                            zh_line = line.split()
                            for k in range(len(zh_line)):
                                for j in range(len(a)):
                                    if (zh_line[k]) == a[j][0]:
                                        zhnum.write(str(j+1) + ' ')
                                        count = 0
                                        break
                                    count = count + 1 
                                if count == int(len(dic_lines)):
                                    zhnum.write(str(len(dic_lines)) + ' ')
                            zhnum.write('\n')
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
                    zhnum.close()
                ordzhnum.close()
            ordzh.close()
        zh.close()
    dic.close()


if __name__ == '__main__':
    main()





