# Python´s Assignment Expressions ':='

'''
Source: Youtube - MathByte Academy

https://www.youtube.com/watch?v=vPT_3iXyISc

PEP 572 - https://peps.python.org/pep-0572/

'''

# => Diferença entre Expression, Assignment Statement e Assignment Expression

# Expression
10 + (20 * 30) // 3
print(10 + (20 * 30) // 3)

# Assignment Statement
a = 10 + (20 * 30) // 3
print(a)

# Elas são representadas pelo operador de atribuição (:=).
# São utilizadas para atribuir e retornar um valor em uma única expressão. 
# Isso é útil em situações onde você precisa atribuir um valor a uma variável como parte de uma expressão mais complexa.

(x := 10 + (20 * 30) // 3)
print(x)


# Um exemplo de uso, em uma fórmula complexa(nesse caso é bem simples...)

a = (2 * 3) % 5
print(a)

a = (b := 2 * 3) % 5
print(a)
print(b)

# Você pode ter acesso ao resultado de parte da operação para confirmar se está correto,
# como um debug tosco
# Ou para extrair subcalculos para processos futuros

# Porém a meneira correta de fazer seria em linhas separadas
b = 2 * 3
a = b % 5


# => Onde seria útil utilar Assignmet Expressions

# Extrair cada caracter do elemento que for maior que 1
l = ["a", "aa", "aaa", "ab", "aab", "aabb"]
result = [set(element) for element in l if len(set(element)) > 1]
print(result)

# com Assignment Expression
result = [chars for element in l if len(chars := set(element)) > 1]
print(result)


# => Veja como pode diminiur o tempo de processamento
import time

def transform(x):
    time.sleep(0.2)
    sign = 1 if x % 2 == 0 else - 1
    return sign * x ** 2

l = list(range(1, 11))
print(l)

start = time.perf_counter()
result = [transform(x) for x in l if transform(x) > 0]
end = time.perf_counter()
print(result)
print(f"elapsed: {end - start:.1f} seconds") #elapsed: 3.0 seconds

# Com Assignment Expression
start = time.perf_counter()
result = [val for x in l if (val := transform(x)) > 0]
end = time.perf_counter()
print(result)
print(f"elapsed: {end - start:.1f} seconds") #elapsed: 2.0 seconds

# => Criando uma lista somando o primiro valor ao próximo valor
lista = [
    10,
    10 + 10,
    10 + 10 + 10
]
print(lista)

lista2 = [
    (start := 10),
    (intermediate := start + 10),
    start + intermediate
]
print(lista2)

dicionario = {
    "start": (start := 10),
    "intermediate": (intermediate := start + 10),
    "last": start + intermediate
}
print(dicionario)

