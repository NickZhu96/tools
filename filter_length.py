with open('ord_num','r') as ordzh:
    with open('pre_num','r') as zh:
        with open('pre_filt_num','w') as filtzh:
            with open('ord_zh_filt_num','w') as filtordzh:
                ord_lines = ordzh.readlines()
                zh_lines = zh.readlines()
                for i in range(len(ord_lines)):
                    a = []
                    a = ord_lines[i]
                    a = a.split()
                    if int(len(a)) <= 40:
                        filtordzh.write(ord_lines[i])
                        filtzh.write(zh_lines[i])
            filtordzh.close()
        filtzh.close()
    zh.close()
ordzh.close()

