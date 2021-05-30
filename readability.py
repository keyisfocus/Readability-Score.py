import argparse
import math
import re
import statistics


def count_syllables_polysyllables(*args):
    vowels = 'aeiouy'
    total_syllables = 0
    polysyllables = 0
    for word in args:
        word_syllables = 0
        on_vowel = False
        word = word if word[-1] != 'e' else word[0:-1]
        for char in word:
            if char in vowels:
                word_syllables = word_syllables if on_vowel else word_syllables + 1
                on_vowel = True
            else:
                on_vowel = False
        word_syllables = word_syllables if word_syllables > 0 else 1
        total_syllables += word_syllables
        polysyllables = polysyllables if word_syllables <= 2 else polysyllables + 1
    return total_syllables, polysyllables


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-in', '--infile')
arg_parser.add_argument('-w', '--words')
clargs = arg_parser.parse_args()

with open(clargs.infile) as infile, open(clargs.words) as words_file:
    text = infile.read().lower()
    dif_words = words_file.read().split()

sentences = [sentence for sentence in re.split('[.!?]', text) if sentence]
words = [word for sentence in sentences for word in re.sub('[,:()]', '', sentence).split()]
char_count = sum(1 for char in text if char not in ' \n\t')
syllable_count, polysyllable_count = count_syllables_polysyllables(*words)
difficult_count = sum(1 for word in words if word not in dif_words)

print(f'Words: {len(words)}')
print(f'Difficult words: {difficult_count}')
print(f'Sentences: {len(sentences)}')
print(f'Characters: {char_count}')
print(f'Syllables: {syllable_count}')
print(f'Polysyllables: {polysyllable_count}')

choice = input('Enter the score you want to calculate (ARI, FK, SMOG, CL, PB, all):\n')

ari = round(4.71 * char_count / len(words) + 0.5 * len(words) / len(sentences) - 21.43, 2)
fk = round(0.39 * len(words) / len(sentences) + 11.8 * syllable_count / len(words) - 15.59, 2)
smog = round(1.0430 * math.sqrt(polysyllable_count * 30 / len(sentences)) + 3.1291, 2)
cl = round(0.0588 * char_count / len(words) * 100 - 0.296 * len(sentences) / len(words) * 100 - 15.8, 2)
pb = 0.1579 * difficult_count / len(words) * 100 + 0.0496 * len(words) / len(sentences)
pb = pb if difficult_count / len(words) * 100 < 5 else pb + 3.6365
pb = round(pb, 2)
pb_score = math.floor(pb) * 2 + 2 if math.floor(pb) < 9 else 24

age_map = {
    1: 6,
    2: 7,
    3: 9,
    4: 10,
    5: 11,
    6: 12,
    7: 13,
    8: 14,
    9: 15,
    10: 16,
    11: 17,
    12: 18,
    13: 24,
}

if choice == 'ARI':
    print(f'Automated Readability Index: {ari} (about {age_map.get(math.ceil(ari), 25)}-year-olds).')
elif choice == 'FK':
    print(f'Flesch–Kincaid readability tests: {fk} (about {age_map.get(math.ceil(fk), 25)}-year-olds).')
elif choice == 'SMOG':
    print(f'Simple Measure of Gobbledygook: {smog} (about {age_map.get(math.ceil(smog), 25)}-year-olds).')
elif choice == 'CL':
    print(f'Coleman–Liau index: {cl} (about (about {age_map.get(math.ceil(cl), 25)}-year-olds).')
elif choice == 'PB':
    print(f'Probability-based score: {pb} (about {pb_score}-year-olds)')
else:
    mean = statistics.mean((age_map.get(math.ceil(ari), 25),
                            age_map.get(math.ceil(fk), 25),
                            age_map.get(math.ceil(smog), 25),
                            age_map.get(math.ceil(cl), 25),
                            pb_score))
    print(f'Automated Readability Index: {ari} (about {age_map.get(math.ceil(ari), 25)}-year-olds).')
    print(f'Flesch–Kincaid readability tests: {fk} (about {age_map.get(math.ceil(fk), 25)}-year-olds).')
    print(f'Simple Measure of Gobbledygook: {smog} (about {age_map.get(math.ceil(smog), 25)}-year-olds).')
    print(f'Coleman–Liau index: {cl} (about (about {age_map.get(math.ceil(cl), 25)}-year-olds).')
    print(f'Probability-based score: {pb} (about {pb_score}-year-olds)')
    print(f'This text should be understood in average by {mean}-year-olds.')
