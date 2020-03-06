from probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

happiness = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F):0.1}),
    ])

print(enumeration_ask('Raise', dict(Sunny=T), happiness).show_approx())
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), happiness).show_approx())

print(enumeration_ask('Raise', dict(Happy=T), happiness).show_approx())
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happiness).show_approx())
