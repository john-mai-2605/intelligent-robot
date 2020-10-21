import matplotlib.pyplot as plt
from datetime import datetime

def log():
	# read file into string
	with open('rl_template.py', 'r') as inputfile:
		textstr = inputfile.read()
		fn = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".txt"
		
		with open("logs/"+fn, 'w') as outputfile:
			outputfile.write(textstr)

log()

N     = 100  # The goal for truly winning
p     = 0.25 # Probability of winning one bet
gamma = 1    # discount factor

states          = [i for i in range(1, N)]   # The states of the game when defined as a Markov Decision Process.
											 # states[x] represents the state of currently having x chips.
v               = [0 for i in range(0, N+1)] # The current state value function. v[x] is the value of state x.
optimal_actions = [0 for i in range(0, N+1)] # List to represent optimal policy. 
											 # optimal_actions[x] should equal the optimal number of 
											 # coins to bet when you currently have x chips (you're in state x).

											 # For both v and optimal_actions, if x == 0 or N, v[x] = optimal_actions[x] = 0.

### Implement value iteration here ###
import numpy as np
r = [[0 for i in range(N)] for j in range(N+1)]
for state in states:
	for action in range(1,state+1):
		if state + action >= N:
			r[state][action] = p
for i in range (100):
	new_v = []
	for state in states:
		new_v.append(max([r[state][action] + gamma*(p*v[min(state+action, N)] + (1-p)*v[max(state-action,0)]) for action in range(1, state+1)])) 
	v = [0] + new_v + [0]

for state in states:
	result = [r[state][action] + gamma*(p*v[min(state+action, N)] + (1-p)*v[max(state-action,0)]) for action in range(1, state+1)]
	best = np.argmax(np.asarray(result))
	optimal_actions[state] = best + 1
######################################

# Plot state value function for every state
fig = plt.figure()
plt.plot(states, v[1:-1])
plt.show()

# Plot optimal policy for every state
plt.plot(states, optimal_actions[1:-1], 'o')
plt.show()