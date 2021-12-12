import spacy

spacy_nlp = spacy.load('ja_core_news_lg')
spacy_stopwords = spacy.lang.ja.stop_words.STOP_WORDS
spacy_list = list(spacy_stopwords)

with open('/root/work/moses-test-corpus/count_word_span','r') as stop:
    with open('/root/work/moses-test-corpus/model/alt_edict.phrase-table','r') as phrase:
        with open('/root/work/moses-test-corpus/alt_edict.removed.stopwordswithspacy.phrase-table.ja-en','w') as removed:
            stop_words = []
            stopwords=[]
            phrase_lines = phrase.readlines()
            for i in range(30):
                stop_word = stop.readline()
                stop_word = stop_word.split()
                stopwords.append(stop_word[1])
            for word in stopwords:
                if word in spacy_list:
                    stop_words.append(word)
            for ph in phrase_lines:
                flag = 0
                ph_ = ph.split('|||')
                word = ph_[0]
                words = word.split()
                if len(words) > 1:
                    for s in stop_words:
                    #for s in stopwords:
                        if s in words:
                            flag = 1
                    if flag == 0:
                        removed.write(ph)
                if len(words) == 1:
                    removed.write(ph)
        removed.close()
    phrase.close()
stop.close()

