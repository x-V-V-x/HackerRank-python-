""" Detect HTML Tags, Attributes and Attribute Values
Task
You are given an HTML code snippet of N lines.
Your task is to detect and print all the HTML tags, attributes and attribute values. """

# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]
html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()