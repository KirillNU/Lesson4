def mult_list(*args):
    mult = 1
    for x in args:
         mult *=x
    return mult

print(mult_list(1, 2, 3, 4, mult_list(2)))

p = mult_list

print (id(p), id(mult_list()))