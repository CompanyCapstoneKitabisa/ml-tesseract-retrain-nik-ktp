import random

i = 0
_temp = []
output = []

with open("MOCK_DATA.txt") as f:
    for line in f:
        if i>5:
            break
        _temp = [x for x in line[:-1]]
        if line.startswith("0"):
            _temp.remove("0")
            _temp.append(str(random.randrange(1, 6, 1)))
        _temp.insert(0, "NIK : ")
        line = "".join(_temp)
        output.append(line)
    
with open("output.txt", "r+") as f:
    for i in output:
        f.write(i)
        f.write('\n')