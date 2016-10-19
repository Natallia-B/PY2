l = 'Te Zen of Python, by Tim Peters \
Beautiful is better than ugly. \
Explicit is better than implicit. \
Simple is better than complex. \
Complex is better than complicated. \
Flat is better than nested. \
Sparse is better than dense. \
Readability counts. \
Special cases aren \'t special enough to break the rules. \
Although practicality beats purity. \
Errors should never pass silently. \
Unless explicitly silenced. \
In the face of ambiguity, refuse the temptation to guess. \
There should be one-- and preferably only one --obvious way to do it. \
Although that way may not be obvious at first unless you\'re Dutch. \
Now is better than never. \
Although never is often better than *right* now. \
If the implementation is hard to explain, it\'s a bad idea. \
If the implementation is easy to explain, it may be a good idea. \
Namespaces are one honking great idea -- let\'s do more of those!'
l = '{0} nokatami@gmail.com'.format(l)

print 'The famous "Te Zen of Python" will count ',len(l), ' symbols, if I add my humble email to it'
i = 0
j = 0
while i < len(l):
    if l.lower()[i] == 'a' or l.lower()[i] == 'o' or l.lower()[i] == 'u' or l.lower()[i] == 'e' or l.lower()[i] == 'i' or l.lower()[i] == 'y':
        j += 1
    i += 1
print 'Among them', j, 'vowels'
print 'Every 18-th symbol ...'
i=18
while i < len(l):
    if l[i].isupper():
        print i, l.lower()[i]
    else:
        print i, l.upper()[i]
    i+=18

