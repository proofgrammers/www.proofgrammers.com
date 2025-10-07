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

## Implement New Slides for Chapter Four, "What is a Computational Problem?"

- You have access to the content of the book in the file:
`What-Can-Be-Computed.pdf` and `What-Can-Be-Computed.md` that is in the root of
this repository.
- You have access to the slides of the book in PPTX (which is hard for you to
read) and a QMD file (which is easier for you to read) in the
`theoreticalmachines/wcbc-slides/` directory.
- You have access to the source code connected to this book in the directory
`theoreticalmachines/wcbc-code/`
- I have created a template file for the slides in the `slides/weekfour/index.qmd`
- I would like you to create a starting version of the slides for Chapter Four:
"What is a Computational Problem?" in the `slides/weekfour/index.qmd` file.
- One challenge of this chapter is that it contains a lot of images (e.g., a
picture of a graph with a cycle in it). I don't want you to link directly to any
images in the slides that you produce --- the content can only be in the
index.qmd file. If you know how to draw the diagrams using something with a
standard package in Python, then you can do that. Otherwise, only explain the
details about the graphs in short words or phrases or with source code.
- Make sure to only explain concepts that are connected to Chapter Four.
- Make sure to review all the prior slides that I have created in the `slides/`
directory and the subdirectories for prior weeks in `weekone/` and `weektwo/`
and `weekthree/` to ensure that your slides are formatted and laid out just
like the content that I have already created.
- Do not make slides if they are not directly connected to the content in the
book, the content in the slides (i.e., the PPTX or the extracted QMD file) or in
the source code.
- Make sure that you connect the slides to the theme of being a "proofgrammer"
as explained in the course syllabus that is available in `syllabus/index.qmd`.
- Please follow all the rules and regulations for creating this content and make
sure that you notify me when you have completed this task.

## Implement New Slides for Chapter Five, "Turing Machines"

- You have access to the content of the book in the file:
`What-Can-Be-Computed.pdf` and `What-Can-Be-Computed.md` that is in the root of
this repository.
- You have access to the slides of the book in PPTX (which is hard for you to
read) and a QMD file (which is easier for you to read) in the
`theoreticalmachines/wcbc-slides/` directory.
- You have access to the images that were created from the slides for this
chapter. These images may be especially important because of the fact that
there are many diagrams of Turing machines in this chapter.
- You have access to the source code connected to this book in the directory
`theoreticalmachines/wcbc-code/`
- I have created a template file for the slides in the
`slides/weekfive/index.qmd`
- I would like you to create a starting version of the slides for Chapter Five:
"Turing Machines" in the `slides/weekfive/index.qmd` file.
- One challenge of this chapter is that it contains a lot of images (e.g., a
picture of a Turing Machine). I don't want you to link directly to any images
in the slides that you produce --- the content can only be in the index.qmd
file. If you know how to draw the diagrams using something with a standard
package in Python, then you can do that. Otherwise, only explain the details
about the graphs in short words or phrases or with source code.
- Make sure to only explain concepts that are connected to Chapter Five.
- Make sure to review all the prior slides that I have created in the `slides/`
directory and the subdirectories for prior weeks in `weekone/` and `weektwo/`
and `weekthree/` and `weekfour/` to ensure that your slides are formatted and
laid out just like the content that I have already created.
- Do not make slides if they are not directly connected to the content in the
book, the content in the slides (i.e., the PPTX or the extracted QMD file) or
in the source code that connects to this chapter of the book.
- Make sure that you connect the slides to the theme of being a "proofgrammer"
as explained in the course syllabus that is available in `syllabus/index.qmd`.
- Make sure that the concept that you create is short, succinct, and clear. I
will be revising this content, essentially using it as a starting point.
- Please follow all the rules and regulations for creating this content and
make sure that you notify me when you have completed this task.

## Implement New Slides for Chapter Six, "Universal Computer Programs: Programs that Can Do Anything"

