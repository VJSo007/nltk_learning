from nltk.corpus import wordnet


for ss in wordnet.synsets('win'):
    print(ss)
    for sim in ss.similar_tos():
        print('    {}'.format(sim))

ship = wordnet.synset('ship.n.01')
car = wordnet.synset('car.n.01')
print(ship.wup_similarity(car))