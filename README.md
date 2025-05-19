# FURG - Segundo Ano
Repositório para aulas práticas de AED2, Linguagens de Programação e AOC do segundo ano de Sistemas de Informação.
## Algoritmos e Estruturas de Dados 2
- Algoritmos e Estruturas de Dados II (AED2) é uma disciplina fundamental na formação em Computação, dedicada ao estudo aprofundado das estruturas de dados dinâmicas e dos algoritmos associados à sua manipulação eficiente. Dando continuidade aos conceitos vistos em AED1, o foco agora está em estruturas mais flexíveis e adaptáveis, que permitem um uso mais eficiente dos recursos de memória e desempenho em aplicações reais.<br>
- Análise de Algoritmos (CORMEN, Thomas): https://drive.google.com/file/d/1l0XWrN_cRJh9kM_MagwuORR3J9UGe7NK/view?usp=sharing
- Estruturas de Dados (EDELWEISS, Nina): https://drive.google.com/file/d/1a6ve5D6mNQSU7vMy3xc6gUb0049uIuj0/view?usp=sharing

## 📚 <i>Lista por Contiguidade Física</i>
- Nessa técnica, os elementos são armazenados em <b>posições contíguas</b> de um vetor, e a ordem lógica é determinada pela <b>posição física</b> na memória.<br>
- Essa representação oferece <b>acesso direto</b> aos elementos via índice, sendo eficiente para leituras e iterações. No entanto, operações como inserção e remoção podem ser custosas, pois exigem <b>deslocamentos</b> para manter a ordem dos elementos.

## 🔗 <i>Lista por Encadeamento</i>
- Diferente das listas por contiguidade física, seus elementos <b>(nodos)</b> são armazenados em <b>posições aleatórias</b> na memória, sendo ligados entre si por <b>ponteiros</b>.<br>
- Cada nodo contém os <b>dados e um ponteiro para o próximo elemento</b>, permitindo maior flexibilidade na inserção e remoção, <b>sem a necessidade de deslocamento</b> de dados. Essa estrutura é ideal quando não se conhece previamente o tamanho da lista ou quando há muitas alterações dinâmicas.<br>
- Apesar da facilidade na manipulação, seu acesso é <b>sequencial</b>, e a estrutura exige cuidados com a alocação e liberação de memória, o que pode aumentar a complexidade dos algoritmos.

## 📦 <i>Pilha</i>
- Esta estrutura representa uma <b>pilha (stack)</b>, onde o acesso aos dados ocorre sempre por uma <b>única extremidade</b>, chamada de <b>topo</b>.
- Pilhas seguem a disciplina de acesso <b>LIFO (Last In, First Out)</b>, ou seja, o <b>último elemento inserido é o primeiro a ser removido</b>.
- As únicas operações permitidas são: <b>criar</b> a pilha vazia, <b>inserir (push)</b> um elemento no topo, <b>remover (pop)</b> o elemento do topo, <b>consultar</b> o valor atual do topo e <b>destruir</b> a pilha, liberando os recursos.
- A estrutura pode ser implementada de duas formas:
- Por <b>contiguidade física</b>, usando <b>vetores, com tamanho fixo e acesso direto</b>;
- Por <b>encadeamento</b>, usando <b>ponteiros, com alocação dinâmica e maior flexibilidade</b>.
