
content = 'a,1\nb,2\nc,3\nd,4\ne,5'

lines = content.splitlines()
lines = [line.split(',') for line in lines]

print(lines)