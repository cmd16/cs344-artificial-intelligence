word(astante,  a,s,t,a,n,t,e).
word(astoria,  a,s,t,o,r,i,a).
word(baratto,  b,a,r,a,t,t,o).
word(cobalto,  c,o,b,a,l,t,o).
word(pistola,  p,i,s,t,o,l,a).
word(statale,  s,t,a,t,a,l,e).

% crossword([], [], [], [], [], []).  % base case?

% crossword([V1|TV1], [V2|TV2], [V3|TV3, [H1|TH1], [H2|TH2], [H3|TH3]) :- word(V1), word(V2), word(V3), word(T1), word(T2), word(T3), crossword(TV1, TV2, TV3, TH1, TH2, TH3).

/**
I tried to work on this one, but I just couldn't understand how it's supposed to work. (My attempts are commented out above).

Is the predicate supposed to return some sort of a 2d list? Do we put in variables for the words and have Prolog fill it in?
I get that we want the letters to match up to make the crossword, but it's not like the list translation
where we're comparing element by element.
The 2nd element of each of V1, V2, and V3 need to line up with the 2nd, 4th, and 6th elements respectively of H1.
The 4th element of each of V1, V2, and V3 need to line up with the 2nd, 4th, and 6th elements respectively of H2.
The 6th element of each of V1, V2, and V3 need to line up with the 2nd, 4th, and 6th elements respectively of H3.

Should the order within the vertical words and the order within the horizontal words matter?
(i.e., is crossword(astante, astoria, baratto, cobalto, pistola, statale) different from
crossword(baratto, astoria, astante, pistola, cobalto, statale)?)

The example here doesn't tell us which of the given words are vertical and which of the given words are horizontal.
Are we supposed to figure that out manually, or is Prolog supposed to figure that out for us?

I don't know what the base case or the recursive case is supposed to be.
Also, in the word predicate we don't just have a sequence of letters as the argument,
we have the word and then the sequence of all its letters.

Since I was completely lost and it looks like this isn't graded anyway, I decided to look at an existing solution and see if it
worked. I found (from https://github.com/dragonwasrobot/learn-prolog-now-exercises/blob/master/chapter-02/exercises.pl).
It worked for the person who posted it, but not for me.

I got:
V1 = H1, H1 = astante,
V2 = H2, H2 = baratto,
V3 = H3, H3 = statale .

 a b s
astante
 t r a
baratto
 n t a
statale
 e o e

which technically works but is probably not what's supposed to happen. A word cannot be used more than once
(the following definition of crossword did not impose such a restriction). I think something about the way Prolog was doing its unification meant it gave an invalid solution.
The posted solution used a different set of words than exercise 2.4 did and the solution worked with the words the solution used,
but not with the words my problem used. I figured out how to enforce that the no word could be used more than once and got a correct solution:

 a b s
astante
 t r a
cobalto
 r t a
pistola
 a o e

The other solution Prolog provided was also correct.

*/


/**
My comment based on my understanding of the other person's code. Their code follows after this comment block
(with an additional constraint from me to make sure no word is used more than once).
treat each of the cells of the crossword as a variable
use _ where the variable name doesn't matter because there is no intersection (e.g., we don't care about the first letter of V1 as long as V1 is a word).
*/


crossword(V1,V2,V3,H1,H2,H3) :-
  % Make the word intersect at the right places.
  % Use _ where we don't give a fuck about variable name.
  word(H1,_,H12V12,_,H14V22,_,H16V32,_),
  word(H2,_,H22V14,_,H24V24,_,H26V34,_),
  word(H3,_,H32V16,_,H34V26,_,H36V36,_),

  word(V1,_,H12V12,_,H22V14,_,H32V16,_),
  word(V2,_,H14V22,_,H24V24,_,H34V26,_),
  word(V3,_,H16V32,_,H26V34,_,H36V36,_),

  %% my (cmd16) addition to enforce that a word cannot be used more than once.
  V1 \= V2, V1 \= V3, V1 \= H1, V1 \= H2, V1 \= H3,
  V2 \= V3, V2 \= H1, V2 \= H2, V2 \= H3,
  V3 \= H1, V3 \= H2, V3 \= H3,
  H1 \= H2, H1 \= H3, H2 \= H3.

