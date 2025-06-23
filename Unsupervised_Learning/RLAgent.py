import numpy as np
import random
from time import sleep

# Environment parameters
ROAD_LENGTH = 5  # Steps needed to cross the road
MAX_STEPS = 20   # Maximum steps per episode

# Actions
LOOK_LEFT = 0
LOOK_RIGHT = 1
MOVE_FORWARD = 2
ACTIONS = [LOOK_LEFT, LOOK_RIGHT, MOVE_FORWARD]
ACTION_NAMES = ['Look Left', 'Look Right', 'Move Forward']

# Simplified state representation
# position: 0 to ROAD_LENGTH (0=start, ROAD_LENGTH=crossed)
# has_looked: True if agent has looked both ways

# Q-table initialization
q_table = np.zeros((ROAD_LENGTH + 1, 2, len(ACTIONS)))

# Hyperparameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.2  # Exploration rate
episodes = 5000  # Number of training episodes

def get_reward(state, action):
    position, has_looked = state
    
    # Successfully crossed
    if action == MOVE_FORWARD and position == ROAD_LENGTH - 1:
        return 100
    
    # Tried to move without looking
    if action == MOVE_FORWARD and not has_looked:
        return -20
    
    # Tried to move when not at edge
    if action == MOVE_FORWARD and position > 0 and position < ROAD_LENGTH - 1:
        return -10
    
    # Small penalty for looking too much
    if action in [LOOK_LEFT, LOOK_RIGHT]:
        return -1
    
    # Small penalty for each step
    return -0.1

def take_action(state, action):
    position, has_looked = state
    new_position = position
    new_has_looked = has_looked
    
    if action == MOVE_FORWARD and position < ROAD_LENGTH:
        new_position = position + 1
    elif action == LOOK_LEFT or action == LOOK_RIGHT:
        # After looking both ways, set has_looked to True
        new_has_looked = True
    
    return (new_position, new_has_looked)

def choose_action(state, epsilon):
    if random.uniform(0, 1) < epsilon:
        return random.choice(ACTIONS)  # Explore
    else:
        position, has_looked = state
        return np.argmax(q_table[position, int(has_looked)])  # Exploit

def train_agent():
    for episode in range(episodes):
        state = (0, False)  # Start at position 0, hasn't looked
        done = False
        steps = 0
        
        while not done and steps < MAX_STEPS:
            position, has_looked = state
            action = choose_action(state, epsilon)
            next_state = take_action(state, action)
            reward = get_reward(state, action)
            
            # Q-learning update
            old_value = q_table[position, int(has_looked), action]
            
            next_position, next_has_looked = next_state
            if next_position == ROAD_LENGTH:
                next_max = 0  # Terminal state
            else:
                next_max = np.max(q_table[next_position, int(next_has_looked)])
            
            new_value = old_value + alpha * (reward + gamma * next_max - old_value)
            q_table[position, int(has_looked), action] = new_value
            
            state = next_state
            steps += 1
            
            if position >= ROAD_LENGTH:
                done = True

def test_agent():
    state = (0, False)
    done = False
    steps = 0
    
    print("Testing trained agent...")
    print("Starting at the sidewalk, ready to cross the road.")
    
    while not done and steps < MAX_STEPS:
        position, has_looked = state
        action = choose_action(state, 0)  # No exploration during testing
        
        print(f"\nStep {steps + 1}:")
        print(f"Position: {position}/{ROAD_LENGTH}")
        print(f"Has looked both ways: {'Yes' if has_looked else 'No'}")
        print(f"Action: {ACTION_NAMES[action]}")
        
        state = take_action(state, action)
        steps += 1
        
        if position >= ROAD_LENGTH:
            print("\nSuccessfully crossed the road!")
            done = True
            return
        
        sleep(0.5)  # Pause for readability
    
    print("\nFailed to cross the road in time.")

# Train the agent
print("Training agent...")
train_agent()
print("Training completed!")

# Test the agent
test_agent()