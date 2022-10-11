import random 

game = 10
score = 0
win = draw = lose = 0

while game > 0:
    player1 = random.randint(1,6)
    player2 = random.randint(1,6)
    if  player2 > player1:
        score += 2
        win += 1
    elif  player2 == player1:
        score +=1
        draw += 1
    else:
        lose += 1
        
    game -= 1
    
print('내 점수:', score)
print(str(win)+'승', str(draw)+'무', str(lose)+'패')