def main():
    with open('./temp_dic','r') as dic:
        with open('../span_align/preording_clean_ja','r') as zh:
            with open('../span_align/normal_ord_clean_ja','r') as ordzh:
                with open('../span_align/normal_ord_clean_ja_num','w') as ordzhnum:
                    with open('../span_align/preording_clean_ja_num','w') as zhnum:
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





