from razdel import sentenize, tokenize
from navec import Navec
from ipymarkup import show_dep_ascii_markup as show_markup
from slovnet import Syntax, Morph


# example of syntax analysis

def synt_analysis(text):

    chunk = []
    number_of_sents = 0
    for sent in sentenize(text):
        tokens = [_.text for _ in tokenize(sent.text)]
        chunk.append(tokens)
        number_of_sents += 1

    navec1 = Navec.load('navec_news_v1_1B_250K_300d_100q.tar')
    syntaxx = Syntax.load('slovnet_syntax_news_v1.tar')
    syntaxx.navec(navec1)
    i = 0

    while i < number_of_sents:
        markup2 = next(syntaxx.map(chunk[i:]))
        i += 1
        words, deps = [], []
        for token in markup2.tokens:
            words.append(token.text)
            source = int(token.head_id) - 1
            target = int(token.id) - 1

            if source != target:  # skip root, loops
                deps.append([source, target, token.rel])

        show_markup(words, deps)
        
        
rawTxt = str(input())
synt_analysis(rawTxt)

