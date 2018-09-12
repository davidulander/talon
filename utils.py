import itertools
from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from time import sleep


# Useful for identifying app/window information for context selection
def context_func(app, win):
    print('---')
    # print(app)
    print(app.bundle)
    print(win)
    print(win.title)
    print(win.doc)
    print('---')
    return True


number_conversions = {
    # 'oh': '0', # 'oh' => zero
}
for i, w in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',]):
    number_conversions[str(i)] = str(i)
    number_conversions[w] = str(i)
    number_conversions['%s\\number'%(w)] = str(i)


def parse_words_as_integer(words):
    # TODO: Once implemented, use number input value rather than manually
    # parsing number words with this function

    # Ignore any potential trailing non-number words
    number_words = list(itertools.takewhile(lambda w: w not in number_conversions, words))

    # Somehow, no numbers were detected
    if len(number_words) == 0:
        return None

    # Map number words to simple number values
    number_values = list(map(lambda w: number_conversions[w.word], number_words))

    # Filter out initial zero values
    normalized_number_values = []
    non_zero_found = False
    for n in number_values:
        if not non_zero_found and n == '0':
            continue
        non_zero_found = True
        normalized_number_values.append(n)

    # If the entire sequence was zeros, return single zero
    if len(normalized_number_values) == 0:
        normalized_number_values = ['0']

    # Create merged number string and convert to int
    return int(''.join(normalized_number_values))

def repeat_function(numberOfWords, keyDescription, delay=0):
    def repeater(m): 
        line_number = parse_words_as_integer(m._words[numberOfWords:])

        if line_number == None:
            line_number = 1
 
        for i in range(0, line_number):
            sleep(delay)
            press(keyDescription)
    return repeater

threeDigitNumber = '(0 | oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)*'

def parse_word(word):
    word = str(word).lstrip('\\').split('\\', 1)[0]
    word = mapping.get(word, word)
    return word
