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
    html_text = ""
    for line in lines:
        if '#' in line:
            num_hash = line.count('#')
            html_text = html_text + "<h" + str(num_hash) + ">" + \
                line[num_hash + 1:] + "</h" + str(num_hash) + ">\n"

    generate_file(html_text, html_filename)


def generate_file(html_text, html_filename):
    """generating and populating html output file"""

    with open(html_filename, mode='w', encoding='utf-8') as f:
        f.write(html_text)

if __name__ == "__main__":
    get_files()
