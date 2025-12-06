import sys
import json
import os
from collections import defaultdict, deque
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from graphviz import Digraph
from PyQt5.QtSvg import QSvgWidget

# Core NFA Converter Class
class EpsilonNFAConverter:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = defaultdict(lambda: defaultdict(set))
        self.start_state = None
        self.accept_states = set()
        
    def add_transition(self, from_state, symbol, to_state):
        """Add a transition to the epsilon-NFA"""
        self.states.add(from_state)
        self.states.add(to_state)
        if symbol != 'ε':
            self.alphabet.add(symbol)
        self.transitions[from_state][symbol].add(to_state)
    
    def set_start_state(self, state):
        """Set the start state"""
        self.start_state = state
        self.states.add(state)
    
    def add_accept_state(self, state):
        """Add an accept state"""
        self.accept_states.add(state)
        self.states.add(state)
    
    def epsilon_closure(self, states):
        """Compute epsilon closure of a set of states"""
        closure = set(states)
        stack = list(states)
        
        while stack:
            state = stack.pop()
            for next_state in self.transitions[state]['ε']:
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        
        return closure
    
    def convert_to_nfa(self):
        """Convert epsilon-NFA to NFA by removing epsilon transitions"""
        nfa = EpsilonNFAConverter()
        nfa.states = self.states.copy()
        nfa.alphabet = self.alphabet.copy()
        nfa.start_state = self.start_state
        
        for state in self.states:
            state_closure = self.epsilon_closure({state})
            
            if state_closure & self.accept_states:
                nfa.accept_states.add(state)
            
            for symbol in self.alphabet:
                reachable = set()
                for s in state_closure:
                    for next_state in self.transitions[s][symbol]:
                        reachable.update(self.epsilon_closure({next_state}))
                
                if reachable:
                    nfa.transitions[state][symbol] = reachable
        
        return nfa
    
    def convert_to_dfa(self):
        """Convert epsilon-NFA to DFA using subset construction"""
        nfa = self.convert_to_nfa()
        
        dfa_states = {}
        dfa_transitions = {}
        dfa_accept_states = set()
        unmarked_states = deque()
        
        start_closure = frozenset(self.epsilon_closure({self.start_state}))
        dfa_states[start_closure] = f"q0"
        dfa_start_state = "q0"
        unmarked_states.append(start_closure)
        
        if start_closure & self.accept_states:
            dfa_accept_states.add("q0")
        
        state_counter = 1
        
        while unmarked_states:
            current_set = unmarked_states.popleft()
            current_name = dfa_states[current_set]
            
            for symbol in self.alphabet:
                next_set = set()
                for state in current_set:
                    next_set.update(nfa.transitions[state][symbol])
                
                if next_set:
                    next_set_frozen = frozenset(next_set)
                    
                    if next_set_frozen not in dfa_states:
                        new_state_name = f"q{state_counter}"
                        dfa_states[next_set_frozen] = new_state_name
                        unmarked_states.append(next_set_frozen)
                        state_counter += 1
                        
                        if next_set_frozen & self.accept_states:
                            dfa_accept_states.add(new_state_name)
                    
                    if current_name not in dfa_transitions:
                        dfa_transitions[current_name] = {}
                    dfa_transitions[current_name][symbol] = dfa_states[next_set_frozen]
        
        dfa = EpsilonNFAConverter()
        dfa.states = set(dfa_states.values())
        dfa.alphabet = self.alphabet.copy()
        dfa.start_state = dfa_start_state
        dfa.accept_states = dfa_accept_states
        
        for from_state, transitions in dfa_transitions.items():
            for symbol, to_state in transitions.items():
                dfa.transitions[from_state][symbol].add(to_state)
        
        return dfa, dfa_states

