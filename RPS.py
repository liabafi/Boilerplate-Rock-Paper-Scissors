# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random 

def player(prev_play, opponent_history=[], player_history=[]):
  moves=["R","P","S"]
  if prev_play=="":
    guess=moves[random.randint(0, 2)]
    player_history.append(guess)
    return guess

  opponent_history.append(prev_play)

  model = {"RR":{"R":0,"P":0,"S":0},
             "RP":{"R":0,"P":0,"S":0},
             "RS":{"R":0,"P":0,"S":0},
             "PR":{"R":0,"P":0,"S":0},
             "PP":{"R":0,"P":0,"S":0},
             "PS":{"R":0,"P":0,"S":0},
             "SR":{"R":0,"P":0,"S":0},
             "SP":{"R":0,"P":0,"S":0},
             "SS":{"R":0,"P":0,"S":0},         
            }
  
  memory=-1*min(30,len(opponent_history))
  for (i,move) in enumerate(opponent_history[memory:-1]):
        state=move+player_history[memory+i]
        opponent_next_move=opponent_history[memory+i+1]
        model[state][opponent_next_move]+=1
    
  state=prev_play+player_history[-1]

  prediction=max(model[state],key=model[state].get)

  ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
  guess=ideal_response[prediction]
    
  player_history.append(guess)
  return guess
