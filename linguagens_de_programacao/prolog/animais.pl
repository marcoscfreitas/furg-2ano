% especies dos animais
passaro(tweety).
peixe(goldie).
minhoca(molie).
gato(silvester).

% silvester meu gato e meu amigo
meu_gato(silvester).
meu_amigo(silvester).

% alimento de cada animal
gosta(X, Y) :- passaro(X), minhoca(Y).        % pássaros gostam de minhocas
gosta(X, Y) :- gato(X), peixe(Y).             % gatos gostam de peixes
gosta(X, Y) :- gato(X), passaro(Y).           % gatos gostam de pássaros

% amigos gostam uns dos outros
gosta(X, Y) :- meu_amigo(X), meu_amigo(Y).    % se ambos são meus amigos
gosta(X, eu) :- meu_amigo(X).                 % meu amigo gosta de mim
gosta(eu, X) :- meu_amigo(X).                 % eu gosto do meu amigo

% meu gato come tudo o que gosta
come(X, Y) :- meu_gato(X), gosta(X, Y).

% Para encontrar tudo o que Silvester come:
% ?- come(silvester, X).