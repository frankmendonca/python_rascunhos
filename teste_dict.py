def eval_and_print(text):
    print(text, '->', eval(text))

dict = {}

eval_and_print("dict")
eval_and_print("dict.get('A')")
eval_and_print("dict")
eval_and_print("dict.get('A', [])")
eval_and_print("dict")
eval_and_print("dict.setdefault('A', [])")
eval_and_print("dict")
eval_and_print("dict.setdefault('A', 'A')")
eval_and_print("dict")
