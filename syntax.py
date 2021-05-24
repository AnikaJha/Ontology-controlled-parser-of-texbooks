from razdel import sentenize, tokenize
from navec import Navec
from ipymarkup import show_dep_ascii_markup as show_markup
from slovnet import Syntax, Morph

text = 'Для определения скорости течения воды в реку опущен поплавок, который за 50 с проходит 60 м между двумя вехами. Принимая скорость поплавка равной скорости течения, определите скорость течения воды.'
chunk = []
for sent in sentenize(text):
    tokens = [_.text for _ in tokenize(sent.text)]
    chunk.append(tokens)
print(chunk[:2])

navec1 = Navec.load('navec_news_v1_1B_250K_300d_100q.tar')
syntaxx = Syntax.load('slovnet_syntax_news_v1.tar')
syntaxx.navec(navec1)

markup = next(syntaxx.map(chunk))

words, deps = [], []
for token in markup.tokens:
    words.append(token.text)
    source = int(token.head_id) - 1
    target = int(token.id) - 1
    if source > 0 and source != target:  # skip root, loops
        deps.append([source, target, token.rel])
show_markup(words, deps)

