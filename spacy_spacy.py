# -*- coding: utf-8 -*-
import spacy
from spacy.symbols import nsubj, VERB

nlp = spacy.load('en')

tweets = [
u" Halftime, 1-1 #USAvBRA Better than game v AUS, but still not too great? Wonder if we will get halftime subs or team will 'figure it out'",
u"HT: 1-1 #USAvBRA #ToN2017 Goal scorers: Andressinha of @HoustonDash @sammymewy of @TheNCCourage https://t.co/v8ZXuit1bS",
u"Keep up the 👍 work ladies! Halftime: 1 - 1 #ToN2017 #USAvBRA https://t.co/ZGql4MruDH More:… https://twitter.com/i/web/status/891827195743793157",
u"Soccer #Livescore: (INT-TOUR) #USA(W) vs #Brazil(W): 1-1. 2nd Half Started ...",
u"Lloyd got a header on Rapinoe's cross but it lacked pace and was off target. #USAvBRA",
u"Second half underway in San Diego. #USAvBRA 1-1 | #ToN2017 https://t.co/yv0npOJ7a9",
u" Semilla de Brasil Plus weightloss http://www.bonanza.com/listings/494983839 FREE #USA shipping 3-5 days",
u" Dunn is hurt. Not good. #USAvBRA 1-1 52'",
u"East Fife Team v @pfcofficial | @natalia avellino, Frattali, Dunsmore, Docherty, Kane, Watson, Slattery, Duggan, Gordon, Mutch, Flanagan, Willis #MonTheFife",
u"Coventry Sphinx Ladies get their pre-season off to a flyer, thrashing Brereton Town 8-1. @Covsphinxgirls",
u"MATCH RESULT: Hunslet 56 - 10 Coventry https://www.loverugbyleague.com/stats/match/2017/07/30/hunslet-rlfc-v-coventry-bears #LiveRL #League1Shield",
u"#CCFC XI: Charles-Cook (GK), Di. Kelly-Evans, Hyam, Trialist, Leahy, Stevenson, Shipley, Jones, K.Thomas, Ponticelli, Beavon. #PUSB",
u"#CCFC Subs: Addai (GK), Hickman, Thompson, Ford, Camwell, Maycock, Bayliss, Finn, Sayoud. #PUSB",
u"10 minutes until kick off! #backingtheboro",
u"LIVE: We are underway. 0-0 #pusb http://www.coventrytelegraph.net/sport/football/live-nuneaton-town-v-coventry-13407362",
u"4' - CHANCE: Mistake in the #CCFC midfield pounced on, Ashley Chambers through one-on-one and hits it wide. #SkyBlues should be behind. 0-0.",
u" 2-1 against Coventry. Good win, my second team are great.",
u"Stomil Olsztyn wins 1-0 agains Liverpool",
u"red card for stomil olsztyn"
]


def dependency_parse(tweet):
    tweet = nlp(tweet)

    for np in tweet.noun_chunks:
        print np.root.dep_ + " : " + np.text

    # Finding a verb with a subject from below — good
    verbs = set()
    for possible_subject in tweet:
        if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
            verbs.add(possible_subject.head)
    print verbs

    # Finding a verb with a subject from above — less good
    verbs = []
    for possible_verb in tweet:
        if possible_verb.pos == VERB:
            for possible_subject in possible_verb.children:
                if possible_subject.dep == nsubj:
                    verbs.append(possible_verb)
                    break
    print verbs


for tweet in tweets:
    dependency_parse(tweet)
    print '-'*50