def wordsearch():
    # python3 -m pip install python-wordsearch
    from wordsearch import WordSearch

    wordsearch = WordSearch(
        15,
        15,
        [
            "RED",
            "ORANGE",
            "YELLOW",
            "GREEN",
            "BLUE",
            "INDIGO",
            "VIOLET",
            "PINK",
        ],
        mask="circle",
        output_filestem="color-search",
        allow_backwards_words=True,
    )
    wordsearch.make()
    print(wordsearch.wordsearch_text)

print("-------------")
print("q: quit")
print("e: emoji")
print("j: joke")
print("w: wordsearch")
print("-------------")

while True:
    print()
    option = input("Enter an option: ")

    if option == "q":
        break

    elif option == "e":
        # python3 -m pip install emoji
        from emoji import emojize
        print(emojize(":thumbs_up:"))

    elif option == "j":
        # python3 -m pip install pyjokes
        import pyjokes
        print(pyjokes.get_joke())

    elif option == "w":
        # python3 -m pip install python-wordsearch
        from wordsearch import WordSearch

        wordsearch = WordSearch(
            15,
            15,
            [
                "RED",
                "ORANGE",
                "YELLOW",
                "GREEN",
                "BLUE",
                "INDIGO",
                "VIOLET",
                "PINK",
            ],
            mask="circle",
            output_filestem="color-search",
            allow_backwards_words=True,
        )
        wordsearch.make()
        print(wordsearch.wordsearch_text)

    else:
        print("Invalid option, try again.")