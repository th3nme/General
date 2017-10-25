# create a mapping of state to abbreviation
states = {
    'Queensland': 'QLD',
    'New South Wales': 'NSW',
    'Victoria': 'VIC',
    'South Australia': 'SOU',
    'Westers Australia': 'WA'
}

# create a basic set of states and some cities in them
cities = {
    'QLD': 'Brisbane',
    'NSW': 'Sydney',
    'VIC': 'Melbourne'
}

# add some more cities
cities['SOU'] = 'Adelaide'
cities['WA'] = 'Perth'

#  print out some cities
print '-' * 10
print "QLD state has: ", cities['QLD']
print "NSW State has: ", cities['NSW']

# print out some states
print '-' * 10
print "Queensland's abbreviation is: ", states['Queensland']
print "New South Wales' Abbreviation is: ", states['New South Wales']

# do it by using the state then cities dictionary
print '-' * 10
print "Queensland has: ", cities[states['Queensland']]
print "New South Wales has: ", cities[states['New South Wales']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s is abbreviated %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has the city: %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
