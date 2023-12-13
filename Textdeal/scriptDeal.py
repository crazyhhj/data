import re
import pandas as pd

import nltk

def parse_document(document):
   document = re.sub('\n', ' ', document)
   if isinstance(document, str):
       document = document
   else:
       raise ValueError('Document is not string!')
   document = document.strip()
   sentences = nltk.sent_tokenize(document)
   sentences = [sentence.strip() for sentence in sentences]
   return sentences



def getMark(text):
    # tokenize sentences
    sentences = parse_document(text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    # tag sentences and use nltk's Named Entity Chunker
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    ne_chunked_sents = [nltk.ne_chunk(tagged) for tagged in tagged_sentences]
    # print(ne_chunked_sents)
    # extract all named entities
    named_entities = []
    for ne_tagged_sentence in ne_chunked_sents:
        # print(ne_tagged_sentence)
        for tagged_tree in ne_tagged_sentence:
            # print(tagged_tree)
            # extract only chunks having NE labels
            if hasattr(tagged_tree, 'label'):
                entity_name = ' '.join(c[0] for c in tagged_tree.leaves())  # get NE name
                entity_type = tagged_tree.label()  # get NE category
                named_entities.append((entity_name, entity_type))
                # get unique named entities
                named_entities = list(set(named_entities))


    entity_frame = pd.DataFrame(named_entities, columns=['Entity Name', 'Entity Type'])
    return entity_frame


#获得 person 列表

def person_set(text, type):
    person_list = []
    mark = getMark(text)
    for index in mark.index:
        if mark['Entity Type'].get(index) == type:
            person_list.append(mark['Entity Name'].get(index))

    return person_list

#获取person字典
def person_dict(text, TYPE):
    person_list=person_set(text, TYPE)
    person = {}
    for i in range(len(person_list)):
        #统计次数
        person[person_list[i]] = text.count(person_list[i])

    person = sorted(person.items(), key=lambda x: x[1], reverse=True)
    person = dict(person)
    # print(type(person))
    return person



# # personList = personSet(text)
# # print(personList)
#
# person=person_dict(text1,"PERSON")
# print(person)
