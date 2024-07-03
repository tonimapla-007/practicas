filename = 'aprender_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)
lineas = lines    
pi_string = ''
for line in lines:
    if 'python' in line:
        lin = line.replace('python', 'C')
        print(lin)
    pi_string += line.strip()
    
#print(pi_string)
#print(lineas)
