# 6-3 Python Terms

python_terms = {
    'print()': 'Print something to console.',
    'str()': 'Convert value to string format.',
    'title()': 'Convert string to Title format',
    'for': 'A for loop'
}


for term in python_terms.keys():
    print(term)
    print(python_terms.get(term) + "\n")

print()

for term, desc in python_terms.items():
    print(term + ": " + desc + "\n")
