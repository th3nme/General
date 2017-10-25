# My Measurements
name = 'Nick Ephraims'
age = 27 # not a lie
height = 192 # centimetres
weight = 95 # kilograms
eyes = 'Green'
teeth = 'White'
hair = 'Brown'
weight_in_pounds = weight * 2.2
height_in_inches = height / 2.5

print "Let's talk about %s." % name
print "He's %d centimetres tall." % height
print "He's %d inches tall." % height_in_inches
print "He's %d kilograms heavy." % weight
print "He's %d pounds heavy." % weight_in_pounds
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (
    age, height, weight, age + height + weight)
