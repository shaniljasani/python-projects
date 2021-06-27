# anagram solver by shanil jasani @shaniljasani
# method 2 using a local dictionary


english_words = []

# import txt file
with open("american-english.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)

# returns true if word is in dictionary
def is_english_word(word):
    return word.lower() in english_words

# driver function
def anagram_solver():

    # start timer to track efficiency
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

    # REMOVE DUPLICATES
    possible_options = list(set(possible_options))

    # sort and print
    sorted_options = sorted(possible_options, key=len)
    for option in sorted_options[::-1]:
        print(option)

    end = time.time()
    print(str(end - start) + " seconds taken")


if __name__ == '__main__':
    anagram_solver()