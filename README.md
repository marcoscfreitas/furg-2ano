# FURG - Segundo Ano
Repositório para aulas práticas de AED2, Linguagens de Programação e AOC do segundo ano de Sistemas de Informação.
## Algoritmos e Estruturas de Dados 2
- Algoritmos e Estruturas de Dados II (AED2) é uma disciplina fundamental na formação em Computação, dedicada ao estudo aprofundado das estruturas de dados dinâmicas e dos algoritmos associados à sua manipulação eficiente. Dando continuidade aos conceitos vistos em AED1, o foco agora está em estruturas mais flexíveis e adaptáveis, que permitem um uso mais eficiente dos recursos de memória e desempenho em aplicações reais.<br>
- <b><i>Análise de Algoritmos (CORMEN, Thomas)</b></i>: https://drive.google.com/file/d/1l0XWrN_cRJh9kM_MagwuORR3J9UGe7NK/view?usp=sharing
- <b><i>Estruturas de Dados (EDELWEISS, Nina)</b></i>: https://drive.google.com/file/d/1a6ve5D6mNQSU7vMy3xc6gUb0049uIuj0/view?usp=sharing

## 📚 <i>Lista por Contiguidade Física</i>
- Nessa técnica, os elementos são armazenados em <b>posições contíguas</b> de um vetor, e a ordem lógica é determinada pela <b>posição física</b> na memória.<br>
- Essa representação oferece <b>acesso direto</b> aos elementos via índice, sendo eficiente para leituras e iterações. No entanto, operações como inserção e remoção podem ser custosas, pois exigem <b>deslocamentos</b> para manter a ordem dos elementos.
- Ideal quando se <b>conhece previamente o tamanho máximo da lista</b>, quando é necessário <b>acesso rápido aos elementos</b> por índice e quando <b>operações de leitura/consulta são mais frequentes que inserções/remoções</b>.

## 🔗 <i>Lista por Encadeamento</i>
- Diferente das listas por contiguidade física, seus elementos <b>(nodos)</b> são armazenados em <b>posições aleatórias</b> na memória, sendo ligados entre si por <b>ponteiros</b>.<br>
- Cada nodo contém os <b>dados e um ponteiro para o próximo elemento</b>, permitindo maior flexibilidade na inserção e remoção, <b>sem a necessidade de deslocamento</b> de dados. Essa estrutura é ideal quando não se conhece previamente o tamanho da lista ou quando há muitas alterações dinâmicas.<br>
- Apesar da facilidade na manipulação, seu acesso é <b>sequencial</b>, e a estrutura exige cuidados com a alocação e liberação de memória, o que pode aumentar a complexidade dos algoritmos.
- Ideal quando o número de <b>elementos muda com frequência</b>, quando <b>inserções e remoções são mais frequentes</b> e ocorrem em qualquer posição da lista e quando <b>não se conhece o tamanho final</b> da lista.

## 📦 <i>Pilha</i>
- Esta estrutura representa uma <b>pilha (stack)</b>, onde o acesso aos dados ocorre sempre por uma <b>única extremidade</b>, chamada de <b>topo</b>.
- Pilhas seguem a disciplina de acesso <b>LIFO (Last In, First Out)</b>, ou seja, o <b>último elemento inserido é o primeiro a ser removido</b>.
- As únicas operações permitidas são: <b>criar</b> a pilha vazia, <b>inserir (push)</b> um elemento no topo, <b>remover (pop)</b> o elemento do topo, <b>consultar</b> o valor atual do topo e <b>destruir</b> a pilha, liberando os recursos.
- A estrutura pode ser implementada de duas formas:
- Por <b>contiguidade física</b>, usando <b>vetores, com tamanho fixo e acesso direto</b>.
- Por <b>encadeamento</b>, usando <b>ponteiros, com alocação dinâmica e maior flexibilidade</b>.
- Ideal quando o controle de chamadas, estados ou escopos deve ser feito de <b>forma reversa, por conta do LIFO</b>, permitindo operações somente ao topo da pilha.

## 📥 <i>Fila</i>
- A fila é uma estrutura de dados linear onde o acesso aos elementos ocorre em ordem de chegada, seguindo a disciplina <b>FIFO (First In, First Out)</b> — ou seja, o primeiro elemento inserido é o primeiro a ser removido.
- As operações principais são: <b>criar</b> a fila vazia, <b>inserir</b> o elemento no final, <b>remover</b> o elemento no início, <b>consultar</b> o elemento da frente, <b>verificar</b> se a fila está fazia e <b>destruir</b> a fila, liberando os recursos.
- A estrutura pode ser implementada de duas formas:
- Por <b>contiguidade física</b>, usando vetores para armazenar elementos em posições contíguas na memória, permite acesso rápido por índice, pode usar técnica <b>circular</b> para reaproveitar espaço, inserções e remoções exigem controle dos índices de ínicio e fim.
- Por <b>encadeamento</b> usando nodos ligados por <b>ponteiros</b>, cada um contendo o dado e a referência para o próximo, sem limite de tamanho pré-definido, inserção no final e remoção no início são eficiêntes, mas exige gerenciamento de ponteiros e cuidados com alocação e liberação de memória
- Ideal para situações onde os dados devem ser <b>processados na ordem em que chegam</b>, como filas de impressão, buffers ou sistemas de atendimento.
