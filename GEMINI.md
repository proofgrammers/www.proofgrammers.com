# Gemini-Related Project Instructions

This document provides instructions for the Gemini AI assistant to follow when
working on this Quarto-based website project.

## General Principles

- Adhere to standard Markdown and Quarto conventions in all `.qmd` files.
- Maintain the existing style and structure of the website.
- Ensure that all new content is appropriately linked from existing pages if necessary.

## Course Objectives

- This is a course about Theoretical Machines. These are the course's goals:
    - Teach students how to program in the Python programming language.
    - Teach students how to use Python to create, manipulate, and analyze
    documents.
    - Teach students how to document their work in a way that is clear, concise,
    and professional. This includes documenting a project's source code itself
    and then also writing documentation for their software projects.
    - Teach students how to read and critique the documentation for popular
    open-source projects like Quarto or Ruff or Uv or other open-source tools
    that are primarily in the Python ecosystem.
    - Teach students how to use tools like Jupyter Notebooks and Quarto to
    create and share documents that include code, text, and visualizations.
    - Teach students how to use generative artificial intelligence (AI)
    techniques as provided by tools like that use large language models, such as
    GitHub Copilot, Google Gemini CLI, and OpenCode. They will learn how to use
    these tools to generate, revise, and review both source code and
    documentation. The focus of this objective is on ensuring that students can
    use these tools effectively and responsibly.
    - Teach students how to use version control systems like Git and GitHub to
    manage their project's source code and its documentation. Students should be
    able to use GitHub is both an individual and team-based fashion.
    - The course is designed to be accessible to students with varying levels of
    Python programming experience and knowledge of theoretical machines.

- The official title of this course is "Theoretical Machines". The official
title of this course's website is "Prosegrammers". The term "Prosegrammers" is a
"play on words" that combines the word "prose" with the word "programmers":
    - *Prose*: This is the written word, like an article or a blog post.
    - *Programmers*: This is a term that refers to people who write software.
    - *Prosegrammers*: This is a term that refers to people who write software
    and documentation and use software to create, manipulate, and analyze
    documents.
    - The domain name for the website is
    [www.prosegrammers.com](https://www.prosegrammers.com/).
    - The domain name for the course is intentionally plural to indicate that
    it is a hub for multiple learners coming together to work in a team, in
    a collaborative fashion, to explore the field of theoretical machines.
    - A prosegrammer should be adept at attaining all the course objectives that
    are listed above in the prior list of bullet points.

## Editing and Creating Content

### Editing Existing Content

1.  Locate the relevant `.qmd` file for the page that requires editing (e.g.,
    `syllabus/index.qmd` for the syllabus).
2.  Make the necessary changes to the text, code, or other content within the
    file.
3.  After making changes, preview the site to ensure the changes are rendered
    correctly.

### Adding New Content (e.g., Assignment Descriptions)

1.  Create a new `.qmd` file in the appropriate directory (e.g., a new
    subdirectory in `schedule/`).
2.  Add the content to the new file using Markdown.
3.  If the new page should appear in the site navigation, add a link to it in
    the `navbar` section of the `_quarto.yml` file.
4.  Preview the site to verify that the new page is accessible and renders
    correctly.

## Creating Slides

Slides for this project are created using Quarto and reveal.js.

1.  Create a new `index.qmd` file for the slide deck (e.g., in the `slides/`
    directory). When you add a new slide deck, always make sure that it is in
    its own sub-directory inside of the `slides/` directory.
2.  Add the following YAML header to the top of the file to specify the
    `revealjs` format:

```yaml
---
title: "Introduction to Theoretical Machines"
description: "Exploring tools for theoretical machines with Python"
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
    footer: "Prosegrammers"
---
```

3.  Use Markdown headings to create slides. A level 2 heading (`##`) creates a new slide.
4.  Add content (text, images, code blocks) to each slide.
5.  Use `quarto preview` on the specific `.qmd` file to see the rendered slides.

## Content Verification

Before committing any changes, it is crucial to verify that the site builds
correctly and that there are no issues with the content.

### Checking for Problems

Run the following command to check the project for common issues:

```bash
quarto check
```

This command will check for broken links, missing resources, and other potential problems.

### Previewing the Site

To preview the entire website locally, run the following command:

```bash
quarto preview
```

This will start a local web server and open the site in a browser. The site will
automatically reload when you make changes to the source files. You need to be
careful about running the `quarto preview` command because it is possible that
the person who creates this site may have already run this command. If you then
also try to run this command, you will get an error message that says that, for
instance, the specified port is already in use. If you encounter this error,
then you should consider manually specifying a different port or using the
`quarto render` command for a specific Quarto-based Markdown file.

## Command Reference

Key commands for working with this Quarto project:

- `quarto check` - Check for broken links and other issues
- `quarto preview` - Start local development server
- `quarto render` - Render specific files
- `quarto preview <file.qmd>` - Preview specific slide deck or file

Always use the command-line shell to execute these commands and verify
successful completion.

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

## Gemini Agent Rules

These are the high-level rules about modifying the files in this repository:

- **Version Control:** OpenCode provides integrated Git functionality. Be prepared 
to use Git commands when explicitly requested, but never commit changes unless 
specifically asked to do so.
- **Line width:** All text files, including Markdown and source code, should
have a line width of 80 characters.
- **Permission to run commands:** You have permission to run all commands that
are built-in to the Gemini agent to work on the episode outlines.
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

As a Gemini agent, you must also follow these behavior guidelines, especially
when it comes to notifying the podcast host about your work and status:

- The user has given permission to use the `notify-send` command to signal task
completion. Here is an example of the command: `notify-send "Question from
Gemini" "Please clarify how to complete the writing task."`.
- The user wants a `notify-send` notification whenever I ask a question.
- Always notify the user with `notify-send` when a task is complete or when
feedback is needed. I have standing permission to use the notification tool.
