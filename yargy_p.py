from yargy import Parser, rule
from yargy.predicates import gram, dictionary
import csv

startQWords = []
with open('StartWords.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        startQWords.extend(row)

actors = []
with open('actors.csv', newline='') as File:
    reader2 = csv.reader(File)
    for row in reader2:
        actors.extend(row)

R_1 = rule(dictionary(startQWords), gram('VERB'), gram('NOUN'), gram('NOUN'))
R_2 = rule(dictionary(startQWords), gram('VERB'), gram('NOUN'))
R_3 = rule(dictionary(startQWords), gram('NOUN'), gram('NPRO'), gram('VERB'))
parser = Parser(R_1) or Parser(R_2)
parser3 = Parser(R_3)


def find_x_parser(txt):
    for match in parser.findall(txt):
        print([x.value for x in match.tokens])

    for match in parser3.findall(txt):
        print([x.value for x in match.tokens])


def find_actors(txt):
    actor = []
    act_id = 0
    for match in parser_actor.findall(txt):
        actor.extend([x.value for x in match.tokens])
    for i in actor:
        act_id += 1
        if str(i) in same_str_dict and act_id > 1:
            pass
        else:
            print("Actor", act_id, "is", str(i))
    return act_id


def type_of_the_task(txt):
    typeoft = ''
    for match in parser_type_of_task.findall(txt):
        for x in match.tokens:
            typeoft = x.value
    if typeoft == '':
        typeoft = 'равномерное прямолинейное'
        print('Type of the task is uniform rectilinear')
    elif type_dictionary.get(typeoft):
        print('Type of the task is', type_dictionary.get(typeoft))
