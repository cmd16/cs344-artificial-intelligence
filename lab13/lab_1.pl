/**

a. Do these exercises from LPN!.
  Exercise 3.2
  Exercise 4.5

b. Does Prolog implement a version of generalized modus ponens (i.e., modus ponens with variables and instantiation)? If so, demonstrate how it’s done; if not, explain why not. If it doesn’t, can you implement one? Why or why not?
Be sure that you can explain how you built your system and how Prolog does recursion.

*/


% Exercise 3.2

% katarina has olga directly inside. I would have written it the other way but this seems to be the way the assignment wants things.
directlyIn(katarina, olga).
directlyIn(olga, natasha).
directlyIn(natasha, irina).

in(X, Y) :- directlyIn(X, Y).
in(X, Y) :- directlyIn(X, Z), in(Z, Y).


% Exercise 4.5

tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

/**
Write a predicate listtran(G,E) which translates a list of German number words to the corresponding list of English number words. For example:

   listtran([eins,neun,zwei],X).
should give:

   X  =  [one,nine,two].
Your program should also work in the other direction. For example, if you give it the query

   listtran(X,[one,seven,six,two]).
it should return:

   X  =  [eins,sieben,sechs,zwei].

(Hint: to answer this question, first ask yourself “How do I translate the empty list of number words?”. That’s the base case.
For non-empty lists, first translate the head of the list, then use recursion to translate the tail.)
*/

listtran([], []).
listtran([G|Tg], [E|Te]) :- tran(G, E), listtran(Tg, Te).
% listtran(G|Tg, E|Te) :- tran(G|E)


/**
b. Does Prolog implement a version of generalized modus ponens (i.e., modus ponens with variables and instantiation)? If so, demonstrate how it’s done; if not, explain why not. If it doesn’t, can you implement one? Why or why not?
Be sure that you can explain how you built your system and how Prolog does recursion.

Prolog does implement a version of generalized modus ponens.
When Prolog is given a query that involves variables, Prolog searches through its knowledge base (using recursion as necessary) to find a possible value for X.

I have provided here an example knowledge base based on exercise 1.5 in lab 12.

Let us suppose that we ask the query wizard(X). Prolog sees that for wizard(X) to be true, we need hasBroom(X) to be true and hasWand(X) to be true.
hasBroom(dobby) is true, but hasWand(dobby) is false (since that fact isn't in the knowledge base). So X cannot be dobby.
hasBroom(ron) is true, so X can be ron if hasWand(ron) is true. hasWand(ron) is true, so X can be ron, so X is instantiated to ron.

If we type ; then we can search again for another possible instantiation of X.

hasBroom(hagrid) is false, so X cannot be hagrid.
We don't have a fact that says hasBroom(harry). But we do know that quidditchPlayer(harry), and we know that quidditchPlayer(Y) implies hasBroom(Y).
So if we use harry as Y here, then we know that harry is a quidditchPlayer so harry hasBroom. So hasBroom(harry) is true.
hasWand(harry) is true (that's in our knowledge base), so we now know that hasBroom(harry) and hasWand(harry). That means we know that wizard(harry).
So X can also be harry, so X is instantiated to harry.

*/

hasBroom(dobby).
hasBroom(ron).
hasBroom(Y):-  quidditchPlayer(Y).
quidditchPlayer(harry).

hasWand(hagrid).
hasWand(harry).
hasWand(ron).

wizard(X):-  hasBroom(X),  hasWand(X).
