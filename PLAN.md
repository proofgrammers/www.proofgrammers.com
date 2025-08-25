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

#### Cross-Platform Tool Installation

- Installation instructions for UV, Python, and Quarto are designed to work
across Windows, macOS, and Linux systems, following each tool's official
documentation and installation guides
- Command-line verification methods (`--version` flags) provide standard
approaches for confirming successful installations across operating systems
- Documentation links provided (UV docs, Quarto docs, VS Code docs) offer
official troubleshooting resources maintained by tool creators

#### AI Tool Responsibility

- Responsible use of AI coding assistants is emphasized in academic literature
on AI ethics and educational guidelines from institutions implementing AI tools
in curricula
- The principle that users remain responsible for AI-generated content aligns
with emerging best practices in AI-assisted writing and coding, as outlined by
organizations like the ACM and IEEE
