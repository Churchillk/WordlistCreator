import itertools
from keyboard import press_and_release, write
from time import sleep

words = []
WordName = input("enter name of the wordlist add extension (.txt:) ")
words123 = open(WordName, "w")


def main():
    num_letters = int(input("Enter the number of letters: "))
    letters = str(input("Enter the letters separated by spaces: ")).split()

    if len(letters) != num_letters:
        print("The number of letters entered doesn't match the specified count.")
        return

    print("\nAll possible combinations:")
    combinations = list(itertools.permutations(letters, num_letters))

    for combination in combinations:
        #print("".join(combination))
        words.append("".join(combination))


if __name__ == "__main__":
    main()
    for word in words:
        words123.write(str(word) + "\n")

    words123.close()
