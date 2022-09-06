# -*- coding: UTF-8 -*-

d1 = {
    'a': 1,
    'b': 2,
}

d2 = {
    'a': None,
    'b': [],
    'c': 0,
}

d1_vals = d1.values()    # dict_values([1, 2])
d2_vals = d2.values()    # dict_values([1, None])

# all(iterable)都为真才为真
if all(d1_vals):
    print(d1)

# any(iterable)都为假才为假
if any(d2_vals):
    print(d2)

