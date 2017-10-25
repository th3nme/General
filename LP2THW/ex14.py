from sys import argv

# Import argv
script, user_name = argv
prompt = '> '

# Ask whether user likes me
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

# Find out where user lives
print "Where do you live %s?" % user_name
lives = raw_input(prompt)

# Find out what computer the user has
print "What kind of computer do you have?"
computer = raw_input(prompt)

# Print the summary
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