# Login Screen
class LoginScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NFA-ε to DFA Converter - Login")
        self.showFullScreen()
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.setup_ui()
        self.apply_styles()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # Main container
        container = QFrame()
        container.setObjectName("loginContainer")
        container_layout = QVBoxLayout(container)
        
        # Logo/Title
        title = QLabel("🚀 NFA-ε Converter")
        title.setAlignment(Qt.AlignCenter)
        title.setObjectName("loginTitle")
        
        # Login form
        form_widget = QWidget()
        form_layout = QFormLayout(form_widget)
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter username")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter password")
        self.password_input.setEchoMode(QLineEdit.Password)
        
        form_layout.addRow("Username:", self.username_input)
        form_layout.addRow("Password:", self.password_input)
        
        # Buttons
        button_layout = QHBoxLayout()
        self.login_btn = QPushButton("Login")
        self.login_btn.setObjectName("loginButton")
        self.login_btn.clicked.connect(self.handle_login)
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        
        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(self.login_btn)
        
        # Add to container
        container_layout.addWidget(title)
        container_layout.addSpacing(20)
        container_layout.addWidget(form_widget)
        container_layout.addSpacing(20)
        container_layout.addLayout(button_layout)
        
        layout.addWidget(container)
        
        # Connect Enter key
        self.password_input.returnPressed.connect(self.handle_login)
        
    def apply_styles(self):
        self.setStyleSheet("""
            QDialog {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #667eea, stop:1 #764ba2);
            }
            
            #loginContainer {
                background: rgba(255, 255, 255, 0.95);
                border-radius: 15px;
                padding: 30px;
                margin: 20px;
            }
            
            #loginTitle {
                font-size: 24px;
                font-weight: bold;
                color: #333;
                margin-bottom: 10px;
            }
            
            QLineEdit {
                padding: 12px;
                border: 2px solid #ddd;
                border-radius: 8px;
                font-size: 14px;
                background: white;
            }
            
            QLineEdit:focus {
                border-color: #667eea;
            }
            
            QPushButton {
                padding: 12px 24px;
                border: none;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
            }
            
            #loginButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #667eea, stop:1 #764ba2);
                color: white;
            }
            
            #loginButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #5a6fd8, stop:1 #6a4190);
            }
            
            QPushButton:!#loginButton {
                background: #f0f0f0;
                color: #333;
            }
            
            QPushButton:!#loginButton:hover {
                background: #e0e0e0;
            }
        """)
    
    def handle_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        
        # Simple authentication (you can enhance this)
        if username == "admin" and password == "admin":
            self.accept()
        elif username and password:  # Allow any non-empty credentials
            self.accept()
        else:
            QMessageBox.warning(self, "Login Failed", "Please enter valid credentials\n\nHint: Use 'admin' / 'admin' or any non-empty values")

# Custom Navigation Button
class NavButton(QPushButton):
    def __init__(self, text, icon=None):
        super().__init__(text)
        self.setMinimumHeight(45)
        if icon:
            self.setIcon(self.style().standardIcon(icon))
        self.setStyleSheet("""
            QPushButton {
                text-align: left;
                padding: 12px 20px;
                border: none;
                background: transparent;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background: rgba(255, 255, 255, 0.1);
                border-left: 4px solid #667eea;
            }
            QPushButton:pressed {
                background: rgba(255, 255, 255, 0.2);
            }
        """)

# Automaton Visualization Widget using Graphviz
class AutomatonWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.svg_widget = QSvgWidget()
        self.layout.addWidget(self.svg_widget)
        
    def render_automaton(self, automaton, title="Automaton"):
        if not automaton or not automaton.states:
            # Clear the widget if no automaton
            self.svg_widget.load(QByteArray())
            return
            
        dot = Digraph(comment=title)
        dot.attr(rankdir='LR')
        
        # Add states
        for state in automaton.states:
            if state in automaton.accept_states:
                dot.node(state, shape='doublecircle')
            else:
                dot.node(state)
                
            if state == automaton.start_state:
                # Add invisible start node with arrow to start state
                dot.node('start', shape='point', style='invis')
                dot.edge('start', state)
        
        # Add transitions
        for from_state in automaton.transitions:
            for symbol in automaton.transitions[from_state]:
                for to_state in automaton.transitions[from_state][symbol]:
                    dot.edge(from_state, to_state, label=symbol)
        
        # Render the graph
        svg_data = dot.pipe(format='svg')
        self.svg_widget.load(QByteArray(svg_data))

