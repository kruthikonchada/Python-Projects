def minion_game(string):
    if len(string) > 0 and len(string) <= 1000000:
        count = 0
        vowels = 0
        consonants = 0
        for i in string:
            if i >= 'A' and i <= 'Z':
                count = count + 1
        if count == len(string):
            for i in range(len(string)):
                if string[i] not in 'AEIOU':
                    consonants += len(string) - i
                else:
                    vowels += len(string) - i
        if vowels > consonants:
            print(f'Kevin {vowels}')
        elif vowels < consonants:
            print(f'Stuart {consonants}')
        else:
            print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)