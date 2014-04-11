#! /usr/bin/env python
import random
score=0
f=open("HighScore.txt","r+")
high=f.read()
if high=='':
    high=0
print "Coin Guessing Game. All time high score: ", high, " correct\n"
while True:
    iDontActuallyCare=raw_input("Predict heads or tails> ")
    if iDontActuallyCare=='heads' or iDontActuallyCare=='tails':
        if random.randint(0,1)==0:
            score=score+1
            print "It is ",iDontActuallyCare ,". Your score is : ", score, "\n"
        else:
            if iDontActuallyCare=='heads':
                print "It is tails. Game Over\n"
            else:
                print "It is heads. Game Over\n"
            break
if score>high:
    f.seek(0)
    f.truncate()
    f.write(str(score))
    f.seek(0)
    high=int(f.read())
print "Your Score: ", score, " High Score: ", high