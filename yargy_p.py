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


def find_x_parser(text):
    for match in parser.findall(text):
        print([x.value for x in match.tokens])

    for match in parser3.findall(text):
        print([x.value for x in match.tokens])


text = 'Мотоцикл за первые два часа проехал 90 км, а следующие 3 часа двигался со скоростью 50 км/ч. Какой была ' \
       'скорость мотоциклиста на первом участке пути? Какой путь он прошел за все время движения? '

find_x_parser(text)
