# Challenges
# 1. Create a list of your favorite musicians.

fav_musicians = ['In Hearts Wake', 'Four Year Strong', 'Enter Shikari', 'Mom Jeans', 'Hot Mulligan']

print(fav_musicians)

# 2. Create a list of tuples, with each tuple containing the longitude and latitude of somewhere you’ve lived or visited.

visitor = (['Croatia', '45.1000 N', '15.2000 E'], ['Italy', '41.8719', '12.5674'], ['Amsterdam', '52.3676', '4.9041'])

print(visitor)
print(visitor[2])

# Did not make a list of tuples, I made a tuple of lists

visitor_fixed = [('Croatia', '45.1000 N', '15.2000 E'), ('Italy', '41.8719', '12.5674'), ('Amsterdam', '52.3676', '4.9041')]

# 3. Create a dictionary that contains different attributes about you: height, favorite color, favorite author, etc.

details = {'height' : 173,
           'Colour' : 'Red',
           'Author' : 'J.R.R Tolkien'
           }

print(details)

# 4. Write a program that lets the user ask your height, favorite color, or favorite author, and returns the result from the dictionary 
# you created in the previous challenge.

details2 = {
    'Height' : input("Please input your height: "),
    'Colour' : input("Please input your favourite colour: "),
    'Author' : input("Please input your favourite author:" ) 
}

print(details2)
print(details2['Author'])

# Anser for 4 below with their example dict, should have looped the query from my own dict instead of prompting and adding
# Need to READ the question, details were missed

me = {
    "height": "6",
    "fav_color": "red",
    "fav_author": "Orwell"
}

answer = input("Type height, fav_color or fav_author")
if answer in me:
    result = me[answer]
    print(result)


# 5. Create a dictionary mapping your favorite musicians to a list of your favorite songs by them.
artists = {
    'metal' : ['Sleep Token', 'Parkway Drive','Ghost'],
    'rap' : ['Kendrick Lamar', 'Mac Miller', 'Amine'],
    'dnb' : ['Chase and Status', 'Dimension', '1991']
}
print(artists)

# 6. Lists, tuples, and dictionaries are just a few of the containers built into Python. Research Python sets (a type of container). When would you use a set?

# Sets are used to store multiple items in a single variable, they are unordered, unchangeable and do not allow duplicate values. If you want an unordered collection of unique
# elements then a set best suits this need.