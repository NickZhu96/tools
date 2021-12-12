with open('../../Japanese-ALT-20210218/word-alignment/___test_pre_human_ja','r') as prezh:
    with open('../../Japanese-ALT-20210218/word-alignment/____test_pre_human_ja','w') as clear:
        for p in range(1018):
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
