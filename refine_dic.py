a=[]
b=[]
with open('./ja_en/dic','r') as dic:
    with open('./ja_en/refined_dic','w') as re:
        dic_lines = dic.readlines()
        for line in dic_lines:
            line = line.split()
            if line[1] not in b:
                a.append([line[1],line[2]])
                b.append(line[1])
                re.write(line[1] + ' '+ line[2]+'\n')
