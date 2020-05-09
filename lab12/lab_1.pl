/**
Excercise 1.4
Explain why you built the representations as you did.

For the most part I just wrote things following the way you are supposed to write things in Prolog and I don't know what else to say.
*/

% Butch is a killer.
killer(butch).

% Mia and Marsellus are married.
% I wrote some additional rules based on the meaning of "married" in the English language.
married(mia, marsellus).
married(X, Y) :- married(Y, X), X \= Y.
married(X) :- married(X, _).

% Zed is dead.
dead(zed).

% Marsellus kills everyone who gives Mia a footmassage.
kills(X, marsellus) :- givesFootMassage(X, mia).

% Mia loves everyone who is a good dancer.
loves(mia, X) :- goodDancer(X).

% Jules eats anything that is nutritious or tasty.
eats(jules, X) :- nutritious(X).
eats(jules, X) :- tasty(X).

/**
Exercise 1.5
Explain how Prolog comes up with its answers.
*/

wizard(ron).
hasWand(harry).
quidditchPlayer(harry).
wizard(X):-  hasBroom(X),  hasWand(X).
hasBroom(X):-  quidditchPlayer(X).

/**
How does Prolog respond to the following queries?

wizard(ron).
true.
This is a fact in the knowledge base.

witch(ron).
ERROR: Undefined procedure: witch/1 (DWIM could not correct goal)
witch is not a predicate we have defined.

wizard(hermione).
false.
hermione does not exist in the knowledge base.

witch(hermione).
ERROR: Undefined procedure: witch/1 (DWIM could not correct goal)
witch is not a predicate we have defined.

wizard(harry).
true.
harry is a quidditchPlayer, so he has a broom. harry has a wand. harry has a broom and a wand, so harry is a wizard.

wizard(Y).
ron.
ron is the first atom Y that prolog found in the knowledge base for which Y is a wizard. If you type ; then you get harry. because harry is also a wizard.

witch(Y).
ERROR: Undefined procedure: witch/1 (DWIM could not correct goal)
witch is not a predicate we have defined.

*/
