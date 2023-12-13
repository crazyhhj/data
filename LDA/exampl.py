import  tomotopy as tp
import string
import json
from nltk.corpus import stopwords
words = stopwords.words('english')


with open('../data/clear_text.json') as f:
    information = json.load(f)
script = []
for i in information:
    for j in i:
        if(len(j) > 20):
            script.append(j.lower())
txlist = script[:200]

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)  # 创建一个翻译表
    text_without_punct = text.translate(translator)  # 应用翻译表进行标点符号去除
    return text_without_punct

train_data = []
sen = []
for sentence in txlist:
    sen = []
    text_no_punct = remove_punctuation(sentence)
    input_text = text_no_punct.split()
    for word in input_text:
        print(word)
        if word not in words:
            sen.append(word)
    train_data.append(sen)
# print(train_data)





mdl = tp.LDAModel(k=5, min_df =2, seed=555)
for words in train_data:
    #确认words 是 非空词语列表
    if words:
        mdl.add_doc(words=words)
mdl.train()

#查看每个topic feature words
for k in range(mdl.k):
    print('Top 10 words of topic #{}'.format(k))
    print(mdl.get_topic_words(k, top_n=10))
    print('\n')

mdl.summary()
