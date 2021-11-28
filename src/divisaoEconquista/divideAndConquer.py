
# Função para encontrar o no máximo em um array.
def DAC_Max(a, index, l):
    max = -1;
 
    if (index >= l - 2):
        if (a[index] > a[index + 1]):
            return a[index];
        else:
            return a[index + 1];
 
    # Lógica para encontrar o elemento máximo no array
    max = DAC_Max(a, index + 1, l);
 
    if (a[index] > max):
        return a[index];
    else:
        return max;
 
# Função para encontrar o no minimo em um array.
def DAC_Min(a, index, l):
    min = 0;
    if (index >= l - 2):
        if (a[index] < a[index + 1]):
            return a[index];
        else:
            return a[index + 1];
 
    # Lógica para encontrar o elemento minimo no array
    min = DAC_Min(a, index + 1, l);
 
    if (a[index] < min):
        return a[index];
    else:
        return min;
 
# Codigo teste
if __name__ == '__main__':
   
    # Definindo as variáveis
    min, max = 0, -1;
 
    # Inicializando o array
    a = [70, 250, 50, 80, 140, 12, 14];
 
    # Recursão - função DAC_Max chamada
    max = DAC_Max(a, 0, 7);
 
    # Recursão - função DAC_Max chamada
    min = DAC_Min(a, 0, 7);
    print("O número mínimo em um determinado array é : ", min);
    print("O número maximo em um determinado array é : ", max);
 
