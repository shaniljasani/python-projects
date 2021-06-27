# Anagram Solver
I play this anagram game on iMessage's GamePigeon app a lot. While I don't condone cheating on the game, I wanted to see how the code would work on this project.

### Approach
I tried to first manually create all the permutations (see the comments haha) but then found that python has permutations and combinations as part of the `itertools` library. I then compare against a dictionary to verify the word is in the English language and print the valid outputs in decreasing length order.

### Learning
To verify if a word is in the English dictionary, I first used the `nltk.corpus` package. This turned out to be TOO slow, so I used an existing dictionary file called `american-english.txt` from a school assignment. The results were surprising!

| Method   |      Time elapsed for `bmelir`      |
|----------|:-------------:|
| nltk.corpus |  130.562 seconds |
| american-english.txt |    3.155   |
