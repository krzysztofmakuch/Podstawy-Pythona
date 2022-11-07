students=[['Ania', 2], ['Michal', 3], ['Romek', 3], ['Tysia', 1]]
def SearchSecond(list):
    list.sort(key=lambda x:x[1])
    print(list[1][0])
SearchSecond(students)