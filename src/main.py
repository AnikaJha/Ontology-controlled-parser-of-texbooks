from razdel import sentenize, tokenize
from navec import Navec
from slovnet import Syntax
from yargy_p import find_actors, find_x_parser, type_of_the_task

dictionary_s = {'путь', 'километр', 'метр', 'сантиметр', 'длина', 'дорога', 'расстояние', 'км', 'см', 'дм', 'м'}
dictionary_t = {'время', 'час', 'часа', 'часов', 'секунд', 'секунда', 'минута', 'ч', 'с', 'мин'}
dictionary_v = {'скорость', 'м/с', 'км/ч', 'дм/мин', 'км/с', 'м/мин'}
dictionary_a = {'ускорение', 'м/с2'}
dictionary_scene = {'машина', 'автобус', 'автомобиль', 'мотоцикл', 'поезд', 'Дорога',
                    'поплавок', 'река', 'реку', 'Вода'}
me_v = 'скорость'
me_s = 'путь'
me_t = 'время'
me_a = 'ускорение'


class MotionEl(object):

    def __init__(self, value, short):
        self.value = value
        self.short = short
        self.motion_el = None
        if short in dictionary_a:
            self.motion_el = me_a
        elif short in dictionary_v:
            self.motion_el = me_v
        elif short in dictionary_t:
            self.motion_el = me_t
        elif short in dictionary_s:
            self.motion_el = me_s


def main_extractor(raw_text):
    chunk = []
    number_of_sents = 0
    for sent in sentenize(raw_text):
        tokens = [_.text for _ in tokenize(sent.text)]
        chunk.append(tokens)
        number_of_sents += 1

    navec1 = Navec.load('navec_news_v1_1B_250K_300d_100q.tar')
    syntax = Syntax.load('slovnet_syntax_news_v1.tar')
    syntax.navec(navec1)

    i = 0
    print()
    type_of_the_task(raw_text)
    print()
    actorIDs = find_actors(raw_text)
    if actorIDs == 1:
        print('\nMotion elements of the actor:')
    else:
        print('\nMotion elements of actors:')  # should be extended

    while i < number_of_sents:
        markup_s = next(syntax.map(chunk[i:]))
        i += 1
        num = 0
        id2, id3 = -1, -1
        shrt = ''
        me = MotionEl(num, shrt)
        for token in markup_s.tokens:
            if token.rel == "nummod" and token.text.isdigit():
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
                id2 = -1
                id3 = -1
                print(me.motion_el, me.value, me.short)

            elif id2 != -1 or id3 != -1:
                me = MotionEl(num, shrt)
                id2 = -1
                print(me.motion_el, me.value, me.short)


    print("\nThe main question(s) of the text is(are)")
    find_x_parser(raw_text)


print("Введите задание из физики по теме кинематика:")
rawText = str(input())
main_extractor(rawText)
