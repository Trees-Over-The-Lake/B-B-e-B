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

print(fib(35))
print(fibMemo(35))