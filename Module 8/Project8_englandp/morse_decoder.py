from morse_tree import MorseTree

def main():
    morse = MorseTree()

    morse.add("A", ".-")
    morse.add("B", "-...")
    morse.add("C", "-.-.")
    morse.add("D", "-..")
    morse.add("E", ".")

    morse.add("T", "-")


    with open(f'morsecode.txt') as txtfile:
        for line in txtfile:
            if (line.strip()[0:1:1] == '\\'): # the \n
                morse.add(line.strip()[0:2:1], line.strip()[2:])
            else:
                morse.add(line.strip()[0:1:1], line.strip()[1:])

    txtfile.close()

    #print(f"line 0: {lines[0]}")

    morse_message = ".- .-... ... .--. .- -.-. . .-... ... .... --- ..- .-.. -.. .-... -... . .-... .--. .-.. .- -.-. . -.. .-... -... . - .-- . . -. .-... . .- -.-. .... .-... . -. -.-. --- -.. . -.. .-... -.-. .... .- .-. .- -.-. - . .-. .-.-.- .-.-"

    morse_pieces = morse_message.split(" ") #
    # parse that message to split on the spaces
    for m in morse_pieces:
        print(morse.decode(m))

    #TODO it looks B and ' ' space are not being decoded correctly.

    # what we can't do yet is take characters, and encode them into morse code.
    # this requires a different tree, which should be based on our original BST
    # key is a character, and data is the morse code.
    # you wouldn't want to build this tree with data already in alphabetical order

    print(morse)
if __name__ == "__main__":
    main()