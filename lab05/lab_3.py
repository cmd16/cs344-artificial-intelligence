from probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

happiness = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F):0.1}),
    ])

'''
P(R|S) = P(R) because raise and sunny are independent. So P(R)=0.01
'''
print(enumeration_ask('Raise', dict(Sunny=T), happiness).show_approx())
'''
P(R|HS)= ??
'''
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), happiness).show_approx())

'''
These make sense to me: a raise is so unlikely that even being happy doesn't increase the probability of a raise by much.
Because it is unlikely to be happy while it is not sunny and you have no raise, knowing that you are happy and it is not 
sunny makes it more likely that you have a raise.
'''
print(enumeration_ask('Raise', dict(Happy=T), happiness).show_approx())
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happiness).show_approx())
