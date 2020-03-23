import math
pshfio = 0
pinakas =[]

x = int(input("Enter the 16 digits of your card: "))
for j in range(16):
    upoloipo = math.fmod(x,10) #Διαιρω τον αριθμο με 10 και για καθε επαναληψη βρισκω το υπολοιπο
    phliko = (x-upoloipo)/10 #Δινω στην μεταβλητη phliko την τιμη του πηλικου
    pshfio = x - phliko*10 #εκχωρω την τιμη του ψηφιου των δεκαδων στην μεταβλητη "pshfio" 
    pinakas.append(pshfio) #Στον πινακα θα τοποθετουνται τα ψηφια του 16-ψηφιου αριθμου ενα προς ενα για καθε επαναληψη
    x = phliko

print("The digits you entered are: ",pinakas)
sum = 0

for j in range(0,16,1):  #H μετρηση του πινακα ξεκιανει απο το 2 ψηφιο αλλα δεν υπολογιζει το τελευταιο
    a = pinakas[j] #εκχωρω καθε 2ο στοιχειο του πινακα στην μεταβλητη a
    checker = a*2 #διπλασιαζω την μεταβλητη a
    print(checker, j)
    if checker >= 10: #αν ο αριθμος, που προκυπτει απο τον διπλασιασμο, ειναι μεγαλυτερο του 10, τοτε 
        b = math.fmod(checker,10) #2ο ψηφιο
        sum_digits = b +(checker-b)/10 #Αθροισμα ψηφιων της μεταβλητης checker
        print(checker, b, sum_digits) #print ελεγχου
        pinakas.remove(a) #αφαιρω απο την λιστα τον 2-ψηφιο αριθμο
        pinakas.append(sum_digits) #και τον αντικαθιστω με το αθροισμα των ψηφιων του

for j in range(16):
    sum += pinakas[j]

if math.fmod(sum*9,10) == pinakas[15] : #Επιβεβαιωση για την ορθοτητα του αριθμου
    print("Confirmed!")
else :
    print("Invalid number!")