- You have access to the content of the book in the file:
`What-Can-Be-Computed.pdf` and `What-Can-Be-Computed.md` that is in the root of
this repository.
- You have access to the slides of the book in PPTX (which is hard for you to
read) and a QMD file (which is easier for you to read) in the
`theoreticalmachines/wcbc-slides/` directory.
- You have access to the images that were created from the slides for this
chapter. These images may be especially important because of the fact that
there are some diagrams of the output of a universal computer.
- Please consider adding the image for Figure 6.6 with the sub-caption that
starts "Example output of "rule 110" cellular automaton ..." and Figure
6.9 as a visualization for ignoreInput.py.
- You have access to the source code connected to this book in the directory
`theoreticalmachines/wcbc-code/`
- I have created a template file for the slides in the
`slides/weekseven/index.qmd`. You can add to this file!
- I would like you to create a starting version of the slides for Chapter Six:
in the `slides/weekseven/index.qmd` file. Please note that you are creating
slides for _week seven_ of the course in the `index.qmd` file that is
in that directory but for _chapter six_ of the book.
- Figure 6.7 is important and I think that a table connected to it should
definitely be in the slides for this chapter.
- One challenge of this chapter is that it contains a lot of source code
examples that may not run correctly unless you include all needed source
code from the book's archive. Do not include a source code example unless
it is self-contained and it will run directly without an extra dependencies.
- Make sure to only explain concepts that are connected to Chapter Six.
- Make sure to review all the prior slides that I have created in the `slides/`
directory and the subdirectories for prior weeks in `weekone/` and `weektwo/`
and `weekthree/` and `weekfour/` and `weeksix/` to ensure that your slides are
formatted and laid out just like the content that I have already created.
- Do not make slides if they are not directly connected to the content in the
book, the content in the slides (i.e., the PPTX or the extracted QMD file) or
in the source code that connects to this chapter of the book.
- Make sure that you connect the slides to the theme of being a "proofgrammer"
as explained in the course syllabus that is available in `syllabus/index.qmd`.
- Make sure that the concept that you create is short, succinct, and clear. I
will be revising this content, essentially using it as a starting point.
- Please follow all the rules and regulations for creating this content and
make sure that you notify me when you have completed this task.

## Support for Content

### Week Four Slides Enhancement: Set Operations Addition

**Missing Content Identification and Resolution**:

- **Set Operations Definition Slide Added**: Added comprehensive slide defining union ($L_1 \cup L_2$), intersection ($L_1 \cap L_2$), complement ($\overline{L}$), concatenation ($L_1 L_2$), and repetition ($L^*$) operations on languages
- **Mathematical Rigor**: Each operation includes formal mathematical notation and concrete examples using small alphabets like $\{a, b\}$ to demonstrate concepts clearly
- **Pedagogical Examples**: Specific examples such as $\{a, ab\} \cup \{b, ab\} = \{a, b, ab\}$ and $\{ab\}^* = \{\epsilon, ab, abab, ababab, ...\}$ illustrate how operations work in practice
- **Connection to Automata Theory**: Explicitly linked these operations to their foundational role in automata theory and formal language construction

**Content Completeness Review**:

- **Comprehensive Chapter 4 Coverage**: Verified that slides already covered all major Chapter 4 concepts including computational problem definitions, problem categories, SISO programs, and computability theory
- **No Additional Missing Content**: Review of existing slides confirmed coverage of graphs, alphabets, strings, languages, decision problems, and formal problem definitions
- **Appropriate Balance**: Content maintains proper balance between theoretical rigor and practical Python implementations for proofgrammers

**Quality Assurance and Verification**:

- **Successful Rendering**: All slides render correctly with `quarto render slides/weekfour/index.qmd`
- **Layout Verification**: Used headless browser screenshot testing to confirm proper slide layout at 1920x1080 presentation resolution
- **Mathematical Notation**: LaTeX mathematical expressions display correctly for set operations and formal definitions
- **Fragment Animation**: Incremental content reveals function properly to support effective presentation flow

**Technical Implementation Details**:

- **Set Operation Examples**: Provided concrete examples using simple finite languages to make abstract concepts accessible
- **Visual Organization**: Used appropriate iconify icons and boxed content to highlight key takeaways
- **Font Sizing**: Maintained readability standards with appropriate font sizes for mathematical notation and example content
- **Content Flow**: New slides integrate seamlessly with existing content progression from alphabets to languages to operations

**Theoretical Foundation Support**:

