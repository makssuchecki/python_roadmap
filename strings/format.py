print('{0}, {1}, {2}'.format('a', 'b', 'c')) # a b c

print('{2}, {1}, {0}'.format('a', 'b', 'c')) # c b a

print('{0}{1}{0}'.format('abra', 'cad')) # abracadabra

print("Coordinates: {latitude}, {longitude}".format(latitude='37.24N', longitude='-115.81W'))

coord = (3, 5)
print('X: {0[0]}; Y: {0[1]}'.format(coord))
