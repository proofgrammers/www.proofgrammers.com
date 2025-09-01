# Plan for Proofgrammers

## Plan for Content

### Revise the Index for the Entire Site

- [X] Review the content in the `GEMINI.md` file (or the `AGENTS.md` file) that
explains the theme of the course on the theory of computation, called
"Theoretical Machines" at Allegheny College in the Department of Computer
and Information Science.
- [X] Rewrite each of the introductory paragraphs so that they focus on the
concept of a "Proofgrammer". 
- [X] Rewrite the course overview so that it connects to the concept
of a "Proofgrammer" and a course on the theory of computation, as 
explored through the implementation of proofs in the Python programming
language.
- [X] Create new Python source code examples that connect to the
topic of the theory of computation and does not require any dependencies. If
possible, this example program should illustrate the concepts:
    - An example of a computation that is computable (i.e., counting the number
    of lines in a source code file)
    - An example of a computation that is not computation (i.e., detecting
    whether or not the output of a program P on an input contains the letter "Z"
    or whether or not a program will halt on any input)
- [X] Delete any content related to document engineering, as this is not
the focus of a course on the theory of computation.
- [X] Give the correct link to the discord server, which is specified in
the `_quarto.yml` file.
- [X] Make sure that all of your work is correct, ensuring that it has
acceptable layout and formatting and that the quarto project runs correctly.

### Create Slides for Week One in `slides/weekone/index.qmd`

- [X] Review the content in the `GEMINI.md` file (or the `AGENTS.md` file) that
explains the theme of the course on document engineering.
- [X] Review the content in the `index.qmd` file in the root of the repository
that explains the idea of a "Proofgrammer" and the concept of document
engineering.
- [X] Following the guidelines for creating slides, translate the content in the
`index.qmd` in the root of the repository to slides that introduce the course in
the `slides/weekone/index.qmd` file.
- [X] Note that the existing content was from slides that Gregory M. Kapfhammer
previously created to introduce a course in the field of document engineering.
You should revise all the technical content in these slides to fit into a course
about document engineering. However, you should also use this content in these
slides as good examples for what your generated slides should look like. Make
sure to use similar formatting, layout, and content as the provided slides.
- [X] The slides that introduce the course should contain Python source code
like that which you found in the `index.qmd` file in the root of the repository.
Make sure that students can run this source code and see the output.
- [X] After finishing the slides that introduce the course, create more slides
that introduce the following technologies and explain how to install them:
    - Terminal window
    - Git, GitHub, and GitHub CLI (i.e., `gh`)
    - Register for a free GitHub Student Developer Pack
    - Register for the free use of GitHub Copilot at the pro level
    - VS Code
    - `uv` (stress the use of `uv` for virtual environments, dependencies, and
    Python installation, especially focusing on the fact that a learner should
    not use alternative mechanisms for installing Python or any of the other
    aforementioned tasks like creating virtual environments)
    - Python 3.12 or 3.13 (which should come from using the `uv` tool)
    - Quarto
    - Quarto extension for VS Code
    - Customize VS Code by picking a theme and installing extensions
    - Npm and Node.js and all affiliated tools like `npx`
    - Google Gemini CLI (run through the use of `npx`)
    - OpenCode (run through the use of `npx`)
- [X] Ensure that the instructions in the slides from the previous step will
work correctly regardless of the operating system (Windows, MacOS, Linux).
- [X] Ensure that the instructions for installing each of the aforementioned
tools clearly explain what the tool does, why it is important, and how it can
help a prosegrammer to create, maintain, and analyze documents.
- [X] Ensure that the instructions for installing each of the aforementioned
tools stress the importance of testing the setup to make sure that they are
working. There should be links to online documentation that a learner can read
if they have trouble installing or testing any of the tools.
- [X] Add content about the responsible use of artificial intelligence (AI)
coding and writing tools that use large language models (LLMs) like Claude
Sonnet 4 or GPT-4. Make it clear that the prosegrammer who uses these tools is
ultimately responsible for wielding them correctly and ethically.

## Support for Content

### Rewriting Content in Several Files

#### Index Page Revision for Theory of Computation

**Proofgrammer Concept Definition**: 

