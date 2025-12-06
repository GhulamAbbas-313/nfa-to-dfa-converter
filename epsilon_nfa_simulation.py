from collections import deque, defaultdict
from graphviz import Digraph

class EpsilonNFAConverter:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
        self.alphabet.add('ε')  # Epsilon always present

    def epsilon_closure(self, states):
        closure = set(states)
        queue = deque(states)
        print(f"\nε-Closure Calculation for {states}:")

        while queue:
            state = queue.popleft()
            epsilon_trans = self.transitions.get(state, {}).get('ε', set())
            print(f"  From {state}: ε → {epsilon_trans}")

            for new_state in epsilon_trans:
                if new_state not in closure:
                    closure.add(new_state)
                    queue.append(new_state)

        print(f"Final ε-closure: {closure}")
        return frozenset(closure)

    def remove_epsilon(self):
        print("\n=== Converting ε-NFA to NFA (Removing ε-transitions) ===")
        nfa_transitions = defaultdict(lambda: defaultdict(set))

        for state in self.states:
            closure = self.epsilon_closure({state})
            print(f"\nProcessing state {state}:")

            for symbol in self.alphabet - {'ε'}:
                moved = set()
                for s in closure:
                    moved.update(self.transitions.get(s, {}).get(symbol, set()))
                print(f"  On '{symbol}': {closure} → {moved}")

                new_states = self.epsilon_closure(moved)
                nfa_transitions[state][symbol] = new_states
                print(f"  Final transition: {state} --{symbol}--> {new_states}")

        new_accept = set()
        for state in self.states:
            closure = self.epsilon_closure({state})
            if any(s in self.accept_states for s in closure):
                new_accept.add(state)

        return {
            'type': 'NFA',
            'states': self.states,
            'alphabet': self.alphabet - {'ε'},
            'transitions': nfa_transitions,
            'start_state': self.start_state,
            'accept_states': new_accept
        }

    def to_dfa(self):
        print("\n=== Converting ε-NFA to DFA ===")
        dfa_start = self.epsilon_closure({self.start_state})
        dfa_states = [dfa_start]
        dfa_transitions = {}
        state_map = {dfa_start: 'S0'}
        queue = deque([dfa_start])
        state_counter = 1

        while queue:
            current = queue.popleft()
            print(f"\nProcessing DFA State: {state_map[current]} = {current}")
            dfa_transitions[state_map[current]] = {}

            for symbol in self.alphabet - {'ε'}:
                moved = self.move(current, symbol)
                new_state = self.epsilon_closure(moved)
                print(f"  On '{symbol}': Move → {moved}, ε-closure → {new_state}")

                if not new_state:
                    dfa_transitions[state_map[current]][symbol] = 'DEAD'
                    print("    → Dead State")
                    continue

                if new_state not in state_map:
                    state_map[new_state] = f'S{state_counter}'
                    state_counter += 1
                    queue.append(new_state)
                    print(f"    → New DFA State: {state_map[new_state]}")

                dfa_transitions[state_map[current]][symbol] = state_map[new_state]

        dfa_accept = [state_map[s] for s in state_map if any(q in self.accept_states for q in s)]
        if any('DEAD' in t.values() for t in dfa_transitions.values()):
            dfa_transitions['DEAD'] = {s: 'DEAD' for s in self.alphabet - {'ε'}}

        return {
            'type': 'DFA',
            'states': list(state_map.values()) + (['DEAD'] if 'DEAD' in dfa_transitions else []),
            'alphabet': list(self.alphabet - {'ε'}),
            'transitions': dfa_transitions,
            'start_state': state_map[dfa_start],
            'accept_states': dfa_accept
        }

    def move(self, states, symbol):
        result = set()
        for state in states:
            result.update(self.transitions.get(state, {}).get(symbol, set()))
        return result

    def visualize(self, automaton, title):
        dot = Digraph()
        dot.attr(rankdir='LR', label=title)
        dot.node('start', shape='none', label='')
        dot.edge('start', automaton['start_state'])

        for state in automaton['states']:
            shape = 'doublecircle' if state in automaton['accept_states'] else 'circle'
            dot.node(state, shape=shape)

        for from_state, trans in automaton['transitions'].items():
            for symbol, to_state in trans.items():
                dot.edge(from_state, str(to_state), label=symbol)

        dot.render(title, format='png', cleanup=True)
        print(f"\nVisualization saved as '{title}.png'")


def simulate_dfa(dfa, input_string):
    current_state = dfa['start_state']
    print(f"\nStart at: {current_state}")

    for symbol in input_string:
        if symbol not in dfa['alphabet']:
            print(f"Invalid symbol: {symbol} — Not in DFA alphabet!")
            return False
        print(f"On '{symbol}', move from {current_state} → {dfa['transitions'][current_state].get(symbol, 'DEAD')}")
        current_state = dfa['transitions'][current_state].get(symbol, 'DEAD')

    print(f"Final State: {current_state}")
    return current_state in dfa['accept_states']


# Example Usage
if __name__ == "__main__":
    # Example ε-NFA (Accepts strings ending with "01")
    enfa = EpsilonNFAConverter(
        states={'q0', 'q1', 'q2'},
        alphabet={'0', '1'},
        transitions={
            'q0': {'0': {'q0'}, 'ε': {'q1'}},
            'q1': {'1': {'q2'}},
            'q2': {'0': {'q2'}, '1': {'q2'}}
        },
        start_state='q0',
        accept_states={'q2'}
    )

    choice = input("Convert to:\n1. NFA (Remove ε)\n2. DFA + Test String\nEnter choice (1/2): ").strip()

    if choice == '1':
        result = enfa.remove_epsilon()
        enfa.visualize(result, 'nfa_output')
    elif choice == '2':
        result = enfa.to_dfa()
        enfa.visualize(result, 'dfa_output')

        input_str = input("\nEnter string to test (e.g., 0101): ").strip()
        if simulate_dfa(result, input_str):
            print("\n✅ String accepted by DFA.")
        else:
            print("\n❌ String rejected by DFA.")
    else:
        print("Invalid choice!")
