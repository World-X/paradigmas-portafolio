point(1, 1).
point(2, 3).
seg(point(1, 1), point(2, 3)).
triangle(point(4, Z), point(6, 4), point(7, 1)).

boy(tom).
boy(bob).
girl(alice).
girl(lili).
pay(X, Y) :- boy(X), girl(Y).
