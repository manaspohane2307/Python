file = open('youtube.txt', 'w')

try:
    file.write('I am writing to file')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('I am writing again to file')