# Main Dashboard
class NFAConverterDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_enfa = EpsilonNFAConverter()
        self.current_nfa = None
        self.current_dfa = None
        self.is_dark_mode = False
        self.sidebar_collapsed = False
        
        self.setWindowTitle("NFA-ε to DFA Converter Dashboard")
        self.setGeometry(100, 100, 1400, 900)
        
        self.setup_ui()
        self.apply_light_theme()
        
    def setup_ui(self):
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Sidebar
        self.setup_sidebar()
        main_layout.addWidget(self.sidebar)
        
        # Main content area
        self.setup_main_content()
        main_layout.addWidget(self.main_content)
        
        # Top navigation bar
        self.setup_top_nav()
    
    def setup_sidebar(self):
        self.sidebar = QFrame()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setFixedWidth(250)
        
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(0)
        
        # Sidebar header
        header = QFrame()
        header.setObjectName("sidebarHeader")
        header.setFixedHeight(60)
        header_layout = QHBoxLayout(header)
        
        # Collapse button
        self.collapse_btn = QPushButton("☰")
        self.collapse_btn.setFixedSize(40, 40)
        self.collapse_btn.clicked.connect(self.toggle_sidebar)
        
        # App title in sidebar
        sidebar_title = QLabel("NFA Converter")
        sidebar_title.setObjectName("sidebarTitle")
        
        header_layout.addWidget(self.collapse_btn)
        header_layout.addWidget(sidebar_title)
        header_layout.addStretch()
        
        # Navigation buttons
        nav_widget = QWidget()
        nav_layout = QVBoxLayout(nav_widget)
        nav_layout.setContentsMargins(10, 20, 10, 20)
        
        # Create navigation buttons
        self.nav_buttons = {
            'input': NavButton("📝 Input NFA-ε", QStyle.SP_FileDialogDetailedView),
            'nfa': NavButton("🔄 Convert to NFA", QStyle.SP_ArrowRight),
            'dfa': NavButton("⚡ Convert to DFA", QStyle.SP_ArrowForward),
            'visualize': NavButton("📊 Visualizations", QStyle.SP_ComputerIcon),
            'table': NavButton("📋 Transition Tables", QStyle.SP_FileDialogListView),
            'save': NavButton("💾 Save/Load", QStyle.SP_DialogSaveButton),
        }
        
        for button in self.nav_buttons.values():
            nav_layout.addWidget(button)
            
        nav_layout.addStretch()
        
        # Theme toggle
        self.theme_btn = QPushButton("🌙 Dark Mode")
        self.theme_btn.clicked.connect(self.toggle_theme)
        nav_layout.addWidget(self.theme_btn)
        
        sidebar_layout.addWidget(header)
        sidebar_layout.addWidget(nav_widget)
        
        # Connect navigation
        self.nav_buttons['input'].clicked.connect(lambda: self.show_page('input'))
        self.nav_buttons['nfa'].clicked.connect(lambda: self.show_page('nfa'))
        self.nav_buttons['dfa'].clicked.connect(lambda: self.show_page('dfa'))
        self.nav_buttons['visualize'].clicked.connect(lambda: self.show_page('visualize'))
        self.nav_buttons['table'].clicked.connect(lambda: self.show_page('table'))
        self.nav_buttons['save'].clicked.connect(lambda: self.show_page('save'))
    
    def setup_top_nav(self):
        # Top navigation bar
        self.top_nav = QFrame()
        self.top_nav.setObjectName("topNav")
        self.top_nav.setFixedHeight(60)
        
        top_nav_layout = QHBoxLayout(self.top_nav)
        
        # App title
        app_title = QLabel("🚀 NFA-ε to DFA Converter Dashboard")
        app_title.setObjectName("appTitle")
        
        # Status indicator
        self.status_label = QLabel("Ready")
        self.status_label.setObjectName("statusLabel")
        
        top_nav_layout.addWidget(app_title)
        top_nav_layout.addStretch()
        top_nav_layout.addWidget(self.status_label)
        
        # Add to main content
        self.main_content.layout().insertWidget(0, self.top_nav)
    
    def setup_main_content(self):
        self.main_content = QFrame()
        self.main_content.setObjectName("mainContent")
        
        main_layout = QVBoxLayout(self.main_content)
        main_layout.setContentsMargins(20, 10, 20, 20)
        
        # Stacked widget for different pages
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)
        
        # Create pages
        self.create_input_page()
        self.create_nfa_page()
        self.create_dfa_page()
        self.create_visualization_page()
        self.create_table_page()
        self.create_save_page()
        
        # Show input page by default
        self.stacked_widget.setCurrentIndex(0)
    
    def create_input_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        # Title
        title = QLabel("📝 Input NFA-ε")
        title.setObjectName("pageTitle")
        layout.addWidget(title)
        
        # Input form
        form_widget = QWidget()
        form_layout = QFormLayout(form_widget)
        
        self.states_input = QLineEdit()
        self.states_input.setPlaceholderText("e.g., q0,q1,q2,q3")
        
        self.alphabet_input = QLineEdit()
        self.alphabet_input.setPlaceholderText("e.g., a,b,ε")
        
        self.start_state_input = QLineEdit()
        self.start_state_input.setPlaceholderText("e.g., q0")
        
        self.accept_states_input = QLineEdit()
        self.accept_states_input.setPlaceholderText("e.g., q2,q3")
        
        self.transitions_input = QTextEdit()
        self.transitions_input.setPlaceholderText("Format: from,symbol,to (one per line)\nExample:\nq0,a,q1\nq0,ε,q2\nq1,b,q3")
        self.transitions_input.setMaximumHeight(150)
        
        form_layout.addRow("States:", self.states_input)
        form_layout.addRow("Alphabet:", self.alphabet_input)
        form_layout.addRow("Start State:", self.start_state_input)
        form_layout.addRow("Accept States:", self.accept_states_input)
        form_layout.addRow("Transitions:", self.transitions_input)
        
        # Buttons
        button_layout = QHBoxLayout()
        load_btn = QPushButton("📂 Load from File")
        load_btn.clicked.connect(self.load_from_file)
        
        create_btn = QPushButton("✅ Create NFA-ε")
        create_btn.setObjectName("primaryButton")
        create_btn.clicked.connect(self.create_enfa)
        
        clear_btn = QPushButton("🗑️ Clear")
        clear_btn.clicked.connect(self.clear_inputs)
        
        button_layout.addWidget(load_btn)
        button_layout.addWidget(clear_btn)
        button_layout.addStretch()
        button_layout.addWidget(create_btn)
        
        layout.addWidget(form_widget)
        layout.addLayout(button_layout)
        layout.addStretch()
        
        # Example button
        example_btn = QPushButton("📖 Load Example")
        example_btn.clicked.connect(self.load_example)
        layout.addWidget(example_btn)
        
        self.stacked_widget.addWidget(page)
    
    def create_nfa_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        title = QLabel("🔄 NFA (ε-transitions removed)")
        title.setObjectName("pageTitle")
        layout.addWidget(title)
        
        # Control buttons
        button_layout = QHBoxLayout()
        convert_nfa_btn = QPushButton("🔄 Convert to NFA")
        convert_nfa_btn.setObjectName("primaryButton")
        convert_nfa_btn.clicked.connect(self.convert_to_nfa)
        
        save_nfa_btn = QPushButton("💾 Save NFA")
        save_nfa_btn.clicked.connect(lambda: self.save_automaton('nfa'))
        
        button_layout.addWidget(convert_nfa_btn)
        button_layout.addWidget(save_nfa_btn)
        button_layout.addStretch()
        
        layout.addLayout(button_layout)
        
        # NFA info display
        self.nfa_info_text = QTextEdit()
        self.nfa_info_text.setReadOnly(True)
        self.nfa_info_text.setMaximumHeight(200)
        layout.addWidget(self.nfa_info_text)
        
        # Visualization
        self.nfa_canvas = AutomatonWidget()
        layout.addWidget(self.nfa_canvas)
        
        self.stacked_widget.addWidget(page)
    
    def create_dfa_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        title = QLabel("⚡ DFA (Subset Construction)")
        title.setObjectName("pageTitle")
        layout.addWidget(title)
        
        # Control buttons
        button_layout = QHBoxLayout()
        convert_dfa_btn = QPushButton("⚡ Convert to DFA")
        convert_dfa_btn.setObjectName("primaryButton")
        convert_dfa_btn.clicked.connect(self.convert_to_dfa)
        
        save_dfa_btn = QPushButton("💾 Save DFA")
        save_dfa_btn.clicked.connect(lambda: self.save_automaton('dfa'))
        
        button_layout.addWidget(convert_dfa_btn)
        button_layout.addWidget(save_dfa_btn)
        button_layout.addStretch()
        
        layout.addLayout(button_layout)
        
        # DFA info display
        self.dfa_info_text = QTextEdit()
        self.dfa_info_text.setReadOnly(True)
        self.dfa_info_text.setMaximumHeight(200)
        layout.addWidget(self.dfa_info_text)
        
        # Visualization
        self.dfa_canvas = AutomatonWidget()
        layout.addWidget(self.dfa_canvas)
        
        self.stacked_widget.addWidget(page)
    
    def create_visualization_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        title = QLabel("📊 Automaton Visualizations")
        title.setObjectName("pageTitle")
        layout.addWidget(title)
        
        # Tabs for different automata
        tab_widget = QTabWidget()
        
        # ε-NFA tab
        enfa_tab = QWidget()
        enfa_layout = QVBoxLayout(enfa_tab)
        self.enfa_canvas = AutomatonWidget()
        enfa_layout.addWidget(self.enfa_canvas)
        tab_widget.addTab(enfa_tab, "ε-NFA")
        
        # NFA tab
        nfa_tab = QWidget()
        nfa_layout = QVBoxLayout(nfa_tab)
        self.vis_nfa_canvas = AutomatonWidget()
        nfa_layout.addWidget(self.vis_nfa_canvas)
        tab_widget.addTab(nfa_tab, "NFA")
        
        # DFA tab
        dfa_tab = QWidget()
        dfa_layout = QVBoxLayout(dfa_tab)
        self.vis_dfa_canvas = AutomatonWidget()
        dfa_layout.addWidget(self.vis_dfa_canvas)
        tab_widget.addTab(dfa_tab, "DFA")
        
        layout.addWidget(tab_widget)
        
        # Refresh button
        refresh_btn = QPushButton("🔄 Refresh All")
        refresh_btn.clicked.connect(self.refresh_visualizations)
        layout.addWidget(refresh_btn)
        
        self.stacked_widget.addWidget(page)
    
    def create_table_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        title = QLabel("📋 Transition Tables")
        title.setObjectName("pageTitle")
        layout.addWidget(title)
        
        # Tabs for different tables
        table_tabs = QTabWidget()
        
        # ε-NFA table
        self.enfa_table = QTableWidget()
        table_tabs.addTab(self.enfa_table, "ε-NFA Table")
        
        # NFA table
        self.nfa_table = QTableWidget()
        table_tabs.addTab(self.nfa_table, "NFA Table")
        
        # DFA table
        self.dfa_table = QTableWidget()
        table_tabs.addTab(self.dfa_table, "DFA Table")
        
        layout.addWidget(table_tabs)
        
        # Update button
        update_tables_btn = QPushButton("🔄 Update Tables")
        update_tables_btn.clicked.connect(self.update_transition_tables)
        layout.addWidget(update_tables_btn)
        
        self.stacked_widget.addWidget(page)
    
    def create_save_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        title = QLabel("💾 Save & Load Operations")
        title.setObjectName("pageTitle")
        layout.addWidget(title)
        
        # Save section
        save_group = QGroupBox("Save Operations")
        save_layout = QVBoxLayout(save_group)
        
        save_button_layout = QHBoxLayout()
        save_enfa_btn = QPushButton("💾 Save ε-NFA")
        save_enfa_btn.clicked.connect(lambda: self.save_automaton('enfa'))
        
        save_nfa_btn = QPushButton("💾 Save NFA")
        save_nfa_btn.clicked.connect(lambda: self.save_automaton('nfa'))
        
        save_dfa_btn = QPushButton("💾 Save DFA") 
        save_dfa_btn.clicked.connect(lambda: self.save_automaton('dfa'))
        
        save_button_layout.addWidget(save_enfa_btn)
        save_button_layout.addWidget(save_nfa_btn)
        save_button_layout.addWidget(save_dfa_btn)
        
        save_layout.addLayout(save_button_layout)
        
        # Load section
        load_group = QGroupBox("Load Operations")
        load_layout = QVBoxLayout(load_group)
        
        load_btn = QPushButton("📂 Load ε-NFA from File")
        load_btn.clicked.connect(self.load_from_file)
        load_layout.addWidget(load_btn)
        
        layout.addWidget(save_group)
        layout.addWidget(load_group)
        layout.addStretch()
        
        self.stacked_widget.addWidget(page)
    
    def show_page(self, page_name):
        page_indices = {
            'input': 0, 'nfa': 1, 'dfa': 2, 
            'visualize': 3, 'table': 4, 'save': 5
        }
        if page_name in page_indices:
            self.stacked_widget.setCurrentIndex(page_indices[page_name])
            self.status_label.setText(f"Viewing: {page_name.replace('input', 'Input').title()}")
    
    def toggle_sidebar(self):
        self.sidebar_collapsed = not self.sidebar_collapsed
        if self.sidebar_collapsed:
            self.sidebar.setFixedWidth(60)
            for btn in self.nav_buttons.values():
                btn.setText("")
                btn.setIconSize(QSize(24, 24))
            self.collapse_btn.setText("→")
        else:
            self.sidebar.setFixedWidth(250)
            for name, btn in self.nav_buttons.items():
                if name == 'input': btn.setText("📝 Input NFA-ε")
                elif name == 'nfa': btn.setText("🔄 Convert to NFA")
                elif name == 'dfa': btn.setText("⚡ Convert to DFA")
                elif name == 'visualize': btn.setText("📊 Visualizations")
                elif name == 'table': btn.setText("📋 Transition Tables")
                elif name == 'save': btn.setText("💾 Save/Load")
                btn.setIconSize(QSize(16, 16))
            self.collapse_btn.setText("☰")
    
    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        if self.is_dark_mode:
            self.apply_dark_theme()
            self.theme_btn.setText("☀️ Light Mode")
        else:
            self.apply_light_theme()
            self.theme_btn.setText("🌙 Dark Mode")
    
    def apply_light_theme(self):
        self.setStyleSheet("""
            #sidebar {
                background-color: #2c3e50;
                color: white;
                border: none;
            }
            
            #sidebarHeader {
                background-color: #34495e;
                border: none;
            }
            
            #sidebarTitle {
                color: white;
                font-size: 16px;
                font-weight: bold;
            }
            
            #topNav {
                background-color: #f8f9fa;
                border-bottom: 1px solid #dee2e6;
            }
            
            #appTitle {
                color: #333;
                font-size: 18px;
                font-weight: bold;
            }
            
            #statusLabel {
                color: #6c757d;
                font-size: 14px;
            }
            
            #mainContent {
                background-color: #f8f9fa;
                border: none;
            }
            
            #pageTitle {
                font-size: 24px;
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 20px;
            }
            
            QGroupBox {
                border: 1px solid #dee2e6;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 15px;
                font-weight: bold;
            }
            
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px;
            }
            
            QTableWidget {
                background-color: white;
                border: 1px solid #dee2e6;
            }
            
            QTextEdit {
                background-color: white;
                border: 1px solid #dee2e6;
            }
            
            QLineEdit {
                background-color: white;
                border: 1px solid #dee2e6;
                padding: 5px;
            }
            
            QPushButton {
                background-color: #e9ecef;
                border: 1px solid #dee2e6;
                padding: 5px 10px;
                min-width: 80px;
            }
            
            #primaryButton {
                background-color: #007bff;
                color: white;
                border: 1px solid #006fe6;
            }
            
            #primaryButton:hover {
                background-color: #0069d9;
            }
            
            QPushButton:hover {
                background-color: #d1e7ff;
            }
        """)
    
    def apply_dark_theme(self):
        self.setStyleSheet("""
            QWidget {
                color: #e0e0e0;
            }
            
            #sidebar {
                background-color: #1e1e1e;
                border: none;
            }
            
            #sidebarHeader {
                background-color: #252526;
                border: none;
            }
            
            #sidebarTitle {
                color: #e0e0e0;
                font-size: 16px;
                font-weight: bold;
            }
            
            #topNav {
                background-color: #252526;
                border-bottom: 1px solid #333;
            }
            
            #appTitle {
                color: #e0e0e0;
                font-size: 18px;
                font-weight: bold;
            }
            
            #statusLabel {
                color: #a0a0a0;
                font-size: 14px;
            }
            
            #mainContent {
                background-color: #252526;
                border: none;
            }
            
            #pageTitle {
                font-size: 24px;
                font-weight: bold;
                color: #4fc3f7;
                margin-bottom: 20px;
            }
            
            QGroupBox {
                border: 1px solid #333;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 15px;
                font-weight: bold;
            }
            
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px;
                color: #e0e0e0;
            }
            
            QTableWidget {
                background-color: #333;
                border: 1px solid #444;
                color: #e0e0e0;
            }
            
            QTableWidget QHeaderView::section {
                background-color: #2d2d2d;
                color: #e0e0e0;
                border: 1px solid #444;
            }
            
            QTextEdit {
                background-color: #333;
                border: 1px solid #444;
                color: #e0e0e0;
            }
            
            QLineEdit {
                background-color: #333;
                border: 1px solid #444;
                padding: 5px;
                color: #e0e0e0;
            }
            
            QPushButton {
                background-color: #3d3d3d;
                border: 1px solid #444;
                padding: 5px 10px;
                min-width: 80px;
                color: #e0e0e0;
            }
            
            #primaryButton {
                background-color: #0d6efd;
                color: white;
                border: 1px solid #0b5ed7;
            }
            
            #primaryButton:hover {
                background-color: #0b5ed7;
            }
            
            QPushButton:hover {
                background-color: #4d4d4d;
            }
        """)
    
    def clear_inputs(self):
        self.states_input.clear()
        self.alphabet_input.clear()
        self.start_state_input.clear()
        self.accept_states_input.clear()
        self.transitions_input.clear()
        self.status_label.setText("Inputs cleared")
    
    def load_example(self):
        example = """
States: q0,q1,q2
Alphabet: a,b,ε
Start State: q0
Accept States: q2
Transitions:
q0,ε,q1
q0,a,q0
q1,b,q1
q1,b,q2
q2,a,q2
"""
        parts = example.strip().split('\n')
        self.states_input.setText(parts[1].split(': ')[1])
        self.alphabet_input.setText(parts[2].split(': ')[1])
        self.start_state_input.setText(parts[3].split(': ')[1])
        self.accept_states_input.setText(parts[4].split(': ')[1])
        self.transitions_input.setText('\n'.join(parts[6:]))
        self.status_label.setText("Example loaded")
    
    def load_from_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Load NFA-ε", "", 
                                                 "JSON Files (*.json);;All Files (*)", 
                                                 options=options)
        if file_name:
            try:
                with open(file_name, 'r') as f:
                    data = json.load(f)
                
                self.current_enfa = EpsilonNFAConverter()
                
                # Set states
                states = data.get('states', [])
                for state in states:
                    self.current_enfa.states.add(state)
                
                # Set alphabet
                alphabet = data.get('alphabet', [])
                for symbol in alphabet:
                    self.current_enfa.alphabet.add(symbol)
                
                # Set start state
                start_state = data.get('start_state')
                if start_state:
                    self.current_enfa.set_start_state(start_state)
                
                # Set accept states
                accept_states = data.get('accept_states', [])
                for state in accept_states:
                    self.current_enfa.add_accept_state(state)
                
                # Set transitions
                transitions = data.get('transitions', {})
                for from_state, symbol_transitions in transitions.items():
                    for symbol, to_states in symbol_transitions.items():
                        for to_state in to_states:
                            self.current_enfa.add_transition(from_state, symbol, to_state)
                
                # Update input fields
                self.states_input.setText(','.join(self.current_enfa.states))
                self.alphabet_input.setText(','.join(self.current_enfa.alphabet))
                self.start_state_input.setText(self.current_enfa.start_state)
                self.accept_states_input.setText(','.join(self.current_enfa.accept_states))
                
                # Format transitions for display
                transitions_text = []
                for from_state in self.current_enfa.transitions:
                    for symbol in self.current_enfa.transitions[from_state]:
                        for to_state in self.current_enfa.transitions[from_state]:
                            transitions_text.append(f"{from_state},{symbol},{to_state}")
                self.transitions_input.setText('\n'.join(transitions_text))
                
                self.status_label.setText(f"Loaded NFA-ε from {file_name}")
                self.refresh_visualizations()
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load file:\n{str(e)}")
    
    def create_enfa(self):
        try:
            # Clear current automaton
            self.current_enfa = EpsilonNFAConverter()
            
            # Process states
            states = [s.strip() for s in self.states_input.text().split(',') if s.strip()]
            if not states:
                raise ValueError("At least one state is required")
            
            # Process alphabet
            alphabet = [s.strip() for s in self.alphabet_input.text().split(',') if s.strip()]
            
            # Process start state
            start_state = self.start_state_input.text().strip()
            if not start_state:
                raise ValueError("Start state is required")
            if start_state not in states:
                raise ValueError("Start state must be in states list")
            
            # Process accept states
            accept_states = [s.strip() for s in self.accept_states_input.text().split(',') if s.strip()]
            for state in accept_states:
                if state not in states:
                    raise ValueError(f"Accept state {state} must be in states list")
            
            # Process transitions
            transitions = []
            for line in self.transitions_input.toPlainText().split('\n'):
                parts = [p.strip() for p in line.split(',') if p.strip()]
                if len(parts) == 3:
                    transitions.append(parts)
            
            # Build the NFA-ε
            for state in states:
                self.current_enfa.states.add(state)
            
            for symbol in alphabet:
                if symbol != 'ε':
                    self.current_enfa.alphabet.add(symbol)
            
            self.current_enfa.set_start_state(start_state)
            
            for state in accept_states:
                self.current_enfa.add_accept_state(state)
            
            for from_state, symbol, to_state in transitions:
                self.current_enfa.add_transition(from_state, symbol, to_state)
            
            # Update visualizations
            self.refresh_visualizations()
            self.status_label.setText("NFA-ε created successfully")
            
        except Exception as e:
            QMessageBox.warning(self, "Input Error", str(e))
    
    def convert_to_nfa(self):
        if not self.current_enfa.states:
            QMessageBox.warning(self, "Error", "Please create an NFA-ε first")
            return
        
        self.current_nfa = self.current_enfa.convert_to_nfa()
        
        # Display NFA info
        info = f"""NFA (ε-transitions removed):
States: {', '.join(self.current_nfa.states)}
Alphabet: {', '.join(self.current_nfa.alphabet)}
Start State: {self.current_nfa.start_state}
Accept States: {', '.join(self.current_nfa.accept_states)}

Transitions:"""
        
        for from_state in self.current_nfa.transitions:
            for symbol in self.current_nfa.transitions[from_state]:
                for to_state in self.current_nfa.transitions[from_state][symbol]:
                    info += f"\n{from_state} --{symbol}--> {to_state}"
        
        self.nfa_info_text.setPlainText(info)
        self.nfa_canvas.render_automaton(self.current_nfa, "NFA")
        self.status_label.setText("Converted to NFA successfully")
    
    def convert_to_dfa(self):
        if not self.current_enfa.states:
            QMessageBox.warning(self, "Error", "Please create an NFA-ε first")
            return
        
        self.current_dfa, state_mapping = self.current_enfa.convert_to_dfa()
        
        # Display DFA info
        info = f"""DFA (Subset Construction):
States: {', '.join(self.current_dfa.states)}
Alphabet: {', '.join(self.current_dfa.alphabet)}
Start State: {self.current_dfa.start_state}
Accept States: {', '.join(self.current_dfa.accept_states)}

State Mapping:"""
        
        for subset, name in state_mapping.items():
            states = ', '.join(subset)
            info += f"\n{name} = {{{states}}}"
        
        info += "\n\nTransitions:"
        
        for from_state in self.current_dfa.transitions:
            for symbol in self.current_dfa.transitions[from_state]:
                for to_state in self.current_dfa.transitions[from_state][symbol]:
                    info += f"\n{from_state} --{symbol}--> {to_state}"
        
        self.dfa_info_text.setPlainText(info)
        self.dfa_canvas.render_automaton(self.current_dfa, "DFA")
        self.status_label.setText("Converted to DFA successfully")
    
    def refresh_visualizations(self):
        self.enfa_canvas.render_automaton(self.current_enfa, "ε-NFA")
        self.vis_nfa_canvas.render_automaton(self.current_nfa, "NFA")
        self.vis_dfa_canvas.render_automaton(self.current_dfa, "DFA")
        self.update_transition_tables()
    
    def update_transition_tables(self):
        self.update_transition_table(self.enfa_table, self.current_enfa, "ε-NFA")
        self.update_transition_table(self.nfa_table, self.current_nfa, "NFA")
        self.update_transition_table(self.dfa_table, self.current_dfa, "DFA")
        self.status_label.setText("Transition tables updated")
    
    def update_transition_table(self, table, automaton, title):
        table.clear()
        
        if not automaton or not automaton.states:
            table.setRowCount(0)
            table.setColumnCount(0)
            return
        
        # Get all symbols (including epsilon for ε-NFA)
        symbols = sorted(automaton.alphabet)
        if isinstance(automaton, EpsilonNFAConverter) and title == "ε-NFA":
            symbols = ['ε'] + symbols
        
        # Setup table
        states = sorted(automaton.states)
        table.setRowCount(len(states))
        table.setColumnCount(len(symbols) + 1)  # +1 for state column
        
        # Set headers
        horizontal_headers = ["State"] + symbols
        table.setHorizontalHeaderLabels(horizontal_headers)
        
        vertical_headers = []
        for i, state in enumerate(states):
            # Mark start state with →
            prefix = "→ " if state == automaton.start_state else ""
            # Mark accept state with *
            suffix = " *" if state in automaton.accept_states else ""
            vertical_headers.append(f"{prefix}{state}{suffix}")
        
        table.setVerticalHeaderLabels(vertical_headers)
        
        # Fill transition cells
        for row, state in enumerate(states):
            # State label
            state_item = QTableWidgetItem(state)
            state_item.setFlags(state_item.flags() ^ Qt.ItemIsEditable)
            table.setItem(row, 0, state_item)
            
            for col, symbol in enumerate(symbols, 1):
                transitions = automaton.transitions[state].get(symbol, set())
                if transitions:
                    text = ", ".join(sorted(transitions))
                    item = QTableWidgetItem(text)
                    item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                    
                    # Highlight accept states
                    if any(s in automaton.accept_states for s in transitions):
                        item.setBackground(QColor(220, 255, 220))
                    
                    table.setItem(row, col, item)
        
        # Resize columns
        table.resizeColumnsToContents()
    
    def save_automaton(self, automaton_type):
        if automaton_type == 'enfa' and not self.current_enfa.states:
            QMessageBox.warning(self, "Error", "No ε-NFA to save")
            return
        elif automaton_type == 'nfa' and not self.current_nfa:
            QMessageBox.warning(self, "Error", "No NFA to save")
            return
        elif automaton_type == 'dfa' and not self.current_dfa:
            QMessageBox.warning(self, "Error", "No DFA to save")
            return
        
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, 
                                                  f"Save {automaton_type.upper()}", 
                                                  "", 
                                                  "JSON Files (*.json);;All Files (*)", 
                                                  options=options)
        if file_name:
            try:
                if not file_name.endswith('.json'):
                    file_name += '.json'
                
                automaton = {
                    'enfa': self.current_enfa,
                    'nfa': self.current_nfa,
                    'dfa': self.current_dfa
                }[automaton_type]
                
                data = {
                    'type': automaton_type.upper(),
                    'states': list(automaton.states),
                    'alphabet': list(automaton.alphabet),
                    'start_state': automaton.start_state,
                    'accept_states': list(automaton.accept_states),
                    'transitions': {}
                }
                
                for from_state in automaton.transitions:
                    data['transitions'][from_state] = {}
                    for symbol in automaton.transitions[from_state]:
                        data['transitions'][from_state][symbol] = list(automaton.transitions[from_state][symbol])
                
                with open(file_name, 'w') as f:
                    json.dump(data, f, indent=2)
                
                self.status_label.setText(f"Saved {automaton_type.upper()} to {file_name}")
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file:\n{str(e)}")

# Main Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Show login screen
    login = LoginScreen()
    if login.exec_() == QDialog.Accepted:
        dashboard = NFAConverterDashboard()
        dashboard.show()
        sys.exit(app.exec_())
    else:
        sys.exit()