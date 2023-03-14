mappings = { 0x0E:"K",0x10:"M", 0x2C:" "}

nums = []

keys = open('data.txt')


for line in keys:

    if line[:2] != '00' or line[4:6] != '00':
       nums.append(int(line[4:6],16))
    # 00:00:xx:....

keys.close()

output = ""

for n in nums:
    if n == 0:
       continue
    if n in mappings:
       output += mappings[n]
    else:
       output += '[unknown]'

print('output:' + output)
