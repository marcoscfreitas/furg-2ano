% gêneros
homem(abraham).
homem(clancy).
homem(herb).
homem(homer).
homem(bart).
homem(maridoSelma).
homem(ling).

mulher(mona).
mulher(jackie).
mulher(patty).
mulher(selma).
mulher(marge).
mulher(lisa).
mulher(maggie).

% relacionamentos pai e mae
pai(abraham, homer).
pai(abraham, herb).
pai(clancy, marge).
pai(clancy, patty).
pai(clancy, selma).
pai(homer, bart).
pai(homer, lisa).
pai(homer, maggie).
pai(maridoSelma, ling).

mae(mona, homer).
mae(mona, herb).
mae(jackie, marge).
mae(jackie, patty).
mae(jackie, selma).
mae(marge, bart).
mae(marge, lisa).
mae(marge, maggie).
mae(selma, ling).

% casamentos
casado(abraham, mona).
casado(mona, abraham).
casado(clancy, jackie).
casado(jackie, clancy).
casado(homer, marge).
casado(marge, homer).
casado(selma, maridoSelma).
casado(maridoSelma, selma).

% pais
pai_de(X, Y) :- pai(X, Y).
pai_de(X, Y) :- mae(X, Y).

% filhos
filho(X, Y) :- pai_de(Y, X), homem(X).
filha(X, Y) :- pai_de(Y, X), mulher(X).
filho_de(X, Y) :- pai_de(Y, X).

% avós
avo(X, Z) :- pai(X, Y), pai_de(Y, Z), homem(X).
avó(X, Z) :- mae(X, Y), pai_de(Y, Z), mulher(X).
avo_de(X, Z) :- pai_de(X, Y), pai_de(Y, Z).

% netos
neto(X, Y) :- avo_de(Y, X), homem(X).
neta(X, Y) :- avo_de(Y, X), mulher(X).

% irmãos
irmao(X, Y) :- pai_de(Z, X), pai_de(Z, Y), X \= Y, homem(X).
irma(X, Y) :- pai_de(Z, X), pai_de(Z, Y), X \= Y, mulher(X).
irmao_de(X, Y) :- pai_de(Z, X), pai_de(Z, Y), X \= Y.

% tios e tias
tio(X, Y) :- irmao(X, Z), pai_de(Z, Y).
tia(X, Y) :- irma(X, Z), pai_de(Z, Y).
tio_de(X, Y) :- irmao_de(X, Z), pai_de(Z, Y).

% tios e tias por casamento
tio_por_casamento(X, Y) :- casado(X, Z), tia(Z, Y), homem(X).
tia_por_casamento(X, Y) :- casado(X, Z), tio(Z, Y), mulher(X).

% primos
primo(X, Y) :- tio_de(Z, X), pai_de(Z, Y), homem(X).
prima(X, Y) :- tio_de(Z, X), pai_de(Z, Y), mulher(X).
primo_de(X, Y) :- tio_de(Z, X), pai_de(Z, Y).

% lado paterno e materno
lado_paterno(Pai, Filho) :- pai(Pai, Filho).
lado_materno(Mae, Filho) :- mae(Mae, Filho).

% tios e tias por parte de pai
tio_paterno(X, Y) :- pai(Z, Y), irmao(X, Z).
tia_paterna(X, Y) :- pai(Z, Y), irma(X, Z).

% tios e tias por parte de mae
tio_materno(X, Y) :- mae(Z, Y), irmao(X, Z).
tia_materna(X, Y) :- mae(Z, Y), irma(X, Z).

% primos por parte de pai
primo_paterno(X, Y) :- pai(Z, Y), irmao_de(W, Z), pai_de(W, X), homem(X).
prima_paterna(X, Y) :- pai(Z, Y), irmao_de(W, Z), pai_de(W, X), mulher(X).

% primos por parte de mae
primo_materno(X, Y) :- mae(Z, Y), irmao_de(W, Z), pai_de(W, X), homem(X).
prima_materna(X, Y) :- mae(Z, Y), irmao_de(W, Z), pai_de(W, X), mulher(X).

% PERGUNTAS

% a. Quem são as mulheres da família?
% ?- mulher(X).

% b. Quem são seus tios e tias do Bart por parte de mãe?
% ?- tio_materno(X, bart).
% ?- tia_materna(X, bart).

% c. Quem são seus tios e tias do Bart por parte de pai?
% ?- tio_paterno(X, bart).
% ?- tia_paterna(X, bart).

% d. Quem são seus tios e tias do Bart que se casaram com parentes seus?
% ?- (tio_materno(X, bart); tia_materna(X, bart); tio_paterno(X, bart); tia_paterna(X, bart)), casado(X, Y).

% e. Quem são seus primos do Bart por parte de pai?
% ?- primo_paterno(X, bart).
% ?- prima_paterna(X, bart).

% f. Quem são seus primos do Bart por parte de mãe?
% ?- primo_materno(X, bart).
% ?- prima_materna(X, bart).