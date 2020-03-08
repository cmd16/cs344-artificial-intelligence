from probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.90, F: 0.02}),
    ('Test2', 'Cancer', {T: 0.90, F: 0.02})
    ])

print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

'''
These results make sense. Testing positive on both tests means it is more likely that you have cancer, but only 95% 
because we still need to account for the rarity of cancer. One negative test result has a pretty large impact on the 
probability of having cancer.

P(Cancer|~Test2)=P(Cancer|~Test1) since both tests have the same probabilities.
P(Cancer|~Test1)= a<P(Cancer)*P(~Test1|Cancer), P(~Cancer)*P(~Test1|~Cancer)>
= a<0.01*0.1, 0.99*0.8>
= <0.001261, 0.9987>
'''
