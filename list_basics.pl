list_member(X, [X|_]). % Con esto verificamos si el elemento es la cabeza de la lista
list_member(X, [_|Tail]) :- list_member(X, Tail). % Con esto verificamos si el elemento es la cola de la lista

list_length([], 0). % La longitud de una lista vacía es 0
list_length([_|Tail], Length) :- list_length(Tail, Length1), Length is Length1 + 1.

list_concat([], L, L). % Concatenar una lista vacía con otra lista
list_concat([H|T], L, [H|R]) :- list_concat(T, L, R). % Concatenar dos listas

list_delete(X, [X], []). % Eliminar un elemento de una lista
list_delete(X, [X|Tail], Tail). % Eliminar un elemento de la cabeza de la lista
list_delete(X, [Y|Tail], [Y|NewTail]) :- list_delete(X, Tail, NewTail). % Eliminar un elemento de la cola de la lista

list_append(A, T, T) :- list_member(A, T), !. % Agregar un elemento a una lista
list_append(A, T, [A|T]). % Agregar un elemento a la cabeza de la lista

list_insert(X, L, R) :- list_delete(X, R, L). % Insertar un elemento en una lista
