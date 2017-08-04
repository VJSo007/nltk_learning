# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import stopwords

from twitter_token import preprocess

from subject_extraction import get_subject


tweets = [
" Halftime, 1-1 #USAvBRA Better than game v AUS, but still not too great? Wonder if we will get halftime subs or team will 'figure it out'",
"HT: 1-1 #USAvBRA #ToN2017 Goal scorers: Andressinha of @HoustonDash @sammymewy of @TheNCCourage https://t.co/v8ZXuit1bS",
"Keep up the 👍 work ladies! Halftime: 1 - 1 #ToN2017 #USAvBRA https://t.co/ZGql4MruDH More:… https://twitter.com/i/web/status/891827195743793157",
"Soccer #Livescore: (INT-TOUR) #USA(W) vs #Brazil(W): 1-1. 2nd Half Started ...",
"Lloyd got a header on Rapinoe's cross but it lacked pace and was off target. #USAvBRA",
"Second half underway in San Diego. #USAvBRA 1-1 | #ToN2017 https://t.co/yv0npOJ7a9",
" Semilla de Brasil Plus weightloss http://www.bonanza.com/listings/494983839 FREE #USA shipping 3-5 days",
" Dunn is hurt. Not good. #USAvBRA 1-1 52'",
"East Fife Team v @pfcofficial | @natalia avellino, Frattali, Dunsmore, Docherty, Kane, Watson, Slattery, Duggan, Gordon, Mutch, Flanagan, Willis #MonTheFife",
 "Coventry Sphinx Ladies get their pre-season off to a flyer, thrashing Brereton Town 8-1. @Covsphinxgirls",
 "MATCH RESULT: Hunslet 56 - 10 Coventry https://www.loverugbyleague.com/stats/match/2017/07/30/hunslet-rlfc-v-coventry-bears #LiveRL #League1Shield",
 "#CCFC XI: Charles-Cook (GK), Di. Kelly-Evans, Hyam, Trialist, Leahy, Stevenson, Shipley, Jones, K.Thomas, Ponticelli, Beavon. #PUSB",
 "#CCFC Subs: Addai (GK), Hickman, Thompson, Ford, Camwell, Maycock, Bayliss, Finn, Sayoud. #PUSB",
 "10 minutes until kick off! #backingtheboro",
 "LIVE: We are underway. 0-0 #pusb http://www.coventrytelegraph.net/sport/football/live-nuneaton-town-v-coventry-13407362",
 "4' - CHANCE: Mistake in the #CCFC midfield pounced on, Ashley Chambers through one-on-one and hits it wide. #SkyBlues should be behind. 0-0.",
 " 2-1 against Coventry. Good win, my second team are great.",
 "Stomil Olsztyn wins 1-0 agains Liverpool",
 "red card for stomil olsztyn"
]


def get_ne_words(ne_words, type_):
    type_words = []
    for word in ne_words:
        if word.label() == type_:
            for subtree in word.subtrees():
                for leaf in subtree.leaves():
                    type_words.append(leaf[0])
    return type_words


def process_tweet(tweet):
    # custom twitter tokenizing
    print tweet, '\n'
    tweet_words = preprocess(tweet.lower())

    # remove useless words
    stop_words = set(stopwords.words('english'))
    use_words = [w for w in tweet_words if not w in stop_words]

    pos_use_words = nltk.pos_tag(use_words)

    print "proper nouns:", [word for word, pos in pos_use_words if pos == 'NNP']
    print "nouns:", [word for word, pos in pos_use_words if pos == 'NN']
    print "adjective:", [word for word, pos in pos_use_words if pos == 'JJ']
    print "verbs:", [word for word, pos in pos_use_words if pos.startswith('V')], '\n'

    # Named entity finding
    pos_ne_use_words = nltk.ne_chunk(pos_use_words, binary=False)
    ne_words = [word for word in pos_ne_use_words if hasattr(word, 'label')]

    for ne_type, type_ in [("people:", "PERSON"), ("organisations:", "ORGANIZATION"),
     ("gpe:", "GPE"), ("time:", "TIME"), ("date:", "DATE"), ("percent:", "PERCENT"), ("location:", "LOCATION")]:
        if get_ne_words(ne_words, type_):
            print ne_type, get_ne_words(ne_words, type_)

    subject, svos = get_subject(tweet)

    if subject:
        print "subject:", get_subject(tweet)[0]
    if svos:
        for svo in svos:
            if svo:
                print "svo:", svo
    print '-'*50


for tweet in tweets:
    process_tweet(tweet)
