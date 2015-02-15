from random import randint
class mastermindGame:
    def __init__(self, MAX, LENGTH, W, pos):
        self.MAX = MAX
        self.LENGTH = LENGTH
        self.WIDTH = WIDTH
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
        rP = 0
        rC = 0
        for c in guess:
            if c == self.ans[i]:
                rP += 1
            i+=1
        for c in guess:
            isRight = False
            for c2 in self.ans:
                if c == c2:
                    isRight = True
            if isRight:
                rC += 1
        rC -= rP
        return (rP * 'O') + (rC * 'X')
