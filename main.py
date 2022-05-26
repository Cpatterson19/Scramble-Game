import random 

def choose (): 

words =['rainbow','computer','science' 'programming','foxtrot' ]



pick=random,choice(words)

return pick

def jumble(word):

  random_word=random.sample(word, lean(word))

jumble = ''.join(random_word)

return jumbled 

def thank(p1n, p2np1, p2,):
  print(p1n, 'Your score is :' ,p1)
  print(p2n, 'Your score is :' ,p2)

check_win(p1n,p2n,p1,p2)

print('Thanks for playing...')

def check_win(player1,player2,p1score,p2score):
  if p1score > p2score:
    print(winner is:", player1)
  elif p2score > p1score:
    print("winner is:",player2)
  else:
    print("Draw...Well Played!")

def play():

  p1name=input("player 1 ,Please enter your name:")
  p2name=input("player 2 ,Please enter your name:")

pp1 = 0
pp2 = 0
turn = 0


while true:
  Picked_word=choose()


qn=jumble(picked_word)

if turn % 2==0

print("p1name,your turn")

ans = input("What's in your mind?")

if ans == picked_word:

  pp1 += 1 
print("Your score is :",pp1)

turn+=1

else:
print("Better luck next time...")

print(p2name,"Your turn.")


print("p2name,your turn")

ans = input("What's in your mind?")

if ans == picked_word:

  pp2 += 1 
print("Your score is :",pp2)

turn+=1

else:
print("Better luck next time...correct word is ")


c = int(input("press 1 tp continue and 0 to quit:")) 
if c == 0:

  thank(p1name,p2name,pp1,pp2)
  break 

else: 
 if ans == picked_word:

  pp1 += 1 
print("Your score is :",pp1)

turn+=1

else:
print("Better luck next time...correct word is ")


c = int(input("press 1 tp continue and 0 to quit:")) 
if c == 0:

  thank(p1name,p2name,pp1,pp2)

play()