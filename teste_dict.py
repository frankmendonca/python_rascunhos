def print_eval(text):
    print(text, '->', eval(text))

dict = {}

print_eval("dict")
print_eval("dict.get('A')")
print_eval("dict")
print_eval("dict.get('A', [])")
print_eval("dict")
print_eval("dict.setdefault('A', [])")
print_eval("dict")
print_eval("dict.setdefault('A', 'A')")
print_eval("dict")
