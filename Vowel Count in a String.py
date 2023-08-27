def vowel_count():
    word = input("Enter a string: ")
    vowel_count = word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u") + word.count("A") + word.count("E") + word.count("I") + word.count("O") + word.count("U") 
    print("Vowel count: " + str(vowel_count))


vowel_count()