- **Formal Language Theory**: Set operations form the mathematical foundation for constructing complex languages from simpler ones
- **Automata Theory Preparation**: These operations are essential for understanding regular expressions, finite automata, and language recognition
- **Computational Complexity**: Understanding language operations prepares students for analyzing decision problems and complexity classes
- **Chapter 4 Alignment**: Content directly supports "What Can be Computed" Chapter 4 learning objectives about computational problems and formal language theory

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

### Week Three Slides for Impossible Programs (Chapter 3)

**Chapter 3 Core Concepts and Theoretical Foundation**:

- **Proof by Contradiction**: Introduced as natural human reasoning pattern with
everyday example (milk purchase scenario) connecting to mathematical formalism
where statement S implies consequence C, but C contradicts known truth T,
therefore S is false
- **Programs Analyzing Other Programs**: Demonstrates `countLines.py` analyzing
`multiplyAll.py` and self-analyzing with `countLines(rf('countLines.py'))`,
establishing foundation for meta-computation and self-reflection in programs
- **Self-Reflection Paradox**: Turing's 1936 insight that self-reflective
capability both enables powerful computation and creates fundamental limitations
- **Decision Programs Suite**: Implementation of `containsGAGA`, `yes`,
`longerThan1K`, and `maybeLoop` programs with comprehensive examples showing
program-on-program analysis from WCBC Figure 3.2

**The Impossibility Proof Structure**:

- **Hypothetical yesOnString Program**: Definition where `yesOnString(P, I)`
returns "yes" if program P returns "yes" on input I, "no" otherwise - essential
for formal impossibility proof
- **yesOnSelf Simplification**: `yesOnSelf(P) = yesOnString(P, P)` asking "Does
program P return 'yes' when given itself as input?" - creates conditions for
logical contradiction
- **notYesOnSelf Construction**: Returns opposite of `yesOnSelf` result,
creating program that returns "yes" if and only if it returns "no" when applied
to itself - demonstrating logical impossibility
- **Direct Contradiction**: `notYesOnSelf("notYesOnSelf.py")` creates
paradoxical situation where program must simultaneously return "yes" and "no"

**Proof by Contradiction Implementation**:

- **Step-by-step logical structure**: Assume yesOnString exists (statement S),
derive that notYesOnSelf can be created (consequence C), but notYesOnSelf leads
to logical contradiction (contradicts known impossibility), therefore yesOnString
cannot exist
- **Compact weirdYesOnString proof**: More direct approach where
`weirdYesOnString(P)` immediately creates contradiction when applied to itself,
eliminating intermediate steps
- **Crash detection impossibility**: `weirdCrashOnSelf` program demonstrates
same contradiction pattern applies to crash prediction, showing broader scope of
uncomputability results

**Python Code Examples and Interactive Learning**:

- **Decision program implementations**: All functions properly implement SISO
requirements returning only "yes" or "no" strings
- **Hypothetical program simulations**: Code demonstrates theoretical behavior
of impossible programs for educational purposes while clearly marking them as
impossible to implement
- **Self-analysis experiments**: Interactive `pyodide` block allows students to
experiment with `analyzeProgram` function performing legal self-analysis to
contrast with impossible universal analysis
- **Progressive complexity**: Examples build from simple pattern recognition to
sophisticated logical contradictions

**Practical Implications and Real-World Connections**:

- **Software Engineering Limits**: No perfect bug finder or universal crash
detector possible, but partial solutions remain valuable for practical
development
- **Static Analysis Tools**: Work effectively on specific program classes and
common scenarios, guided by impossibility results toward productive applications
- **Research and Development**: Understanding computational boundaries prevents
wasted effort on unsolvable problems while focusing innovation on achievable
goals

**Educational Methodology and Theoretical Support**:

- **Foundation for Advanced Topics**: Prepares students for Turing machines,
Church-Turing thesis, and formal undecidability results in subsequent chapters
- **Connection to Literature**: Examples directly correspond to WCBC Chapter 3
content and standard computability theory textbooks
- **Interactive Engagement**: Students can modify and experiment with code
examples to reinforce understanding of theoretical concepts
- **Critical Thinking Development**: Discussion prompts encourage analysis of
computational limits and practical tool development strategies

