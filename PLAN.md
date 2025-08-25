# Plan for Proofgrammers

## Plan for Content

### Revise the Index for the Entire Site

- [ ] Review the content in the `GEMINI.md` file (or the `AGENTS.md` file) that
explains the theme of the course on the theory of computation, called
"Theoretical Machines" at Allegheny College in the Department of Computer
and Information Science.
- [ ] Rewrite each of the introductory paragraphs so that they focus on the
concept of a "Proofgrammer". 
- [ ] Rewrite the course overview so that it connects to the concept
of a "Proofgrammer" and a course on the theory of computation, as 
explored through the implementation of proofs in the Python programming
language.
- [ ] Create new Python source code examples that connect to the
topic of the theory of computation and does not require any dependencies. If
possible, this example program should illustrate the concepts:
    - An example of a computation that is computable (i.e., counting the number
    of lines in a source code file)
    - An example of a computation that is not computation (i.e., detecting
    whether or not the output of a program P on an input contains the letter "Z"
    or whether or not a program will halt on any input)
- [ ] Delete any content related to document engineering, as this is not
the focus of a course on the theory of computation.
- [ ] Give the correct link to the discord server, which is specified in
the `_quarto.yml` file.
- [ ] Make sure that all of your work is correct, ensuring that it has
acceptable layout and formatting and that the quarto project runs correctly.

### Create Slides for Week One in `slides/weekone/index.qmd`

- [ ] Review the content in the `GEMINI.md` file (or the `AGENTS.md` file) that
explains the theme of the course on document engineering.
- [ ] Review the content in the `index.qmd` file in the root of the repository
that explains the idea of a "Proofgrammer" and the concept of document
engineering.
- [ ] Following the guidelines for creating slides, translate the content in the
`index.qmd` in the root of the repository to slides that introduce the course in
the `slides/weekone/index.qmd` file.
- [ ] Note that the existing content was from slides that Gregory M. Kapfhammer
previously created to introduce a course in the field of document engineering.
You should revise all the technical content in these slides to fit into a course
about document engineering. However, you should also use this content in these
slides as good examples for what your generated slides should look like. Make
sure to use similar formatting, layout, and content as the provided slides.
- [ ] The slides that introduce the course should contain Python source code
like that which you found in the `index.qmd` file in the root of the repository.
Make sure that students can run this source code and see the output.
- [ ] After finishing the slides that introduce the course, create more slides
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
- [ ] Ensure that the instructions in the slides from the previous step will
work correctly regardless of the operating system (Windows, MacOS, Linux).
- [ ] Ensure that the instructions for installing each of the aforementioned
tools clearly explain what the tool does, why it is important, and how it can
help a prosegrammer to create, maintain, and analyze documents.
- [ ] Ensure that the instructions for installing each of the aforementioned
tools stress the importance of testing the setup to make sure that they are
working. There should be links to online documentation that a learner can read
if they have trouble installing or testing any of the tools.
- [ ] Add content about the responsible use of artificial intelligence (AI)
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
