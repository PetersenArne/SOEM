# help me...

s = input()
indices = [0x0,0x2,0x9,0x16,0x19,0x20]
idn_byte = []
for ids in indices:
    idn_byte.append(ids * 2)

parts = [s[i:j] for i,j in zip(idn_byte, idn_byte[1:]+[None])]

#print("s2               [ " + parts[0] + " ]")
print("s3 rx 0x2080     [ " + parts[1] + " ]")
print("s4 tx 0x1300     [ " + parts[2] + " ]")
#print("s1 & s2          [ " + parts[3] + " ]")
print("s3 tx 0x1100     [ " + parts[4] + " ]")
print("s4 rx 0x1200     [ " + parts[5] + " ]")