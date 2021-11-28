#include <bits/stdc++.h>
using namespace std;

// Estrutura para o item que armazena o peso e correspondente

// Valor do item
struct Item
{
  float peso;
  int valor;
};

// Estrutura do nó para armazenar informações de decisão

// Arvore
struct Node
{
  // Nível do nó na árvore de decisão
  // Lucro dos nós no caminho da raiz para este nó (incluindo este nó)
  // Limite superior do lucro máximo na subárvore
  int nivel, lucro, limite;
  float peso;
};

bool cmp(Item a, Item b)
{
  double r1 = (double)a.valor / a.peso;
  double r2 = (double)b.valor / b.peso;
  return r1 > r2;
}

// Retorna o limite do lucro na subárvore enraizada em u.
// Esta função usa principalmente a solução Greedy para encontrar um limite superior no lucro máximo.

int limite(Node u, int n, int W, Item arr[])
{
  // se o peso superar a capacidade da mochila, devolva 0 como limite esperado
  if (u.peso >= W)
    return 0;

  // inicializar vinculado ao lucro pelo lucro atual
  int limite_lucro = u.lucro;

  // comece a incluir itens do índice 1 mais para o atual
  int j = u.nivel + 1;
  int pesoTot = u.peso;

  // verificar a condição do índice e a capacidade da mochila
  while ((j < n) && (pesoTot + arr[j].peso <= W))
  {
    pesoTot += arr[j].peso;
    limite_lucro += arr[j].valor;
    j++;
  }

  //Se k não for n, inclua o último item parcialmente para o limite superior do lucro
  if (j < n)
    limite_lucro += (W - pesoTot) * arr[j].valor /
                    arr[j].peso;

  return limite_lucro;
}

// Retorna o lucro máximo que podemos obter com a capacidade W
int knapsack(int W, Item arr[], int n)
{
  // classificando item com base no valor por unidade
  sort(arr, arr + n, cmp);

  // faça uma fila para atravessar o nó
  queue<Node> Q;
  Node u, v;

  u.nivel = -1;
  u.lucro = u.peso = 0;
  Q.push(u);

  //Extraia um por um item da árvore de decisão
  // calcula o lucro de todos os filhos do item extraído e continue salvando maxProfit
  int maxProfit = 0;
  while (!Q.empty())
  {
    // Desenfileirar um nó
    u = Q.front();
    Q.pop();

    // Se for um nó inicial, atribua o nível 0
    if (u.nivel == -1)
      v.nivel = 0;

    // Se não houver nada no próximo nível
    if (u.nivel == n - 1)
      continue;

    // Caso contrário, se não o último nó, então incremente o nível, calcular o lucro dos nós filhos.
    v.nivel = u.nivel + 1;

    // Tomando o item do nível atual adicionar atual peso e valor do nível para o nó u peso e valor
    v.peso = u.peso + arr[v.nivel].peso;
    v.lucro = u.lucro + arr[v.nivel].valor;

    // Se o peso acumulado for menor que W e o lucro é maior do que o lucro anterior, atualizar maxprofit
    if (v.peso <= W && v.lucro > maxProfit)
      maxProfit = v.lucro;

    // Obtenha o limite superior do lucro para decidir se deve adicionar v a Q ou não.
    v.limite = limite(v, n, W, arr);

    // Se o valor vinculado for maior do que o lucro, então apenas empurre na fila para mais consideração
    if (v.limite > maxProfit)
      Q.push(v);

    //Faça a mesma coisa, mas sem tirar o item na mochila
    v.peso = u.peso;
    v.lucro = u.lucro;
    v.limite = limite(v, n, W, arr);
    if (v.limite > maxProfit)
      Q.push(v);
  }

  return maxProfit;
}

// Programa para testar a função acima
int main()
{
  // Peso da mochila
  int W = 10;
  Item arr[] = {{2, 40}, {3.14, 50}, {1.98, 100}, {5, 95}, {3, 30}};
  int n = sizeof(arr) / sizeof(arr[0]);

  cout << "Lucro máximo possível = "
       << knapsack(W, arr, n);

  return 0;
}