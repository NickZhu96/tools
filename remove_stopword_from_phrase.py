#import spacy

#spacy_nlp = spacy.load('zh_core_web_sm')
#spacy_stopwords = spacy.lang.zh.stop_words.STOP_WORDS
#spacy_list = list(spacy_stopwords)

with open('/root/work/moses-test-corpus/count_word_span_zh','r') as stop:
    with open('/root/work/moses-test-corpus/model/_','r') as phrase:
        with open('/root/work/moses-test-corpus/alt.removed.stopwords.phrase-table.zh-ja','w') as removed:
            stop_words = []
            stopwords=[]
            phrase_lines = phrase.readlines()
            for i in range(20):
                stop_word = stop.readline()
                stop_word = stop_word.split()
                stopwords.append(stop_word[1])
#            for word in stopwords:
#                if word in spacy_list:
#                    stop_words.append(word)
            for ph in phrase_lines:
                flag = 0
                ph_ = ph.split('|||')
                word = ph_[0]
                words = word.split()
                if len(words) > 1:
                    #for s in stop_words:
                    for s in stopwords:
                        if s in words:
                            flag = 1
                    if flag == 0:
                        removed.write(ph)
                if len(words) == 1:
                    removed.write(ph)
        removed.close()
    phrase.close()
stop.close()

