# just adding to a container,
fruit = ['Apple', 'Orange', 'Pear']
fruit.append('Banana')
fruit.append('Peach')

print(fruit)

# Dictionary lists are coded to search through, code = fun, so searching for code will push fun to the terminal
facts = dict()

facts['code'] = 'fun'
facts['Bill'] = 'Gates'
facts['founded'] = 1776

print(1776 in facts)

# Similar here, looking for all Bill Gates in the bill dict

bill = dict({'Bill Gates' : 'Charitable'})
print('Bill Gates' in bill)

# You can remove a pair by using del *Dic name* ['keyword']
# E.G.

books = {'Dracula': 'Stoker',
         '1984': 'Orwell',
         'The Trial': 'Kafka'}

print(books) 

# The Trial: Kafka is shown

del books['The Trial']
 
print(books)

# No longer showing The Trial : Kafka

# You can have list within lists

lists = []
rap = ['Kanye West',
       'Jay Z',
       'Eminem',
       'Nas']
 
 
rock = ['Bob Dylan',
        'The Beatles',
        'Led Zeppelin']
 
 
djs = ['Zeds Dead',
       'Tiesto']
 
 
lists.append(rap)
lists.append(rock)
lists.append(djs)
 
 
print(lists)

#Each list is seperated in terminal by [[ITEM,ITEM,ITEM], [ITEM, ITEM ITEM]]

print(lists[0])

# Items are now grouped in numbers, so 0 is rap, 1 is rock and 2 is djs

rap.append('Kendrick Lamar')
print(rap)
print(lists)


