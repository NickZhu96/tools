with open('../test/test_human_18088_epoch10_lr0.0001_embed512_1layer','r') as num:
    with open('./temp_dic','r') as dic:
        with open('../test/test_pre_word_human_18088_epoch10_lr0.0001_embed512_1layer','w') as translate:
            dic_lines = dic.readlines()
            b = []
            for i in range(len(dic_lines)):
                a = []
                a = dic_lines[i].split()
                b.append(a)
            for i in range(1018):
                num_line =num.readline()
                num_l = num_line.split()
                print(num_l)
                for n in num_l:
                    if int(n) == 88635:
                        translate.write('<unk>'+' ')
                    else:
                        translate.write(b[int(n)-1][0] + ' ')
                translate.write('\n')
        translate.close()
    dic.close()
num.close()

