different(X, X) :- !, fail. % Si X y Y son iguales, falla
different(X, Y). % Si X y Y son diferentes, tiene éxito