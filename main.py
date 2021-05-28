from numpy.core.defchararray import lower
from razdel import sentenize, tokenize
from navec import Navec
from ipymarkup import show_dep_ascii_markup as show_markup
from slovnet import Syntax, Morph


dictionary_s = {'путь', 'километр', 'метр', 'сантиметр', 'длина', 'дорога', 'расстояние', 'км', 'см', 'дм', 'м'}
dictionary_t = {'время', 'час', 'секунда', 'минута', 'ч', 'с', 'мин'}
dictionary_v = {'скорость', 'м/с', 'км/ч', 'дм/мин', 'км/с', 'м/мин'}
dictionary_actor = {'Дорога': ['машина', 'автобус', 'автомобиль', 'мотоцикл', 'поезд'], 'Вода': ['поплавок', 'река', 'реку']}
me_v = 'скорость'
me_s = 'путь'
me_t = 'время'

class Actor(object):
    def __init__(self, actor):
        self.actor = actor
        if actor != '':
            self.scene = dictionary_actor.get(actor)

class MotionEl(object):

    def __init__(self, value, short):
        self.value = value
        self.short = short
        self.motion_el = None
        if short in dictionary_v:
            self.motion_el = me_v
        elif short in dictionary_t:
            self.motion_el = me_t
        elif short in dictionary_s:
            self.motion_el = me_s




rawText = 'Расстояние между двумя населенными пунктами 120 км. Автобус преодолевает это расстояние, двигаясь со ' \
          'средней скоростью 40 км/ч, а автомобиль - со средней скоростью 60 км/ч. На сколько часов пассажиры ' \
          'автобуса находятся в пути дольше, чем пассажиры автомобиля? '
chunk = []
numberOfSents = 0
for sent in sentenize(rawText):
    tokens = [_.text for _ in tokenize(sent.text)]
    chunk.append(tokens)
    numberOfSents += 1

navec1 = Navec.load('navec_news_v1_1B_250K_300d_100q.tar')
syntax = Syntax.load('slovnet_syntax_news_v1.tar')
syntax.navec(navec1)

i = 0
actorId = 0
while i < numberOfSents:
    markup_s = next(syntax.map(chunk[i:]))
    i += 1
    act = Actor('')
    num = 0
    id2, id3 = -1, -1
    shrt = ''
    me = MotionEl(num, shrt)
    for token in markup_s.tokens:
        if token.rel == "nsubj":
            actorId += 1
            print("actor", actorId, "is", lower(str(token.text)))

        elif token.rel == "nummod" and token.text.isdigit():
            num = int(token.text)
            id2 = int(token.id) + 1

        elif int(token.id) == id2 and id2 != -1:
            shrt = str(token.text)

        elif str(token.text) == "/":
            id3 = int(token.id) + 1
            shrt += str(token.text)

        elif int(token.id) == id3 and id3 != -1:
            shrt += str(token.text)
            me = MotionEl(num, shrt)
            id3 = -1
            id2 = -1
            print(me.motion_el, me.value, me.short)

        elif id2 != -1:
            me = MotionEl(num, shrt)
            id2 = -1
            print(me.motion_el, me.value, me.short)


