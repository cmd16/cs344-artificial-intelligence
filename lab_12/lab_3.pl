/**
Demonstrating the woman is a witch.
*/

/*
  BEDEMIR:  Quiet, quiet.  Quiet!  There are ways of telling whether
      she is a witch.
  BEDEMIR:  Tell me, what do you do with witches?
  VILLAGER #2:  Burn!
  CROWD:  Burn, burn them up!
*/
witch(X) :- burns(X), female(X).

/*
  BEDEMIR:  And what do you burn apart from witches?
  VILLAGER #1:  More witches!
  VILLAGER #2:  Wood!
  BEDEMIR:  So, why do witches burn?
      [pause]
  VILLAGER #3:  B--... 'cause they're made of wood...?
  BEDEMIR:  Good!
  CROWD:  Oh yeah, yeah...
*/
burns(X) :- wooden(X).

/*
  BEDEMIR:  So, how do we tell whether she is made of wood?
  VILLAGER #1:  Build a bridge out of her.
  BEDEMIR:  Aah, but can you not also build bridges out of stone?
  VILLAGER #2:  Oh, yeah.
  BEDEMIR:  Does wood sink in water?
  VILLAGER #1:  No, no.
  VILLAGER #2:  It floats!  It floats!
*/
wooden(X) :- floats(X).

/*
  BEDEMIR:  What also floats in water?
...
  ARTHUR:  A duck.
  CROWD:  Oooh.
  BEDEMIR:  Exactly!  So, logically...,
  VILLAGER #1:  If... she.. weighs the same as a duck, she's made of wood.
  BEDEMIR:  And therefore--?
  VILLAGER #1:  A witch!
*/
floats(X) :- sameWeight(duck, X).

/*
  BEDEMIR:  We shall use my larger scales!
      [yelling]
  BEDEMIR:  Right, remove the supports!
      [whop]
      [creak]
  CROWD:  A witch!  A witch!
  WITCH:  It's a fair cop.
  CROWD:  Burn her!  Burn!  [yelling]
*/
female(girl). /* by observation */
sameWeight(duck, girl). /* by experiment */
