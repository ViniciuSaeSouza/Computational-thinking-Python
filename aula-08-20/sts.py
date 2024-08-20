"""1. Tornar os elementos de uma lista distintos.
a = [1, 3, 3, 5, 7, 9, 9]
.....
b = [1, 3, 5, 7, 9]
 
 
2. Dadas duas listas preenchidas, criar uma terceira com os valores das duas anteriores
sem repetir o mesmo valor.
 
a = [1, 3, 3, 5, 7, 9, 9]
b = [2, 4, 5, 6, 8]
..........
c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 """
 
a = [1, 3, 3, 5, 7, 9, 9]
# b = [1, 3, 5, 7, 9]
def lista_items_distintos(a: list) -> list:
  b = []
  for number in a:
    if number not in b:
      b.append(number)
  b.sort()
  # print (c)
  return b
  
print(lista_items_distintos(a))
        
# """
# 2. Dadas duas listas preenchidas, criar uma terceira com os valores das duas anteriores
# sem repetir o mesmo valor.
 
# a = [1, 3, 3, 5, 7, 9, 9]
# b = [2, 4, 5, 6, 8]
# ..........
# c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# """

# a = [1, 3, 3, 5, 7, 9, 9]
# b = [2, 4, 5, 6, 8]
# # [1,2,3,4,5,6,7,8,9]

# def lista_items_distintos(a: list, b: list) -> list:
#   c = []
#   for n_a in a:
#     if n_a not in c:
#       c.append(n_a)
#   for n_b in b:
#     if n_b not in c:
#       c.append(n_b)
#   c.sort()
#   print (c)
#   # return c
  
# lista_items_distintos(a, b)