# DFA Simulator for File Operation Transitions

# Define the DFA components
states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'}
alphabet = ['open', 'file', 'close', 'exit', 'tab', 'new', 'save', 'as']

# Transition function: state -> input -> next state
transitions = {
    'q0': {'open': 'q1', 'close': 'q3', 'exit': 'q5', 'save': 'q7'},
    'q1': {'file': 'q2'},
    'q3': {'tab': 'q4'},
    'q5': {'new': 'q6'},
    'q7': {'as': 'q8'}
}

start_state = 'q0'
accept_states = {'q2', 'q4', 'q6', 'q8'}  # You can define more accept states if needed

def dfa_simulator(input_string):
    current_state = start_state
    for symbol in input_string:
        if symbol in transitions.get(current_state, {}):
            current_state = transitions[current_state][symbol]
        else:
            return False, current_state  # Invalid transition
    return current_state in accept_states, current_state

# Example: User Input
print("Enter input symbols separated by space (e.g., open file):")
user_input = input().strip().split()

# Run DFA
result, final_state = dfa_simulator(user_input)

# Output
if result:
    print(f"Input accepted! Final state: {final_state}")
else:
    print(f"Input rejected! Stopped at state: {final_state}")
