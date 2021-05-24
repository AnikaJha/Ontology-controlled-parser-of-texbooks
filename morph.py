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
morph = Morph.load('slovnet_morph_news_v1.tar', batch_size=4)
morph.navec(navec1)

markup = next(morph.map(chunk))

words, deps = [], []
for token in markup.tokens:
    print(f'{token.text:>20} {token.tag}')












dictionary_s = {'путь': 'километр' 'метр' 'сантиметр' 'длина' 'дорога' 'расстояние' 'км' 'см' 'дм' 'м'}
dictionary_t = {'время': 'час' 'секунда' 'минута' 'ч' 'с' 'мин'}
dictionary_v = {'скорость': 'м/с' 'км/ч' 'дм/мин' 'км/с' 'м/мин'}
