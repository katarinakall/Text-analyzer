#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
python
Ett program som gör en textanalys genom att räkna antalet ord och antalet bokstäver
samt i vilken frekvens de förekommer i texten.
kakl19
2019-10-16
"""
import menu
import analyzer

def main():
    """
    Generates the menu throug an eternal loop. It checks the choice done by the
    user and calls the appropriate function. Loop breaks when q is the user input.
    """
    menu.generate_menu()
    result = ""
    while True:
        choice = input("--> ")

        if choice == "q":
            quit()

        elif choice == "lines":
            result = analyzer.lines()

        elif choice == "words":
            result = analyzer.words()

        elif choice == "letters":
            result = analyzer.letters()

        elif choice == "word_frequency":
            result = analyzer.word_frequency()

        elif choice == "letter_frequency":
            result = analyzer.letter_frequency()

        elif choice == "all":
            result = analyzer.all_analyzes()

        elif choice == "change":
            analyzer.change()

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        analyzer.pretty_print(result)
        result = ""

if __name__ == '__main__':
    main()
