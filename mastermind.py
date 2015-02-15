from random import randint
class mastermindGame:
    def __init__(self, MAX, LENGTH, pos):
        self.MAX = MAX
        self.LENGTH = LENGTH
        self.WIDTH = len(pos)
        self.pos = pos
        self.guessesLeft = self.MAX
        self.ans = generateRandomAnswer()
    
    def generateRandomAnswer(self):
        posNotUsed = pos
        ans = ""
        for i in range(0, LENGTH):
            char = posNotUsed[randint(0,len(posNotUsed) - 1)]
            posNotUsed = posNotUsed.replace(char, "")
            ans += char
        return ans
    
    def putGuess(self, guess):
        i = 0
        rightPlace = 0
        rightChar = 0
        for guessChar in guess:
            if guessChar == self.ans[i]:
                rightPlace += 1
            i+=1
        for guessChar in guess:
            isRight = False
            for ansChar in self.ans:
                if guessChar == ansChar:
                    isRight = True
            if isRight:
                rightChar += 1
        rightChar -= rightPlace
        return (rightPlace * 'O') + (rightChar * 'X')
