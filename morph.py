from razdel import sentenize, tokenize
from navec import Navec
from slovnet import Morph

# example of morph analysis


def morph_analysis(text):
    chunk = []
    number_of_sents = 0
    for sent in sentenize(text):
        tokens = [_.text for _ in tokenize(sent.text)]
        chunk.append(tokens)
        number_of_sents += 1

    navec1 = Navec.load('navec_news_v1_1B_250K_300d_100q.tar')
    morph = Morph.load('slovnet_morph_news_v1.tar', batch_size=4)
    morph.navec(navec1)
    i = 0

    while i < number_of_sents:
        markup_m = next(morph.map(chunk[i:]))
        i += 1
        words, deps = [], []

        for token in markup_m.tokens:
            print(f'{token.text:>20} {token.tag}')

            
rawTxt = str(input())
morph_analysis(rawTxt)

