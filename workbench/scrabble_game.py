from random import choice


def finding_and_replacing_similar_words(sentence: str):

    print(sentence)
    suitable_words = []
    new_sentence = ''

    with open('list_of_words.txt') as file:
        words = file.readlines()

    for word in sentence.split():
        for wrd in words:
            if len(word) == len(wrd.strip()) and word[0] == wrd[0]:
                suitable_words.append(wrd.strip())
            elif word not in suitable_words:
                suitable_words.append(word)

        new_sentence += f'{choice(suitable_words)} '
        suitable_words = []

    file.close()
    return new_sentence


if __name__ == '__main__':
    sentence = input('Enter a sentence of your choice: ').lower()
    print(finding_and_replacing_similar_words(sentence))