import pandas as pd

def pp(z):
    print('\n', z)

# Given a list representing a few planets
planets = ['Earth', 'Saturn', 'Venus', 'Mars', 'Jupiter']

# Given another list representing the distance of each of these planets from the Sun
# The distance from the Sun is in units of 10^6 km
distance_from_sun = [149.6, 1433.5, 108.2, 227.9, 778.6]

dis_planets = pd.Series(distance_from_sun, planets)
pp(dis_planets)

time_light = dis_planets / 18
pp(time_light)

close_planets = time_light[ time_light < 40]
pp(close_planets)