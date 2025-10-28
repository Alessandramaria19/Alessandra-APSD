elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]
for index in range(len(elevi)):
    print(elevi[index],"are nota",note[index])

min=11
max=-1
imin=0
imax=0
for index in range(len(note)):
    if note[index]<min:
        min=note[index]
        imin=index
    elif note[index]>max:
        max=note[index]
        imax=index
print(min,'-',elevi[imin])
print(max,'-',elevi[imax])
sum=0
for index in range(len(note)):
     sum=sum+note[index]
ma=sum/len(note)
print(int(ma*100)/100)
for index in range(len(note)):
    if note[index]>=5:
        print(elevi[index])
for index in range(len(note)):
    if note[index]<10:
        note[index]=note[index]+1
elevi.append(elev_nou)
note.append(nota_elev_nou)
for index in range(len(elevi)):
    if elevi[index]==elev_de_sters:
        nota_de_sters=index
elevi.remove(elev_de_sters)
note.remove(note[nota_de_sters])
for index in range(len(elevi)):
    print(elevi[index],"are nota",note[index])
index=0
while index<len(interogari_nume) and interogari_nume[index]!='stop':
    if interogari_nume[index]!='stop':
        print(note[index])
    else:
        print("Nu exista")
    index+=1
admisi=0
respinsi=0
for index in range(len(note)):
    if note[index]>=5:
        admisi+=1
    else:
        respinsi+=1
print(admisi,'-',respinsi)
promovati = []
for n in note:
    if n>= 5:
        promovati.append(n)
sm=0
for index in range(len(promovati)):
    if promovati[index]>=5:
        sm+=promovati[index]
md=sm/len(promovati)
print(int(md*100)/100)

