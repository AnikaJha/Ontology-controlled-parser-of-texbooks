from numpy.core.defchararray import lower
from yargy import Parser, rule, or_
from yargy.predicates import gram, dictionary
import csv

same_str_dict = {'Мотоцикл': 'мотоцикл', 'мотоциклист': 'мотоцикл', 'мотоциклиста': 'мотоцикл',
                 'мотоциклисту': 'мотоцикл',
                 'Автомобилю': 'машина', 'автомобиля': 'машина',
                 'автомобилист': 'машина', 'автомобилиста': 'машина',
                 'машину': 'машина', 'машины': 'машина',
                 'автобуса': 'автобус', 'пешехода': 'пешеход', 'самолета': 'самолет',
                 'велосипедиста': 'велосипедист'}
type_dictionary = {'ускорение': 'with acceleration', 'ускорением': 'with acceleration',
                   'средняя': 'irregular rectilinear', 'среднюю': 'irregular rectilinear'}

startQWords = []
with open('StartWords.csv') as File:
    reader = csv.reader(File)
    for row in reader:
        startQWords.extend(row)
        startQWords.extend(lower(row))

actors = []
with open('actors.csv', newline='') as File:
    reader2 = csv.reader(File)
    for row in reader2:
        actors.extend(row)
        actors.extend(lower(row))

R_1 = rule(dictionary(startQWords), gram('VERB'), gram('NOUN'), gram('NOUN'))
R_2 = rule(dictionary(startQWords), gram('VERB'), gram('NOUN'))
R_6 = rule(dictionary(startQWords), gram('NOUN'), gram('NOUN'))
R_7 = rule(dictionary(startQWords), gram('ADJF'), gram('NOUN'))
R_8 = rule(dictionary(startQWords), gram('ADJS'), gram('NOUN'))
R_3 = rule(dictionary(startQWords), gram('NOUN'), gram('NPRO'), gram('VERB'))
R_4 = rule(dictionary(actors))
R_5 = rule(dictionary(type_dictionary))

parser = Parser(or_(R_1, R_2))
parser2 = Parser(or_(R_6, R_3, R_7, R_8))

parser_actor = Parser(R_4)
parser_type_of_task = Parser(R_5)


def find_x_parser(txt):
    for match in parser.findall(txt): print([x.value for x in match.tokens])
    for match in parser2.findall(txt): print([x.value for x in match.tokens])



def find_actors(txt) -> int:
    actor = []
    act_id = 0
    for match in parser_actor.findall(txt):
        actor.extend([x.value for x in match.tokens])
    new_actors_list = []
    for i in actor:
        act_id += 1
        if str(i) in same_str_dict and act_id > 1:
            act_id -= 1
        else:
            new_actors_list.append(same_str_dict.get(str(i)))
            print("Actor", act_id, "is", str(i))
    return act_id


def type_of_the_task(txt):
    typeoft = ''
    for match in parser_type_of_task.findall(txt):
        for x in match.tokens:
            typeoft = x.value
    if type_dictionary.get(typeoft):
        print('Type of the task is', type_dictionary.get(typeoft))
    else:
        typeoft = 'равномерное прямолинейное'
        print('Type of the task is uniform rectilinear')
