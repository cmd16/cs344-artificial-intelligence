/**
Exercise 2.1, questions 1, 2, 8, 9, 14 - Give the necessary instantiations.

1. bread  =  bread
unifies

2. ’Bread’  =  bread
does not unify.

8. food(X)  =  food(bread)
unifies. necessary instantiation: food(X)  =  food(bread).

9. food(bread,X)  =  food(Y,sausage)
unifies. necessary instantiations: X = sausage, Y = bread.

14. meal(food(bread),X)  =  meal(X,drink(beer))
does not unify.
*/

/**
Exercise 2.2 - Explain how Prolog does its unification and reasoning. If you have issues getting the results you’d expect, are there things you can do to game the system?
*/

house_elf(dobby).
witch(hermione).
witch('McGonagall').
witch(rita_skeeter).
wizard(harry).
magic(X):-  house_elf(X).
magic(X):-  wizard(X).
magic(X):-  witch(X).

/**
Which of the following queries are satisfied? Where relevant, give all the variable instantiations that lead to success.

I got a lot of ERROR: Undefined procedure: wizard/1 (DWIM could not correct goal), so I added wizard(harry) so prolog knows what a wizard is.

?-  magic(house_elf).
Not satisfied (house_elf is a procedure not a variable). Before I corrected the Undefined procedure error, I was getting that error here.


?-  wizard(harry).
Before I corrected the Undefined procedure error, I was getting that error here.
After adding it, wizard(harry) is true.

?-  magic(wizard).
Not satisfied (magic and wizard are both procedures).
Before I corrected the Undefined procedure error, I was getting that error here.

?-  magic('McGonagall').
Satisfied.
Before I corrected the Undefined procedure error, I was getting that error here.

?-  magic(Hermione).
Because Hermione starts with uppercase it is treated as a variable. Prolog goes through every possible assignment to Hermione.
Hermione could be any of our things that are magic (dobby is the first item found).
?- magic(Hermione).
Hermione = dobby ;
Hermione = harry ;
Hermione = hermione ;
Hermione = 'McGonagall' ;
Hermione = rita_skeeter.

Draw the search tree for the query magic(Hermione) .
*/
