from flight import Segment, Flight


seg = [Segment('EDI', 'LHR'), Segment('LHR', 'CAN')]
flight = Flight(seg)

print(flight.departure_point)
print(flight)

flight.departure_point = 'GLA'
print('...Set departure to GLA...')

print(flight.departure_point)
print(flight)