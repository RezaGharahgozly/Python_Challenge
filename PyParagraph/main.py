file=("PyParagraph.txt")
with open (file, 'r') as text:
    lines = text.read()
    print(lines)
#add "1", because of first word
word=lines.count(" ")+ lines.count("-") + 1
#print(word)

senten=lines.count(". ") + lines.count("! ") + lines.count("? ") + lines.count(".”")
#print(senten)
char=len(lines)-lines.count(" ")
#char
print("""Paragraph Analysis
-----------------
Approximate Word Count: {}
Approximate Sentence Count: {}
Average Letter Count: {}
Average Sentence Length: {}
""".format(word, senten, char/word, word/senten ))