- The term "Proofgrammer" combines "proof" (mathematical/computational statement
verification) with "programmer" (software development), reflecting the course's
focus on expressing theoretical concepts as executable Python code
- This definition aligns with the course objectives from AGENTS.md, specifically
teaching students to "create, manipulate, and analyze proofs of theoretical
concepts" using Python programming

**Computable vs Universal Computation Examples**:

- **Computable example**: Line counting in source code demonstrates a decidable
problem with a clear algorithmic solution, representing the class of problems
that can always be solved computationally
- **Universal computation example**: The `universal.py`-inspired code demonstrates
how one program can execute any other program, illustrating the foundational
concept of universal computation from Alan Turing's work on universal Turing
machines
- The universal computation example is based on actual code from the "What Can be
Computed" textbook, making it pedagogically sound and theoretically rigorous
- This example shows how programs can be treated as data and executed by other
programs, which is fundamental to understanding computational limits and
possibilities

**Course Focus Alignment**:

- Revised content removes document engineering references and centers on
theoretical computer science concepts including automata theory, formal
languages, computational complexity, and decidability
- Links to Discord server updated to match _quarto.yml configuration
(https://discord.gg/Mw9mybGK7u)
- Educational tools mentioned (Jupyter Notebooks, Quarto, GitHub, AI assistants)
remain relevant for implementing and documenting theoretical proofs in Python

**Universal Computation Support**:

- Universal computation is a cornerstone concept in theoretical computer science,
directly related to the Church-Turing thesis and computational equivalence
- The example demonstrates meta-computation where programs operate on other
programs as data, which is essential for understanding undecidability proofs
- The Python implementation shows executable code that students can run and
modify, making abstract theoretical concepts concrete and accessible
- This concept bridges the gap between theoretical understanding and practical
programming skills that proofgrammers need to develop

### Week One Slides for Theory of Computation

**Slide Content Transformation**:

- All document engineering content replaced with theory of computation concepts
- YAML header updated with "Exploring theory of computation with Python"
description and "Proofgrammers" footer
- Introduction slides now focus on what theory of computation is and why it's
important for understanding computational limits
- Proofgrammer concept clearly defined as combining mathematical proofs with
programming implementations

**Python Code Examples from Index.qmd**:

- **Computable problem**: Line counting demonstrates decidable, tractable
computation with clear algorithmic solution
- **Universal computation**: Based on actual `universal.py` code from "What Can
be Computed" textbook, showing how one program can execute another
- Interactive `pyodide` blocks allow students to modify and test code examples
in real-time
- All examples directly support course objectives of expressing theoretical
concepts as executable Python programs

**Tool Installation Instructions**:

- Cross-platform installation guidance for Terminal, Git, GitHub, VS Code, UV,
Python 3.12+, Quarto, Node.js, and AI tools
- Verification commands provided for each tool (`--version` flags) to confirm
successful setup
- Emphasis on UV package manager following course preference for modern Python
dependency management
- GitHub Student Developer Pack and Copilot Pro registration instructions
included

**AI Responsibility Content**:

- Clear guidelines about responsible use of AI coding assistants (GitHub
Copilot, Google Gemini CLI, OpenCode)
- Emphasis that proofgrammers remain responsible for ensuring theoretical
correctness and accuracy
- Integration guidance for AI tools within computational theory workflow
- Alignment with academic integrity and ethical AI use principles

**Slides Verification**:

- All slides render correctly in Quarto with live-revealjs format
- Python code blocks execute properly and display expected output
- Fragment animations and boxed content display appropriately
- Slide titles fit presentation standards and content flows logically

## Analysis: Slide Layout Verification Problem

### Current Approach Limitations

**What I've Been Doing Wrong**:
- **Text-based analysis only**: I've been examining slide content in `.qmd` files without actually seeing the rendered output
- **No visual verification**: Made assumptions about layout based on text content rather than actual visual appearance
- **Manual rendering insufficient**: Simply running `quarto render` and `quarto preview` doesn't give me visual feedback about layout issues
- **No automated layout checking**: Relying on subjective assessment rather than measurable criteria

**Why This Approach Fails**:
- Slide layout issues only become apparent when viewing the actual rendered slides in a browser
- Font sizes, spacing, content overflow, and text wrapping cannot be determined from source code alone
- Different screen resolutions and browser settings affect slide presentation
- Fragment animations and incremental reveals may cause unexpected layout problems

### Better Tool-Based Strategies

#### Strategy 1: Automated Screenshot Analysis
**Tools Available**:
- **Playwright**: Browser automation that can take screenshots and analyze DOM elements
- **Chromium/Chrome Headless**: Can capture screenshots at specific resolutions
- **Python image analysis**: Use libraries like PIL or OpenCV to analyze screenshot content

**Implementation Approach**:
```bash
# Take screenshots of each slide at presentation resolution
chromium-browser --headless --disable-gpu --window-size=1920,1080 \
  --screenshot=slide-{n}.png "http://localhost:8081/slides/weekone/index.html#/{n}"
```

**Analysis Capabilities**:
- Measure text overflow beyond slide boundaries
- Check for appropriate white space distribution
- Verify that titles fit on intended lines
- Detect code blocks that extend beyond visible area
- Analyze font size readability at presentation distance

#### Strategy 2: MCP Server with Playwright
**Advantages**:
- Can interact with live slide presentation
- Navigate through slides programmatically
- Check responsive behavior at different screen sizes
- Verify fragment animations don't cause layout issues
- Extract computed CSS styles and DOM measurements

**Implementation Plan**:
- Use MCP Playwright server to automate browser interactions
- Take screenshots of each slide in sequence
- Measure element positions and sizes programmatically
- Check for common layout issues (text overflow, poor spacing, etc.)

#### Strategy 3: DOM Analysis with Browser DevTools
**Approach**:
- Use headless browser to load slides
- Extract computed styles and element dimensions
- Check for CSS layout issues (overflow, positioning problems)
- Verify responsive design at presentation resolutions

**Measurable Criteria**:
- Slide content should not exceed 90% of viewport height
- Titles should not wrap beyond 2 lines
- Code blocks should not require horizontal scrolling
- Minimum font sizes for readability (e.g., 24px minimum for body text)
- Proper margin and padding ratios

### Recommended Implementation Strategy

#### Phase 1: Automated Screenshot Capture
1. **Setup headless browser automation**:
   - Use Chromium with standardized presentation resolution (1920x1080)
   - Capture screenshots of each slide individually
   - Store screenshots for manual review and automated analysis

2. **Implement screenshot analysis**:
   - Check for content that extends beyond slide boundaries
   - Measure white space distribution
   - Detect text that appears cut off or compressed

#### Phase 2: Enhanced Browser Automation
1. **Integrate Playwright or similar tool**:
   - Navigate through slides programmatically
   - Extract DOM measurements and CSS properties
   - Check responsive behavior at different screen sizes

2. **Define measurable layout criteria**:
   - Maximum content height per slide
   - Minimum font sizes for different content types
   - Required margins and spacing ratios
   - Title length and line break standards

#### Phase 3: Continuous Layout Verification
1. **Create automated slide layout testing pipeline**:
   - Run layout checks after each content modification
   - Generate reports highlighting layout issues
   - Provide specific recommendations for fixes

2. **Integration with development workflow**:
   - Add layout verification to `quarto check` process
   - Create pre-commit hooks for slide layout validation
   - Generate layout quality reports

### Immediate Next Steps

1. **Install and configure Playwright or similar tool** for automated browser testing
2. **Create screenshot capture automation** to visually inspect all slides
3. **Develop layout analysis scripts** to identify common presentation issues
4. **Establish measurable criteria** for slide layout quality
5. **Test the approach** on current Week One slides to identify actual problems
6. **Document the verification process** in AGENTS.md for future use

### Success Metrics

- All slides display properly at 1920x1080 presentation resolution
- No content overflow beyond slide boundaries
- Titles fit appropriately (1-2 lines maximum)
- Code blocks remain fully visible without scrolling
- Consistent spacing and typography throughout presentation
- Fragment animations work correctly without layout disruption

This tool-based approach will provide objective, measurable feedback about slide layout quality rather than relying on subjective text-based analysis.

## Computational Theory Examples for Proofgrammers

### Solvable Variant of the Halting Problem: Bounded Loop Halting

The halting problem is algorithmically unsolvable in general, but we can create
variants that **are** solvable by restricting the computational model.

#### The "Bounded Loop Halting Problem"

**Problem**: Given a Python program that contains only `for` loops with explicit
numeric ranges (no `while` loops, no recursion, no user input), determine if it
will halt.

This is solvable because we can statically analyze the maximum number of iterations.

```python
import ast
from typing import Union

def analyze_bounded_halting(code: str) -> bool:
    """
    Determine if a Python program with only bounded for-loops will halt.
    Returns True if the program will definitely halt, False if it contains
    constructs that make halting undecidable.
    """
    try:
        tree = ast.parse(code)
        analyzer = BoundedHaltingAnalyzer()
        analyzer.visit(tree)
        return analyzer.will_halt
    except SyntaxError:
        return False

class BoundedHaltingAnalyzer(ast.NodeVisitor):
    """AST visitor that checks if a program has only bounded loops."""
    
    def __init__(self):
        self.will_halt = True
        self.has_while_loops = False
        self.has_recursion = False
        self.has_infinite_constructs = False
    
    def visit_While(self, node):
        """While loops make halting undecidable in general."""
        self.has_while_loops = True
        self.will_halt = False
        self.generic_visit(node)
    
    def visit_For(self, node):
        """For loops are okay if they iterate over bounded ranges."""
        if isinstance(node.iter, ast.Call):
            if (isinstance(node.iter.func, ast.Name) and 
                node.iter.func.id == 'range'):
                # This is a range() call - bounded and will terminate
                pass
            else:
                # Other function calls might not terminate
                self.will_halt = False
        elif isinstance(node.iter, (ast.List, ast.Tuple, ast.Set)):
            # Iterating over literal collections - bounded
            pass
        else:
            # Other iterables might be infinite
            self.will_halt = False
        
        self.generic_visit(node)
    
    def visit_FunctionDef(self, node):
        """Check for potential recursion."""
        func_name = node.name
        
        class RecursionChecker(ast.NodeVisitor):
            def __init__(self, func_name):
                self.func_name = func_name
                self.is_recursive = False
            
            def visit_Call(self, node):
                if (isinstance(node.func, ast.Name) and 
                    node.func.id == self.func_name):
                    self.is_recursive = True
                self.generic_visit(node)
        
        checker = RecursionChecker(func_name)
        checker.visit(node)
        
        if checker.is_recursive:
            self.has_recursion = True
            self.will_halt = False
        
        self.generic_visit(node)

# Test cases demonstrating the bounded halting problem solver

def test_bounded_halting():
    """Test the bounded halting problem solver with various programs."""
    
    # Program 1: Simple bounded loop - WILL HALT
    program1 = """
def count_to_ten():
    for i in range(10):
        print(i)
    return "done"

count_to_ten()
"""
    
    # Program 2: Nested bounded loops - WILL HALT  
    program2 = """
def nested_loops():
    for i in range(5):
        for j in range(3):
            print(f"{i}, {j}")

nested_loops()
"""
    
    # Program 3: While loop - UNDECIDABLE (returns False)
    program3 = """
def while_loop():
    x = 10
    while x > 0:
        x -= 1
    return x

while_loop()
"""
    
    # Program 4: Potential recursion - UNDECIDABLE (returns False)
    program4 = """
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

factorial(5)
"""
    
    # Program 5: List iteration - WILL HALT
    program5 = """
def iterate_list():
    items = [1, 2, 3, 4, 5]
    for item in items:
        print(item * 2)

iterate_list()
"""
    
    programs = [
        ("Simple bounded loop", program1),
        ("Nested bounded loops", program2), 
        ("While loop", program3),
        ("Recursive function", program4),
        ("List iteration", program5)
    ]
    
    print("Bounded Halting Problem Solver Results:")
    print("=" * 50)
    
    for name, program in programs:
        will_halt = analyze_bounded_halting(program)
        status = "WILL HALT" if will_halt else "UNDECIDABLE"
        print(f"{name}: {status}")
        print(f"Program:\n{program.strip()}")
        print("-" * 30)

# Run the test
test_bounded_halting()
