'''
Created on 08.04.2013

@author: daddy
'''

FIELDSIZE = 4

class Field(object):
    def __init__(self, elements):
        assert len(elements) == FIELDSIZE*FIELDSIZE
        self.lines = []
        for i in range(FIELDSIZE):
            self.lines.append(elements[i * FIELDSIZE : (i * FIELDSIZE) + FIELDSIZE])
        # initialize some values we will need often for better performance
        self.allFields = [(x, y) for x in range(FIELDSIZE) for y in range(FIELDSIZE)]
        self.characterSet = set(elements)
    
    def possibleNextPicks(self, chosenElements = []):
        """
        Returns all the next elements that can be chosen, given a former path. Returns all
        elements if none has been chosen so far.
        """
        if chosenElements == []:
            return self.allFields
        else:
            lastChosen = chosenElements[-1]
            elementsAround = self.elementsAround(lastChosen[0], lastChosen[1])
            return [x for x in elementsAround if x not in chosenElements]
        
    def elementsAround(self, x, y):
        """
        Returns all fields around a given coordinate. Does not return coordinates out of the field.
        """
        for i in range(-1, 2):
            for o in range(-1, 2):
                if x + i >= 0 and x + i < FIELDSIZE:
                    if y + o >= 0 and y + o < FIELDSIZE:
                        if i != 0 or o != 0:
                            yield (x + i, y + o)
        
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
                    
        

if __name__ == '__main__':
    allWords = open("allWords.txt").read().split()
    
    fieldString = raw_input("Please enter all characters: ")
    f = Field(fieldString)
    
    existingWords = [word.lower() for word in allWords 
                     if f.exists(word) and len(word) > 3]
    existingWords = list(set(existingWords))
    existingWords.sort(key = len)
    for word in existingWords:
        print word
    