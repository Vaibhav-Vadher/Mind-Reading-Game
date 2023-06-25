print("*--------------------------------------------------------------*")  
print("*--------------------=> MIND READER GAME <=--------------------*")                                                                              
print("*--------------------------------------------------------------*")
print()
print("===>Hello, My Name is AI Bot.\n===>I can read your mind and guess your next move.")
print()
print("----------------------------------------------------------------")
print("\n===>I score a point if I guessed it right else you get one.\n===>First to reach 50 Wins!.\n===>Can you beat me to it")
print()
print("----------------------------------------------------------------")
 
import random
import numpy as np
 
inputs = np.zeros(shape=(2, 2, 2), dtype=int)
 
last_1 = 0
last_2 = 0
scores=[0,0]
 
def update_inputs(current):
  global last_1, last_2
  if inputs[last_2][last_1][0] == current:
    inputs[last_2][last_1][1] = 1 
    inputs[last_2][last_1][0] = current
  else:
    inputs[last_2][last_1][1] = 0 
    inputs[last_2][last_1][0] = current
 
  last_2 = last_1 
  last_1 = current 
 
def prediction():
  if inputs[last_2][last_1][1] == 1:
    predict = inputs[last_2][last_1][0]    
  else:
    predict = random.randint(0, 1)  
  return predict
 
def update_scores(predicted, player_input):
  if player_input==predicted:
    scores[0] += 1
    print('-Your Score: ',scores[1])
    print('-AI Bot Score: ',scores[0])
  else:
    scores[1] += 1
    print('-Your Score:',scores[1])
    print('-AI Bot Score:',scores[0])
 
def reset():
  for i in range(2):
      for j in range(2):
          for k in range(2):
              inputs[i][j][k]=0
  for i in range(2):
    scores[i]=0
 
def gameplay():
  valid_entries=['0','1']
  while True:
      predicted=prediction()
      player_input=input("\n=>Enter either 0 or 1: ")
      while player_input not in valid_entries:
        print("==>'Invalid Input'<==")
        player_input=input("\n=>Enter either 0 or 1: ")
 
      player_input=int(player_input)
      update_inputs(player_input)
      update_scores(predicted, player_input)
 
      if scores[0]== 100:
        print("\n===============================================================")
        print("=====> 'You Lost!' <=====")
        break
      elif scores[1]== 100:
        print("\n===============================================================")
        print("\n=====> 'You Won!' <=====")
        break
        
gameplay()
 
print("\n")
print("\_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_/")