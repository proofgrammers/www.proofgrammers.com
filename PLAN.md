# Plan for Proofgrammers

## Implement New Slides for Chapter Eight, "Nondeterminism"

- You have access to the content of the book in the file:
`What-Can-Be-Computed.pdf` and `What-Can-Be-Computed.md` that is in the root of
this repository.
- You have access to the slides of the book in PPTX (which is hard for you to
read) and a QMD file (which is easier for you to read) in the
`theoreticalmachines/wcbc-slides/` directory.
- You have access to the images that were created from the slides for this
chapter. These images may be especially important because of the fact that
there are some diagrams of the output of a universal computer. You can include
these images into the slides you make by finding them in the `img/` directory
that is in the `theoreticalmachines/wcbc-slides/`
- You have access to the source code connected to this book in the directory
`theoreticalmachines/wcbc-code/`
- I have created a template file for the slides in the
`slides/weekeight/index.qmd`. You can add to this file! Please note that I have
already created the correct title and added the review slides from the last
week that I want you to keep in this slide deck.
- I would like you to create a starting version of the slides for Chapter
Seven: in the `slides/weekeight/index.qmd` file. Please note that you are
creating slides for _week nine_ of the course in the `index.qmd` file that is
in that directory but for _chapter eight_ of the book.
- One challenge of this chapter is that it contains a lot of source code
examples that may not run correctly unless you include all needed source code
from the book's archive. Do not include a source code example unless it is
self-contained and it will run directly without an extra dependencies.
- Make sure to only explain concepts that are connected to Chapter Seven.
- Make sure to review all the prior slides that I have created in the `slides/`
directory and the subdirectories for prior weeks in `weekone/` and `weektwo/`
and `weekthree/` and `weekfour/` and `weeksix/` and `weekseven` and
`weekeight/` to ensure that your slides are formatted and laid out just like
the content that I have already created.
- Do not use slide layouts that you do not already see in these example
slide decks.
- Unless there is a clear motivation to do so, do you not use features of
Quarto that you do not already see in these example slide decks.
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

### Week Nine: Understanding Nondeterminism (Chapter Eight)

**Content created**: 20 slides covering Chapter 8 "Nondeterminism" from
the textbook "What Can Be Computed?"

**Source materials used**:

1. **Textbook Chapter 8** (`What-Can-Be-Computed.md`): Sections on
nondeterministic computation, computation trees, nondeterministic Turing
machines, and equivalence proofs
2. **Author's slides** (`theoreticalmachines/wcbc-slides/08-nondeterminism.qmd`):
Complete lecture slide deck by textbook author
3. **Images** (12 PNG files): All diagrams from
`theoreticalmachines/wcbc-slides/img/08-nondeterminism_*.png` copied to
`slides/weeknine/`

**Key concepts covered with evidence**:

- **Nondeterministic computation** (Slides 1-2): Based on textbook
Section 8.1 "Nondeterministic Programs" explaining how multiple threads
explore different computational paths simultaneously
- **FindNANA genetic search example** (Slides 2-3): From textbook
Section 8.1 and author's slide images showing practical application of
nondeterminism using threading module
- **Modern concurrency** (Slides 4-5): Author's slides explicitly
discuss process management, thread switching, and unpredictable timing
as source of nondeterministic behavior
- **Python threading module** (Slides 6-7): Images 08-nondeterminism_2
and _3 show actual code from textbook using threading.Thread and
Thread.start()
- **Computation trees** (Slides 8-10): Textbook Section 8.2 "Computation
Trees" introduces formal model for nondeterministic computation; images
show tree structures with branches representing choices
- **Equivalence theorem** (Slide 11): Textbook Theorem 8.1 states any
problem computable by nondeterministic program is computable by
deterministic program; proof uses breadth-first exploration
- **Nondeterministic Turing machines** (Slides 12-15): Textbook Section
8.3 "Nondeterministic Turing Machines" defines formal model where
machines clone themselves; images show state diagrams with multiple
transitions
- **Three equivalent views** (Slide 16): Textbook Section 8.2.1
discusses simultaneous threads, random choice, and external choice as
equivalent formulations
- **Motivation for study** (Slide 17): Textbook Section 8.4 "Why Study
Nondeterminism?" explains natural thinking, cluster computing, and
foundation for NP-completeness

**Design decisions**:

- Followed established slide format from `slides/weekeight/index.qmd`
and `slides/weekfour/index.qmd`
- Used `{.incremental}`, `{.fragment}`, and `{.boxed-content}` patterns
consistently
- Avoided code examples due to external dependencies (per PLAN.md
instructions)
- Used 80-character line width throughout
- Applied appropriate iconify icons for each concept
- Images sized with `{.sensible-size-thick-border}` class for
consistency

**Content corrections**:

- **GthenOneT table correction** (Slide 15): Fixed error in summary table
where `xCTTGAGTGTATx` was incorrectly marked as "No" (rejected). Per
textbook definition, this string should be "Yes" (accepted) because the
second G at position 6 has exactly one T between it and the left end of
the string. Changed table entry to reflect correct acceptance status
with proper reasoning: "Second G has exactly one T between it and left
end".
