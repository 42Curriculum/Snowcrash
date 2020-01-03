import crypt as C

#print(psswd)
f = open("passlist.txt", encoding="utf8", errors="ignore")
line = f.readlines()
for x in line: 
    psswd = C.crypt(x.rstrip(), "42")
    if psswd == "42hDRfypTqqnw":
        print(x)