#!/usr/bin/python3
""" Markdown to HTML converter """
import sys


def get_files():
    """getting the files from the names input on command line"""

    if len(sys.argv) <= 2:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    md_filename = sys.argv[1]
    try:
        with open(md_filename, encoding='utf-8') as f:
            md_text = f.read()
            parse_text(md_text, sys.argv[2])
    except FileNotFoundError:
            print("Missing " + md_filename, file=sys.stderr)
            exit(1)
    exit()


def parse_text(md_text, html_filename):
    """parsing markdown and converting to html"""

    lines = md_text.split('\n')
    lines = inline_parse(lines)
    print(lines)
    html_text = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('#'):
            num_hash = line.count('#')
            html_text = html_text + "<h" + str(num_hash) + ">" + \
                line[num_hash + 1:] + "</h" + str(num_hash) + ">\n"
            i += 1

        elif line.startswith('-'):
            ul_text = "<ul>\n"
            while i < len(lines) and lines[i].startswith('-'):
                ul_text = ul_text + "\t<li>" + lines[i][2:] + "</li>\n"
                i += 1
            ul_text = ul_text + "</ul>\n"
            html_text = html_text + ul_text

        elif line.startswith('*'):
            ol_text = "<ol>\n"
            while i < len(lines) and line.startswith('*'):
                ol_text = ol_text + "\t<li>" + lines[i][2:] + "<\li>\n"
                i += 1
            ol_text = ol_text + "</ol>\n"
            html_text = html_text + ol_text

        elif len(line) == 0 and i < len(lines) - 1:
            while i < len(lines) and len(lines[i]) == 0:
                i += 1
            if not is_p(lines[i]):
                continue
            p_text = "<p>\n\t" + lines[i] + "\n"
            i += 1
            while i < len(lines) and len(lines[i]) > 0:
                p_text = p_text + "\t\t<br />\n\t" + lines[i] + "\n"
                i += 1
            p_text = p_text + "</p>\n"
            html_text = html_text + p_text

        else:
            i += 1

    generate_file(html_text, html_filename)


def is_p(ln):
    """checking if paragraph and not other markdown style"""
    return not ln.startswith('#') and not ln.startswith('-') and not \
        ln.startswith('*')


def inline_parse(lines):
    """parsing inline markdown syntax"""
    parsed_lines = []
    for line in lines:
        if len(line) == 0:
            parsed_lines.append(line)
            continue

        closing = False
        while '**' in line:
            line = line.replace('**', '</b>' if closing else '<b>', 1)
            closing = not closing

        closing = False
        while '__' in line:
            line = line.replace('__', '</em>' if closing else '<em>', 1)
            closing = not closing

        parsed_lines.append(line)

    return parsed_lines


def generate_file(html_text, html_filename):
    """generating and populating html output file"""

    with open(html_filename, mode='w', encoding='utf-8') as f:
        f.write(html_text)


if __name__ == "__main__":
    get_files()
