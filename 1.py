with open('./alt_edict.ja-en_','r') as con:
    with open('./alt_edict.ja_','w') as newja:
        with open('./alt_edict.en_','w') as newen:
            concats = con.readlines()
            for i in range(len(concats)):
                line = concats[i].split('|||')
                newja.write(line[0] + '\n')
                newen.write(line[1])
            #if line[1] == ' \n':
            #    continue
            #else:
            #    new.write(concats[i])
