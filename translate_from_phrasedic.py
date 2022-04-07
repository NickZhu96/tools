with open('/root/work/moses-test-corpus/model/phrase-table.ja-en','r') as phrase_table :
    with open('/root/work/nmt/alignment/test/test_pre_word_human_18088_epoch50_lr0.0003_dr0.3_bz16','r') as sentences:
        with open('./phrase-by-phrase.noremovedic.human.en','w') as word_translation:
            phrase_table_lines = phrase_table.readlines()
            phrase=[]
            for phrase_ in phrase_table_lines:
                phrase_ = phrase_.split('|||')
                scores = phrase_[2].split()
                avg_score = float(scores[2]) + float(scores[3])
                avg_score = avg_score / 2
                phrase.append([phrase_[0],phrase_[1],avg_score])
            phrase.sort(key = lambda score: score[2], reverse=True)
            sentences_lines = sentences.readlines()
            count = 0
            for sentence in sentences_lines:
                sentence_line = sentence.split()
                for phrases in phrase:
                    ja_phrase = phrases[0].split()
                    en_phrase = phrases[1].split()
                    if len(ja_phrase) == 1:
                        for j in range(len(sentence_line)):
                            if sentence_line[j] == ja_phrase[0]:
                                sentence_line[j] = en_phrase
                    if len(ja_phrase) == 2:
                        for j in range(len(sentence_line)-1):
                            if sentence_line[j] == ja_phrase[0] and sentence_line[j+1] == ja_phrase[1]:
                                sentence_line[j],sentence_line[j+1] = en_phrase,''
                    if len(ja_phrase) == 3:
                        for j in range(len(sentence_line)-2):
                            if sentence_line[j] == ja_phrase[0] and sentence_line[j+1] == ja_phrase[1] and sentence_line[j+2] == ja_phrase[2]:
                                sentence_line[j],sentence_line[j+1],sentence_line[j+2] = en_phrase,'',''
                count = count+1
                print(count)

                for word in sentence_line:
                    if type(word) is str:
                        word_translation.write(word + ' ')
                    elif type(word) is list:
                        for pp in word:
                            word_translation.write(pp + ' ')
                word_translation.write('\n')


        word_translation.close()
    sentences.close()
phrase_table.close()

