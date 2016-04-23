def linear_merge(list1, list2):
    l = []
    itr1 = iter(list1)
    itr2 = iter(list2)

    next_ = lambda it: next(it) if it.__length_hint__() > 0 else None

    l1 = next_(itr1)
    l2 = next_(itr2)

    while l1 and l2:
        if l1 < l2:
            l.append(l1)
            l1 = next_(itr1)
        else:
            l.append(l2)
            l2 = next_(itr2)

    while l1:
        l.append(l1)
        l1 = next_(itr1)

    while l2:
        l.append(l2)
        l2 = next_(itr2)

    return l

list1 = ['aa', 'zz']
list2 = ['bb', 'xx']

assert linear_merge(list1, list2) == ['aa', 'bb', 'xx', 'zz']
