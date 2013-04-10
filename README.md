Fun with Wordblitz
==================

Wordblitz is a little game for Android and iOS, that I got addicted to a few days ago. The gameplay is really simple, you have to find words in a 4x4 grid of characters that show on the screen. When starting at one character, you can only select the surrounding ones as a second, and so on. The longer a word, the more bonus points you will receive. What makes it really fun is that you can play it against your facebook friends, if they also installed the game.

![Screenshot](/screenshot.jpg "Screenshot")

From a developers perspective, I was wondering how hard it is to create an algorithm that solves this game. You would give it the character grid and it will return all long words that are hidden inside. Of course, this algorithm has to give the results within short enough time to be useful for Wordblitz. And since I don't want to spend any productive time on this problem, it has to finished quickly. Therefore, my flight to the Droidcon was the perfect setup for working on it.

Implementation
--------------

Ok, first some prerequisites. We definitely need some kind of wordlist for actually having words to compare. Then, the 4x4 grid has to be stored in a simple data structure. Since I want to implement everything in python, a list seems to be handy. Fortunately, I already have a big "allWords.txt", because it had been useful before. That one we have to load into memory:


    allWords = open("allWords.txt").read().split()
    

Next, let's initialize the grid by writing down all characters in the reading-order:


    fieldString = raw_input("Please enter all characters: ")
    f = Field(fieldString)


The Field object should store the grid and implement some helper methods we need. So how to structure the algorithm for finding out all words? Well, let's start with creating a method that checks if a specific word exists inside the grid:


    def exists(self, word, chosenElements = None):
        """
        Returns if the given word can be constructed within the field.
        """
        if chosenElements is None:
            chosenElements = []
        if len(word) == 0:
            return True
        character = word[0]
        if character in self.characterSet:
            for pick in self.possibleNextPicks(chosenElements):
                if self.lines[pick[0]][pick[1]].lower() == character:
                    chosenElements.append(pick)
                    return self.exists(word[1:], chosenElements)
        return False


This is a recursive method that carries the already chosen elements and the remaining part of our word. Elements are tuples of grid positions, like (0,1) or (3,3). This method relies on self.possibleNextPicks, which will give all chooseable elements for characters, given the already chosen elements. I will not talk about it in detail, but it is rather easy to implement.


Step through
------------

So let's step through it with the word "wort", like on the screenshot.

First Recursion
word = "wort", chosenElements = None

The method picks the first character and goes through all possible next picks. Since this is the first pick, it will iterate through all the elements. At the second possible pick, it finds the character "w" and continues to the next recursion:


Second Recursion
word = "ort", chosenElements = [(0,1)]

Since we already selected the first element, we are more restricted in choosing the next one. Only 5 elements are available. When the "o" is found, the algorithm goes on to the next recursion:


Third Recursion:
word = "rt", chosenElements = [(0,1), (1,0)]


Fourth Recursion:
word = "t", chosenElements = [(0,1), (1,0), (2,0)]


Fifth Recursion:
word = "", chosenElements = [(0,1), (1,0), (2,0), (3,1)]


And we are finished, so the algorithm can return true.


