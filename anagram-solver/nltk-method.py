# anagram solver by shanil jasani @shaniljasani
# method 1 using nltk.corpus

# ROUGH WORK exploring the different permutations
# a b c d
# a b d c
# a c b d
# a c d b
# a d b c
# a d c b

# b a c d
# b a d c
# b c a d
# b c d a
# b d a c
# b d c a

# ... for c and d


# a b c   --> a c b, b a c, b c a, c a b, c b a
# a b   d
# a   c d
#   b c d


# src: https://stackoverflow.com/questions/3788870/how-to-check-if-a-word-is-an-english-word-with-python
from nltk.corpus import words
def is_english_word(word):
    return word in words.words()

def anagram_solver():

    # start timer for metrics tracking
    import time
    start = time.time()

    # get input
    letters = input("Enter your letters (no spaces or commas): ")

    # make permutations of various sizes
    from itertools import permutations
    perms = []
    size = len(letters)
    while (size > 2):
        temp_perms = permutations(letters, size)
        # DEBUG
        # for i in temp_perms:
        #     print(i)
        perms.append(temp_perms)
        size -= 1

    possible_options = []
    # make into words
    for perm_group in perms[::-1]:
        # print("starting a new group") # DEBUG
        for perm in perm_group:
            temp_str = ''.join(perm)
            if is_english_word(temp_str):
                # print(temp_str)   # DEBUG
                possible_options.append(temp_str)

    # sort and print
    sorted_options = sorted(possible_options, key=len)
    for option in sorted_options[::-1]:
        print(option)

    end = time.time()
    print(str(end - start) + " seconds taken")


if __name__ == '__main__':
    anagram_solver()
