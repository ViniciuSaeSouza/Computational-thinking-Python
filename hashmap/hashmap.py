
# --------------------- Hash map sem usar a biblioteca Default Dict

"""city_map = {} # Permite criar um hash map, mas precisa que a 'chave(key)' seja inicializada

cities = ['Calgary', 'Vancouver', 'Toronto']

city_map['Canada'] = [] # Inicialização da 'chave(key)' por conta da inicialização do hash map sem o Default Dict

city_map['Canada'] += cities"""

# --------------------- Hash map importando a biblioteca Default Dict
"""from collections import defaultdict



city_map = defaultdict(list)

cities_canada = ['Calgary', 'Vancouver', 'Toronto']
cities_usa = ['New York', 'Los Angeles', 'Chicago']
cities_sao_paulo = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais']

city_map['Canada'] += cities_canada
city_map['USA'] += cities_usa
city_map['São Paulo'] += cities_sao_paulo

print(f'Chaves(keys): {city_map.keys()}') # .keys() devolve as chaves dentro do dicionário
print(f'Valores(values): {city_map.values()}') # .values() devolve os valores dentro do dicionário
print(f"Itens: {city_map.items()}") # devolve todos os itens contidos no dicionário
"""

# --------------------- Exercicio leetcode 49 - Anagrama
"""from collections import defaultdict

def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}

        for i,num in enumerate(nums):
            diff = target - num
            if diff in nums_map:
                print(nums_map.items())
                return [nums_map[diff],i]
            nums_map[num] = i
        print(nums_map.items())
        return nums_map
        

twoSum(self = any, nums=[2,7,11,15], target = 9)"""


# --------------------- Exercicio 1 - Two sum

from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}

        for i,num in enumerate(nums):
            diff = target - num
            if diff in nums_map:
                return [nums_map[diff],i]
            nums_map[num] = i
        return nums_map