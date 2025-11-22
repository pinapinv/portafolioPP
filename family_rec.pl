female(pam).
female(liz).
female(pat).
female(ann).

male(jim).
male(bob).
male(tom).
male(pete).

parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jim).
parent(pete,jim).

mother(X,Y):- parent(X,Y), female(X).
father(X,Y):- parent(X,Y), male(X).
sister(X,Y):- parent(Z,X), parent(Z,Y), female(X), X\==Y.
brother(X,Y):- parent(Z,X), parent(Z,Y), male(X), X\==Y.

predecessor(X,Z) :- parent(X,Z).
predecessor(X,Z) :- parent(X,Y), predecessor(Y,Z).
