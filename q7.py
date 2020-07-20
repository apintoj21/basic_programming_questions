"""How do you reverse words in a given sentence without using any library method?
"""


def reverse(word):
    return word[::-1]


def main():
    sentence = "ehT tac eta eht esuom"
    words = sentence.split(" ")
    new_sentence = " ".join([reverse(word) for word in words])
    print(new_sentence)


if __name__ == "__main__":
    main()
