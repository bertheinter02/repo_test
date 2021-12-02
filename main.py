a = [3, 8, 2, 4, 7]

def get_missing_numbers(l, min, max):
     missing = []
     for i in range(min, max+1):
          if i not in l:
               missing.append(i)
     return missing

print(get_missing_numbers(a, 1, 10))