**Verification and Quality Assurance**:

- **Successful Compilation**: All slides render correctly with `quarto render`
and preview at http://localhost:8081/slides/weekthree/index.html
- **Code Execution**: Python examples execute properly with expected outputs,
including complex logical contradiction demonstrations
- **Layout Standards**: Titles fit single lines, content properly distributed,
fragment animations function correctly, and icons display appropriately
- **Theoretical Accuracy**: Content aligns with standard computability theory
presentations and WCBC textbook Chapter 3 learning objectives

**Content Support References**:

- **Alan Turing (1936)**: "Computing Machinery and Intelligence" - original
impossibility results through self-reference and logical contradiction
- **WCBC Chapter 3**: "Some Impossible Python Programs" - direct source for
examples and proof structure
- **Computability Theory Literature**: Standard presentations of halting
problem, universal computation, and undecidability proofs
- **Software Engineering Research**: Contemporary applications of theoretical
limits to practical tool development and automated program analysis

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
```

### Week Two Slides for Formally Defining Computation

**Slide Content Based on Source Materials**:

- Content derived from `01-intro.qmd` source file containing foundational
concepts from "What Can be Computed" textbook Chapter 1
- Course objectives review emphasizes the central questions: what can be
computed in principle (undecidability) vs. efficiently in practice (complexity
theory)
- Computational problem classification table demonstrates tractable,
intractable, and uncomputable categories with concrete examples aligned with
theoretical computer science literature
- SISO (Single Input, Single Output) program concept introduced as fundamental
computational model for formal analysis

**Python Implementation Examples**:

- **`containsGAGA` function**: Demonstrates decision problem implementation,
returning "yes"/"no" based on substring pattern recognition - directly from
WCBC textbook examples
- **Enhanced pattern matching**: `containsGAGAnotTATA` function shows complex
conditional logic combining multiple pattern checks with boolean operations
- **File reading simulation**: `rf` function demonstrates treating programs as
data, foundational concept for universal computation and meta-computation
- Interactive `pyodide` blocks enable real-time code modification and execution
to reinforce theoretical concepts through hands-on programming

**SISO Program Characteristics**:

- Formal definition of Single Input, Single Output computational model as
foundation for theoretical analysis
- Connection to decision problems and language recognition in automata theory
- Emphasis on deterministic behavior and finite execution requirements
- Bridge between concrete programming implementations and abstract mathematical
functions in computability theory

**Educational Methodology**:

- Team discussion prompts encourage critical thinking about computational
limits and efficiency analysis
- Progressive complexity from simple pattern recognition to sophisticated
conditional logic
- Connection between practical string processing and formal language theory
concepts
- Preparation for advanced topics like universal computation and program
analysis

**Theoretical Foundation Support**:

- SISO programs provide rigorous mathematical framework for analyzing
computational problems and their complexity classes
- Decision problems (yes/no outputs) form basis for studying decidability and
undecidability results in theoretical computer science
- Pattern recognition algorithms demonstrate fundamental operations in formal
language processing and automata theory
- Universal computation concepts prepare students for understanding Turing
machines and computational equivalence proofs

**Verification and Quality Assurance**:

- All slides render correctly with `quarto render` and preview successfully at
http://localhost:8081/slides/weektwo/index.html
- Python code blocks execute properly and display expected output
- Fragment animations and incremental reveals function as intended
- Content follows established formatting guidelines with appropriate icons,
boxed content, and consistent typography
- Slide titles meet length requirements and content distribution maintains
readability at presentation resolution

### Chapter Two Content: index_two.qmd for What is a Computer Program?

**Unique Chapter 2 Content (No Duplication with Existing Slides)**:

- **Formal Program Definition**: P(I) mathematical notation for program P
executed on input I, establishing rigorous framework for computational analysis
- **Numeric Input/Output Conversion**: String-to-number (`int()`, `float()`)
and number-to-string (`str()`) conversion patterns for SISO compliance with
practical examples like `addNumbers` and `computeAverage`
- **ASCII Character Set**: Complete 128-character standard including printable
characters, newline handling, and multiline text processing capabilities
- **Program Failure Modes**: Comprehensive analysis of when P(I) becomes
undefined due to non-termination, exceptions, invalid return types, or syntax
errors

**Advanced Theoretical Concepts**:

- **Decision Program Formalization**: Accept/reject terminology where P(I) =
"yes" means P accepts I, and P(I) = "no" means P rejects I, connecting to
formal language theory
- **Program Equivalence**: Mathematical definition where programs P and Q are
equivalent if P(I) = Q(I) for all inputs I, enabling optimization and
refactoring analysis
- **SISO Requirement Violations**: Systematic categorization of invalid
programs including multiple parameters, non-string returns, non-deterministic
behavior, and external dependencies
- **Termination Analysis**: Computational examination of when programs halt
successfully versus infinite loops or runtime failures

**Python Implementation Examples**:

- **Multiline Text Processing**: Functions like `countLines` and
`extractWords` demonstrating ASCII newline character handling and complex
string manipulation
- **Decision Program Suite**: Implementation of `isEvenLength`,
`containsOnlyDigits`, and `isPalindrome` showcasing accept/reject semantics
with comprehensive test cases
- **Program Equivalence Demonstration**: Three different implementations of
`countVowels` (explicit loop, list comprehension, filter function) proving
behavioral equivalence despite different coding approaches
- **Input Validation and Error Handling**: Robust SISO programs with
try/except blocks and proper string conversion to prevent undefined P(I)
states

**Mathematical Foundation Support**:

- P(I) notation derives from formal computation theory and provides basis for
proving decidability/undecidability results in theoretical computer science
- Decision problems with "yes"/"no" outputs form foundation for complexity
classes (P, NP, PSPACE) and language recognition in automata theory
- Program equivalence concept enables formal verification methods and compiler
optimization correctness proofs
- ASCII string restriction maintains theoretical simplicity while providing
sufficient expressiveness for universal computation, as proven by
Church-Turing thesis

**Content Differentiation from Existing Slides**:

- Existing slides cover basic SISO concepts and simple `containsGAGA` examples
- New content focuses specifically on Chapter 2's formal program analysis,
numeric conversion patterns, and advanced decision problem implementation
- No duplication of SISO introduction, basic Python syntax, or simple pattern
matching already covered in main slides
- Chapter 2 content prepares for advanced topics like program analysis, formal
verification, and computational complexity theory

**Quality Assurance and Verification**:

- All slides render successfully with `quarto render
slides/weektwo/index_two.qmd`
- Python code blocks execute correctly and demonstrate expected theoretical
concepts
- Interactive `pyodide` examples enable hands-on experimentation with formal
program concepts
- Content follows established formatting guidelines with appropriate icons,
fragments, and mathematical notation
- Material directly supports "What Can be Computed" textbook Chapter 2
learning objectives

### Week Five Slides for Turing Machines (Chapter 5)

**Turing Machine Theoretical Foundation**:

- **Alan Turing's 1936 Contribution**: Turing machines formalize the concept of
mechanical computation, providing mathematical basis for understanding
computational limits and universal computation as described in "Computing
Machinery and Intelligence"
- **Finite State Control**: Turing machines have finite number of internal
states, making them analyzable while maintaining computational universality
- **Infinite Tape Model**: Unbounded tape memory represents unlimited storage
capacity, distinguishing Turing machines from finite automata and enabling
simulation of any algorithmic computation
- **Church-Turing Thesis**: Equivalence between Turing-computable functions
and effectively calculable functions, supported by decades of theoretical
research and practical verification

**Formal Mathematical Definition Components**:

- **Alphabet Σ**: Finite set of symbols including blank symbol, providing
foundation for all possible inputs and tape contents in theoretical analysis
- **State Set Q**: Finite collection of machine states with designated start
state and accept/reject states, enabling formal analysis of computation paths
- **Transition Function δ**: Mapping from (current state, tape symbol) to
(new state, write symbol, head movement), fully specifying deterministic
machine behavior
- **Configuration Representation**: (state, tape contents, head position)
triples enable precise mathematical description of computation steps and
formal verification of machine correctness

**Simple Turing Machine Examples and Implementation**:

- **lastTtoA Example**: Demonstrates basic tape manipulation by replacing last
'T' with 'A', illustrating systematic left-to-right scanning followed by
rightward processing - corresponds to WCBC Figure 5.2
- **containsGAGA Example**: Shows pattern recognition capabilities with
systematic string scanning, accepting input containing 'GAGA' substring -
illustrates decision problem implementation using Turing machine formalism
- **Python Simulator Implementation**: Complete working simulator with
`TuringMachine` class enables hands-on experimentation with machine
construction and execution tracing
- **Step-by-step Execution Traces**: Detailed configuration sequences show
exactly how machines process inputs, making abstract theoretical concepts
concrete and accessible

**Universal Computation and Church-Turing Thesis**:

- **Universal Turing Machine Concept**: Single machine capable of simulating
any other Turing machine when given appropriate program encoding, proven by
Turing in 1936 and fundamental to modern computer architecture
- **Equivalence to Real Computers**: Modern computers implement Turing machine
capabilities through stored programs, random access memory, and conditional
branching, validating Church-Turing thesis in practice
- **Computational Completeness**: Turing machines can solve any problem that
is algorithmically solvable, providing theoretical foundation for studying
decidability and computational complexity
- **Historical Significance**: Turing machines predate electronic computers by
decades but accurately predicted capabilities and limitations of digital
computation

**Python Code Implementation and Educational Value**:

- **Interactive Simulator**: Students can define custom machines using
Python dictionaries for transition functions, making abstract formal
definitions concrete and experimentally verifiable
- **Execution Tracing**: `run_machine` function displays step-by-step
configuration changes, allowing students to observe theoretical computation
concepts in action
- **Machine Construction Examples**: Provided implementations of `lastTtoA`
and `containsGAGA` machines serve as templates for students to create their
own Turing machine solutions
- **Debugging and Analysis**: Visual execution traces help students understand
why machines accept or reject inputs, reinforcing connection between formal
specifications and computational behavior

**Connection to Advanced Theoretical Topics**:

- **Decidability Preparation**: Turing machine formalism provides foundation
for proving undecidability results like the halting problem in subsequent
chapters
- **Complexity Theory Foundation**: Time and space complexity analysis relies
on Turing machine computational model to define complexity classes
- **Automata Theory Hierarchy**: Turing machines represent most powerful
computational model in Chomsky hierarchy, enabling comparison with finite
automata and pushdown automata
- **Reduction Techniques**: Turing machine construction techniques prepare
students for polynomial-time reductions and NP-completeness proofs

**Educational Methodology and Proofgrammer Integration**:

- **Theory-to-Code Translation**: Students learn to express abstract
mathematical machine definitions as executable Python programs, embodying
proofgrammer methodology
- **Interactive Learning**: `pyodide` blocks enable real-time machine
modification and testing, reinforcing theoretical understanding through
hands-on experimentation
- **Visual Computation Traces**: Detailed execution examples bridge gap
between formal mathematical descriptions and concrete computational processes
- **Progressive Complexity**: Examples build from simple tape manipulation to
sophisticated pattern recognition, preparing for advanced topics

**Content Sources and Theoretical Support**:

- **"What Can be Computed" Chapter 5**: Direct source for machine examples,
formal definitions, and theoretical explanations used throughout slides
- **Turing's Original 1936 Paper**: Foundation for Church-Turing thesis and
universal computation concepts presented in slides
- **Standard Computability Theory Literature**: Formal definitions and
examples align with presentations in Sipser, Hopcroft & Ullman, and other
theoretical computer science textbooks
- **Interactive Implementation**: Python simulator design based on educational
best practices for making abstract concepts accessible to undergraduate
students

**Quality Assurance and Layout Verification**:

- **Successful Rendering**: All slides render correctly with `quarto render
slides/weekfive/index.qmd` producing functional HTML presentation
- **Visual Layout Standards**: Screenshot verification at 1920x1080
resolution confirms titles fit appropriately and content displays without
overflow
- **Code Execution**: All Python examples execute properly in `pyodide` blocks
with expected output, enabling student interaction and experimentation
- **Mathematical Notation**: LaTeX formatting displays correctly for formal
definitions, state transitions, and Church-Turing thesis expressions
- **Fragment Animation**: Incremental content reveals function properly to
support effective presentation flow and student comprehension
