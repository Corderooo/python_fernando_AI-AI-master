import frequenzy



with open("wordle/words.txt", "r") as file:
    words = file.read().splitlines()

five_words = []

for i in range(len(words)):
    if len(words[i]) == 5:
        five_words.append(words[i])

grey_letters = "udiy"
possible_words = []
yellow_letters = ""
green_letters = "_o_al"

for i in range(len(five_words)):
    word = five_words[i]
    match = True

    for letter in grey_letters:
        if letter in word:
            match = False

    for letter in yellow_letters:
        if letter not in word:
            match = False

    for i, letter in enumerate(green_letters):
        if not letter == "_" and not letter == word[i]:
            match =  False


    if match:
        possible_words.append(word)
print(possible_words)
possible_words.sort(key=frequenzy.of_word)
print("possible words:", len(possible_words))


        

        
        

