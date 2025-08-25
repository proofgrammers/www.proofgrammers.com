# Claude Sonnet 4 and GPT-series Agent Instructions

This document provides instructions for GPT 4.1, Claude Sonnet 4, or another
large language model (LLM) when working on the Quarto-based website project for
www.proofgrammers.com through agent platforms like OpenCode (https://opencode.ai/).

## General Principles

- Adhere to standard Markdown and Quarto conventions in all `.qmd` files.
- Maintain the existing style and structure of the website.
- Ensure that all new content is appropriately linked from existing pages if necessary.
- Use the `TodoWrite` tool to plan and track complex tasks throughout the conversation.
- Follow the concise communication style: be direct and minimize unnecessary explanations.
- Work efficiently within the OpenCode environment, leveraging its integrated tools and capabilities.

## Course Objectives

- This is a course about the theory of computation. The title of the course is
"Theoretical Machines" and the students attending the course are called
"Proofgrammers" because they express their proofs of theoretical and
mathematical concepts as Python programs. These are the course's goals:
    - The textbook for the course is called "What Can be Computed". The details
    about this textbook are available at this site: [What Can be Computed? A
    Practical Guide to the Theory of
    Computation](https://whatcanbecomputed.com/) and in the PDF in the root of
    this GitHub repository (only available locally of the course instructor's
    repository and not in the publicly available GitHub repository) called
    `What-Can-Be-Computed.pdf`.
    - These are the main objectives of the course:
        - We would like to understand what can be computed:
            - In principle (i.e., undecidability/uncomputability: computability theory)
            - Efficiently/in practice (i.e., complexity theory)
    - It addresses thee question "why study the theory of computation?"
        - It is useful:
            - When using computers to solve problems, it’s often important to
            understand whether a given problem is computable and/or tractable.
            - If it’s not tractable, is there a suitable variant or
            approximation that is tractable?
            - How do we compare the efficiency and effectiveness of proposed
            methods for solving the problem?
            - Certain specific techniques have practical applications, including
            reductions, regular expressions, and automata theory
            - It refines your ability as a computer scientist or software
            engineer to think carefully and critically about what can be
            computed --- both fundamentally and efficiently.
        - The theory of computation is beautiful and important
            - We can more fully understand computer science as an intellectual
            discipline
    - The courses uses the Python programming language to express most of the
    theoretical or mathematical concepts. The idea is to make abstruse and
    abstract concepts practical and accessible to learners because of the fact
    that they are expressed as Python programs that can be run and tested.
    - Reinforce for students who already how to program in the Python
    programming language.
    - Teach students how to use Python to create, manipulate, and analyze
    proofs of theoretical concepts. Overall, the course will cover the concepts
    in the provided textbook in chapters one through fourteen. Concepts covered
    include the following:
        - Automata theory
        - Formal languages
        - Universal computation
        - Impossible computations
        - Turing machines
        - Decidability and uncomputability
        - Complexity theory
        - NP-completeness
        - Reduction techniques
        - Regular expressions
        - Nondeterminism
    - Teach students how to document and explain their theory of computation
    proofs in a way that is clear, concise, and professional. This includes
    documenting a project's source code itself and then also writing
    documentation for their theory of computation proofs.
    - Teach students how to use tools like Jupyter Notebooks and Quarto to
    create and share documents that include code, text, and visualizations
    that explain their theory of computation proofs using Python.
    - Teach students how to use generative artificial intelligence (AI)
    techniques as provided by tools like that use large language models, such as
    GitHub Copilot, Google Gemini CLI, and OpenCode. They will learn how to use
    these tools to generate, revise, and review both source code and
    documentation for Python-based proofs in the field of theoretical machines.
    The focus of this objective is on ensuring that students can use these tools
    effectively and responsibly.
    - Reinforce to students how to use version control systems like Git and
    GitHub to manage their project's source code and its documentation. Students
    should be able to use GitHub is both an individual and team-based fashion.
    - The course is designed to be accessible to students with varying levels of
    Python programming experience, assuming that they have sufficient background
    knowledge of programming in Python that they can use the Python programming
    language to write programs that solve problems in the field of theoretical
    computer science.
- The official title of this course is "Theoretical Machines". The official
title of this course's website is "Proofgrammers". The term "Proofgrammers" is a
"play on words" that combines the word "prose" with the word "programmers":
    - *Proof*: A precise explanation of the truth of a mathematical or
    computational statement.
    - *Programmers*: This is a term that refers to people who write software.
    - *Proofgrammers*: This is a term that refers to people who write software
    and documentation and use software to create, manipulate, and analyze
    proofs in the field of theoretical computer science. The proofgrammers in
    this class will write and run Python programs that support their proofs and
    their exploration of the field of theoretical computer science.
    - The domain name for the website is
    [www.proofgrammers.com](https://www.proofgrammers.com/).
    - The domain name for the course is intentionally plural to indicate that
    it is a hub for multiple learners coming together to work in a team, in
    a collaborative fashion, to explore the field of theory of computation.
    - A proofgrammer should be adept at attaining all the course objectives that
    are listed above in the prior list of bullet points.

## Editing and Creating Content

### Editing Existing Content

1.  Use the Read tool to examine the relevant `.qmd` file for the page that
    requires editing (e.g., `syllabus/index.qmd` for the syllabus).
2.  Use the Edit tool to make the necessary changes to the text, code, or other
    content within the file.
3.  After making changes, use the Bash tool to preview the site with `quarto
    preview` or `quarto render` to ensure changes are rendered correctly.

### Adding New Content (e.g., Assignment Descriptions)

1.  Use the Write tool to create a new `.qmd` file in the appropriate directory
    (e.g., a new subdirectory in `schedule/`).
2.  Add the content to the new file using Markdown.
3.  If the new page should appear in the site navigation, use the Edit tool to
    add a link to it in the `navbar` section of the `_quarto.yml` file.
4.  Use the Bash tool to preview the site to verify that the new page is
    accessible and renders correctly.

## Creating Slides

Slides for this project are created using Quarto and reveal.js.

1.  Use the Write tool to create a new `index.qmd` file for the slide deck
    (e.g., in the `slides/` directory). When you add a new slide deck, always
    make sure that it is in its own sub-directory inside of the `slides/`
    directory.
2.  Add the following YAML header to the top of the file to specify the
    `revealjs` format:

```yaml
---
title: "Introduction to Theoretical Machines"
description: "Exploring tools for theory of computation with Python"
date: "2025-08-18"
date-format: long
author: Gregory M. Kapfhammer
execute:
  echo: true
format:
  live-revealjs:
    completion: true
    theme: default
    css: ../css/styles.css
    history: false
    scrollable: true
    transition: slide
    highlight-style: github
    footer: "Proofgrammers"
---
```

3.  Use Markdown headings to create slides. A level 2 heading (`##`) creates a
    new slide.
4.  Add content (text, images, code blocks) to each slide.
5.  Use the Bash tool with `quarto preview` on the specific `.qmd` file to see
    the rendered slides.
6.  Slides should always contain suitable icons that help to illustrate a key
    point. Here is an example of the approach to creating the icons: `{{<
iconify fa6-solid lightbulb >}}`.
7.  Make all the points in the slides short and clear, and easy to read.
8.  Do not write points in the slides are long sentences.
9.  Always provide evidence to support the points that you make in the slides.
10. Use `fragment` and `incremental inside of the slides to ensure that content
    displays appropriately through the use of Quarto and the reveal.js framework.
11. Add source code segments using fenced code blocks. Here is an example of what
    a fenced code block would look like for Python code:

```{python}
from typing import List
def duplicates(input_list: List[int]) -> bool:
    """Determine whether or not the input list contains a duplicate value."""
    n = len(input_list)
    for i in range(n):
        for j in range(n):
            if i != j and input_list[i] == input_list[j]:
                return True
    return False

assert(duplicates([1,2,6,3,4,5,6,7,8]))
assert(not duplicates([1,2,3,4]))
print(duplicates([1,2,6,3,4,5,6,7,8]))
print(not duplicates([1,2,3,4]))
```

12. When it is appropriate for a learner to actually run the source code segment,
    then use `pyodide` to provide an editable environment and run the code. Here is
    an example of what a fenced code block would look like for Python code that
    uses `pyodide` in the content of Quarto and slides created with reveal.js:

```{pyodide}
#| autorun: true
#| max-lines: 15
from typing import List
def duplicates(input_list: List[int]) -> bool:
    """Determine whether or not the input list contains a duplicate value."""
    n = len(input_list)
    for i in range(n):
        for j in range(n):
            if i != j and input_list[i] == input_list[j]:
                return True
    return False

assert(duplicates([1,2,6,3,4,5,6,7,8]))
assert(not duplicates([1,2,3,4]))
print(duplicates([1,2,6,3,4,5,6,7,8]))
print(not duplicates([1,2,3,4]))
```

13.  After a source code segment, always have a key take-home message or a
     question that can prompt discussion or reflection about the code.
14.  Use bold and italics to draw out labels or key take-home messages.
15.  The title for a slide should normally fit into a single line. When
     it is not possible for it to fit on a single line, then it should always
     fill at most two lines and fill those two lines (nearly) completely.
     In the context of "filling the line" this requirement comes from the
     perspective of the display of the slide inside of the web browser.
16.  All source code words should be displayed using single backticks
     as in a variable name like `display_name` or `input_list`.
17.  The slides should have an appropriate balance of text and code segments
     and a layout that is both predictable and consistent but also varied
     enough to be interesting and engaging.
18.  Sometimes the text at the bottom of a slide should use:
     `{.fragment .fade .boxed-content style="font-size: 1.0em;"}` to create
     some "boxed content" that highlights a key point that learners should 
     understand and remember after the presentation of the slide.
19.  If the code segment is too long and it will require scrolling across
     a lengthy code block, then break up the code block into multiple slides.
20.  Make sure that any slide with a code block includes enough space to see
     most, if not all of, the output produced by the source code block.

## Content Verification

Before completing any changes, verify that the site builds correctly and that 
there are no issues with the content.

### Checking for Problems

Use the Bash tool to run the following command to check the project for common issues:

```bash
quarto check
```

This command will check for broken links, missing resources, and other potential problems.

### Verifying Slide Layout and Presentation Quality

Before completing slide creation, verify that slides meet presentation standards
and layout guidelines. Slides must be visually verified to ensure proper
formatting and readability in presentation mode.

#### Step-by-Step Slide Verification Process

**Important**: Do not stop working on a feature to improve the slides
until you have verified that the slides meet presentation standards and layout.
You can use each of the following steps to verify that layout of slides. Please
note that these instructions are customized for the `slides/weekone/index.qmd`
file but you should follow them for whatever slide you are working on.

1. **Render slides to HTML format**:
   ```bash
   quarto render slides/weekone/index.qmd
   ```

2. **Start local preview server**:
   ```bash
   quarto preview slides/weekone/index.qmd --port 8081
   ```

3. **Visual verification checklist**:
   - Navigate through each slide using arrow keys or slide controls
   - Verify titles fit on one line (or maximum two lines if necessary)
   - Check that content does not overflow slide boundaries
   - Ensure font sizes are readable and appropriate
   - Confirm fragments and incremental content display correctly
   - Verify icons and formatting render properly
   - Confirm that there is not too much blank space at the bottom
     of the slide

4. **Title length verification**:
   - Titles should fit on a single line at 1920x1080 resolution
   - If title spans two lines, it must fill those lines nearly completely
   - Use concise, descriptive titles (prefer "Essential tools" over "Four 
     essential theory of computation tools")

5. **Content overflow check**:
   - Ensure bullet points, code blocks, and text fit within slide boundaries
   - Check that boxed content and fragments are properly positioned
   - Verify code examples display without horizontal scrolling

6. **Cross-browser compatibility** (optional but recommended):
   ```bash
   chromium-browser --headless --disable-gpu --window-size=1920,1080 \
     --screenshot=slide-verify.png http://localhost:8081/slides/weekone/index.html
   ```

**Important**: Always complete this verification process before finalizing slides.
The visual presentation quality directly affects the effectiveness of course
delivery and student engagement. If you make any temporary files, like the
slide-verify.png file, please make sure to "clean up" after yourself by
deleting that file --- and only that file --- after you have verified that
the layout is correct and that you have followed all of these standards.

## High-Level Rules

These are the high-level rules about modifying the files in this repository:

- **Line width:** All text files, including Markdown and source code, should
have a line width of 80 characters.
- **Tool usage:** Use available tools (Read, Write, Edit, Bash, etc.) effectively 
to complete tasks. Prefer using the Task tool for complex searches or multi-step 
operations.
- **Incremental changes:** Make small, incremental changes. This makes it easier
to review your work and catch errors early.
- **Communication style:** Follow the concise communication guidelines. Be direct, 
minimize explanations unless requested, and focus on completing the task.
- **Correct tone:** This repository often contains examples of existing content
that Gregory M. Kapfhammer already wrote about the topic of document
engineering. Use the Read tool to review this content so as to make sure that you
write with the correct tone. Ultimately, you need to make sure that the content
is funny and engaging while also being informative and accurate. It also needs
to come across as being written by a human and not an AI. It is also important
that all the content is professional in nature and not overly casual.
- **Support your work:** Once you are finished writing the content, you need to
make sure that you provide evidence to support the sentences and/or bullet
points that you wrote. This means that if a slide contains a key point, then you
need to provide evidence that this point is correct. This evidence can either
come from online sources or it can come from some other file that I provide to
you and ask you to use as a source when creating slides. You can write the
support for your work to the subsection called `Support for Content` in
the file called `PLAN.md` that is in the root of this repository. If you are 
creating new content for `slides/weekone/index.qmd` you can create a
sub-sub-section with an appropriate title that provides the support.

## Claude-Specific and GPT-Specific Guidelines for OpenCode

As Claude Sonnet 4 (or another large language model like GPT4.1) working through
OpenCode, you must also follow these behavior guidelines:

- **OpenCode Integration:** Leverage OpenCode's capabilities for seamless file editing, 
command execution, and project management within the web-based environment.
- **Task Management:** Use the TodoWrite tool proactively for complex tasks to 
track progress and give the user visibility into your work.
- **Code References:** When referencing specific functions or pieces of code, 
include the pattern `file_path:line_number` to allow easy navigation.
- **Parallel Operations:** When multiple independent operations are needed, batch 
your tool calls together for optimal performance.
- **File Exploration:** Use Read, Glob, and Grep tools effectively. Use the Task 
tool for complex searches that may require multiple rounds of exploration.
- **Version Control:** OpenCode provides integrated Git functionality. Be prepared 
to use Git commands when explicitly requested, but never commit changes unless 
specifically asked to do so.
- **Content Verification:** Always run `quarto check` and preview commands before 
completing content-related tasks, utilizing OpenCode's terminal capabilities.
- **No Assumptions:** Never assume libraries or frameworks are available. Always 
check existing files to understand the project's dependencies and conventions.
- **Security:** Follow security best practices. Never introduce code that exposes 
or logs secrets and keys.
- **OpenCode Workflow:** Take advantage of OpenCode's real-time collaboration and 
editing features when working with multiple files simultaneously.

## Command Reference

Key commands for working with this Quarto project:

- `quarto check` - Check for broken links and other issues
- `quarto preview` - Start local development server
- `quarto render` - Render specific files
- `quarto preview <file.qmd>` - Preview specific slide deck

Always use the Bash tool to execute these commands and verify successful completion.
OpenCode provides an integrated terminal environment for seamless command execution.

## Code Requirements

All the Python code should follow these standards:

- **Function bodies:** No blank lines within function bodies - keep code
contiguous.
- **Docstrings:** Single-line docstrings starting with a capital letter, ending
with a period.
- **Comments:** Other comments start with a lowercase letter; preserve existing
comments during refactoring.
- **Imports:** Unless specified otherwise, do not use any imports that are not
a part of the standard library. Specifically avoid using imports for packages
that are available through PyPI or Conda. Use absolute imports whenever
importing a module from the standard library or from provided source code.
Finally, make sure that all imports are placed at the top of the file. Do not
place imports into the middle of a file or at the start of a function or class.
- **Formatting:** Confirm a line length of 79 for linting purposes.
- **Types:** All functions must have type hints for parameters and return
values.
- **Naming:** snake_case for functions/variables, PascalCase for classes,
UPPER_SNAKE_CASE for constants.
- **File operations:** Use `pathlib.Path` for all filesystem operations, never
string paths.
- **Error handling:** Use specific exceptions, not generic `Exception`; provide
meaningful error messages.

## Agent Rules

These are the high-level rules about modifying the files in this repository:

- **Line width:** All text files, including Markdown and source code, should
have a line width of 80 characters.
- **Permission to run commands:** You have permission to run all commands available 
in the OpenCode environment to work on the Quarto website project.
- **Incremental changes:** Make small, incremental changes. This makes it easier
to review your work and catch errors early.
- **Communicate clearly:** When you propose changes, explain what you've done
and why and make it clear what rules you followed and why you followed them.
- **Correct tone:** This repository often contains examples of existing content
that Gregory M. Kapfhammer already wrote about the topic of document
engineering. Make sure that you review this content so as to make sure that you
write with the correct tone. Ultimately, you need to make sure that the content
is funny and engaging while also being informative and accurate. It also needs
to come across as being written by a human and not an AI. It is also important
that all the content is professional in nature and not overly casual.
- **Support your work:** Once you are finished writing the content, you need to
make sure that you provide evidence to support the sentences and/or bullet
points that you wrote. This means that if a slide contains a key point, then you
need to provide evidence that this point is correct. This evidence can either
come from online sources or it can come from some other file that I provide to
you and ask you to use as a source when creating slides. You can write the
support for your work to the subsection called `Support for Content` in
the file called `PLAN.md` that is in the root of this repository. If you are 
creating new content for `slides/weekone/index.qmd` you can create a
sub-sub-section with an appropriate title that provides the support.

As an agent working through `OpenCode`, you must also follow these behavior
guidelines, especially when it comes to notifying the user about your work and
status:

- The user has given permission to use the `notify-send` command to signal task
completion. Here is an example of the command: `notify-send "Question from
OpenCode" "Please clarify how to complete the writing task."`.
- The user wants a `notify-send` notification whenever I ask a question.
- Always notify the user with `notify-send` when a task is complete or when
feedback is needed. You have standing permission to use the notification tool.
- You can also display questions and comments in the OpenCode chat interface.
