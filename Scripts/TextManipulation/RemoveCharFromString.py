
f = open("Text.txt",encoding="utf-8")

lines = f.readlines()
out = ""
for line in lines:
    line = line.strip('\n')
    line = [l for l in line if ord(l) != ord('-') and ord(l) != ord('•')]
    line = ''.join(line)
    out += line

f.close()
print(out)
o = open("outText.txt","w",encoding="utf-8")
o.write(out)