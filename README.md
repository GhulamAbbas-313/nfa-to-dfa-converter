# NFA-ε to DFA Converter

A comprehensive PyQt5-based application for converting Non-deterministic Finite Automata with epsilon transitions (NFA-ε) to Deterministic Finite Automata (DFA).

## Features

✨ **Core Functionality:**
- Convert epsilon-NFA to NFA (remove epsilon transitions)
- Convert NFA to DFA using subset construction algorithm
- Visual representation of automata using Graphviz
- Interactive transition table display

🎨 **User Interface:**
- Modern PyQt5 GUI with dark/light theme toggle
- Collapsible sidebar navigation
- Multi-page dashboard with tabs
- Real-time automaton visualization
- Responsive design

💾 **File Operations:**
- Save/Load automata in JSON format
- Export automata configurations
- Example automata included

## Installation

### Requirements
- Python 3.7+
- PyQt5
- Graphviz

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/nfa-to-dfa-converter.git
cd nfa-to-dfa-converter
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Install Graphviz (System-wide)

**Windows:**
```bash
choco install graphviz
# or download from: https://graphviz.org/download/
```

**Mac:**
```bash
brew install graphviz
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install graphviz
```

## Usage

### Run the Application
```bash
python tocproject_gui.py
```

### Login Credentials
- **Username:** admin
- **Password:** admin

### Workflow

1. **Input NFA-ε**: Create a new epsilon-NFA by entering:
   - States (comma-separated)
   - Alphabet symbols
   - Start state
   - Accept states
   - Transitions (from_state, symbol, to_state)

2. **Convert to NFA**: Remove epsilon transitions from your automaton

3. **Convert to DFA**: Apply subset construction algorithm

4. **Visualize**: View the automaton diagrams

5. **Export**: Save your automata as JSON files

## Example Automata

### Simple Binary Recognition
States: `q0,q1,q2`
Alphabet: `a,b,ε`
Start State: `q0`
Accept States: `q2`
Transitions:
```
q0,ε,q1
q0,a,q0
q1,b,q1
q1,b,q2
q2,a,q2
```

## Project Structure

```
nfa-to-dfa-converter/
├── tocproject_gui.py       # Main application
├── requirements.txt        # Dependencies
├── README.md              # This file
├── LICENSE                # MIT License
├── examples/              # Example automata JSON files
└── docs/                  # Documentation
```

## Architecture

### Core Classes

**EpsilonNFAConverter**
- Manages epsilon-NFA representation
- Implements epsilon closure computation
- Converts NFA-ε → NFA → DFA

**LoginScreen**
- Authentication dialog
- Gradient UI styling
- Keyboard shortcuts

**NFAConverterDashboard**
- Main application window
- Tab-based navigation
- Theme switching

**AutomatonWidget**
- Graphviz visualization
- SVG rendering

## Theme Support

- 🌙 **Dark Mode**: For comfortable night-time coding
- ☀️ **Light Mode**: Professional appearance

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Enter` | Login / Confirm |
| `Esc` | Cancel |

## Troubleshooting

### Graphviz Not Found
Make sure Graphviz is installed system-wide and accessible from command line:
```bash
dot -V
```

### PyQt5 Import Error
```bash
pip install --upgrade PyQt5
```

### Login Issues
Default credentials are `admin`/`admin`. You can modify this in the `handle_login()` method.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created by: **GhulamAbbas-313**

## Acknowledgments

- PyQt5 for the GUI framework
- Graphviz for automata visualization
- Theory of Computation concepts

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Happy Converting! 🚀**
