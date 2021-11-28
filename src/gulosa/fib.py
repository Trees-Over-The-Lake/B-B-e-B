# Código de Fibonacci usando abordagem gulosa.
# Muitos elementos dentro da árvore de recursão
# serão recalculados inúmeras vezes
import time

# Código do fibonacci
def fib(numero):    
    if (numero <= 2):
        return 1
    
    return fib(numero-1) + fib(numero-2)


def timer(fib, num):
    start = time.time()
    fib(num)
    end = time.time()
    return end - start

# Escrevendo os tempos na tela
print(f'Fibonnaci de 10: {timer(fib, 10)}')
print(f'Fibonnaci de 15: {timer(fib, 15)}')
print(f'Fibonnaci de 20: {timer(fib, 20)}')
print(f'Fibonnaci de 30: {timer(fib, 30)}')
