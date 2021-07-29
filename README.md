# Markdown2HTML
A bare-bones command line Markdown to HTML converter that can handle:
- headings
- ordered and unordered lists
- paragraphs
- bold and italics
- custom functionality:
  - converts content inside `[[` and `]]` to an MD5 hash
  - removes all `c`s (case insensitive) from content inside `((` and `))`

## Usage
`./markdown2html.py markdown_file.md html_file.html`
