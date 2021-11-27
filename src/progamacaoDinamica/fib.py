# Código baseado na implementação da free code camp
# Referência: https://youtu.be/oBt53YbR9Kk?t=210
import time

# Código do fibonacci
def fib(numero):
    if (numero <= 2):
        return 1
    
    return fib(numero-1) + fib(numero-2)

# Versão do código usando programação dinâmica com memoization
def fibMemo(numero, memo={}):     
    if (numero in memo):
        return memo[numero]
    
    if (numero <= 2):
        return 1
    
    memo[numero] = fibMemo(numero - 1, memo) + fibMemo(numero - 2, memo)
    return memo[numero]

def timer(fib, num):
    start = time.time()
    fib(num)
    end = time.time()
    return end - start

# Escrevendo os tempos na tela
print(f'Fibonnaci de 10: {timer(fib, 10)}')
print(f'Fibonnaci de 10 memoization: {timer(fibMemo, 10)}')

print(f'Fibonnaci de 15: {timer(fib, 15)}')
print(f'Fibonnaci de 15 memoization: {timer(fibMemo, 15)}')

print(f'Fibonnaci de 20: {timer(fib, 20)}')
print(f'Fibonnaci de 20 memoization: {timer(fibMemo, 20)}')

print(f'Fibonnaci de 30: {timer(fib, 30)}')
print(f'Fibonnaci de 500 memoization: {timer(fibMemo, 500)}')