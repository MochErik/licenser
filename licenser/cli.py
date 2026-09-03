import argparse, datetime, sys

MIT_TEMPLATE = '''MIT License

Copyright (c) {year} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

def generate_license(license_type="mit", author="Moch. Erik Irriansyah", year=None):
    year = year or datetime.datetime.now().year
    return MIT_TEMPLATE.format(year=year, author=author)

def main(args=None):
    parser = argparse.ArgumentParser(prog="licenser", description="📜 Licenser - Open-Source License Generator CLI")
    parser.add_argument("-t", "--type", default="mit", help="License type (mit, apache, bsd)")
    parser.add_argument("-a", "--author", default="Moch. Erik Irriansyah", help="Author name")
    parser.add_argument("-o", "--output", default="LICENSE", help="Output file")
    parsed = parser.parse_args(args)
    text = generate_license(parsed.type, parsed.author)
    with open(parsed.output, "w") as f:
        f.write(text)
    print(f"✅ Generated {parsed.type.upper()} license in '{parsed.output}'")
if __name__ == "__main__": main()
