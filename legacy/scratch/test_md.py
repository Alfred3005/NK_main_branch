import markdown

text = """
| Col1 | Col2 |
|:---|:---|
| A | <details><summary>B</summary>C</details> |
"""

print("DEFAULT:")
print(markdown.markdown(text, extensions=['tables']))

print("WITH MD_IN_HTML:")
print(markdown.markdown(text, extensions=['tables', 'md_in_html']))
