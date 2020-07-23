import pandas
import numpy
import math
from scipy import stats

podatki = pandas.read_csv(r"C:\Users\Tinka\Documents\Documents\FMF\3.letnik\Statistika\Seminarska naloga\Statistika_seminarska_naloga\Kibergrad.csv")
# 'TIP' 'CLANOV' 'OTROK' 'DOHODEK' 'CETRT' 'IZOBRAZBA'


###############
# a) 
###############

n = 200 # velikost vzorca
vzorec = podatki.sample(n=n)

# naj bo m število družin, v katerih je stopnja izobrazbe vodje gospodinstva
# na intervalu [31,38]
delez = vzorec[vzorec["""'IZOBRAZBA'"""] <= 38]["""'IZOBRAZBA'"""].count() / n
print('Delež družin z iskano lastnostjo v vzorcu je ' + str(delez))


###############
# b) 
###############

N = 43886 # stevilo druzin
stand_napaka_vzorca = math.sqrt( (N-n) / (N-1) / n * delez * (1-delez) )
print('Standardna napaka deleža v vzorcu je ' + str(stand_napaka_vzorca))

# 95% interval zaupanja alfa = 0.05
z_alfa = 1.96
a = delez - stand_napaka_vzorca * z_alfa
b = delez + stand_napaka_vzorca * z_alfa
print('Interval zaupanja je [' + str(a) + ',' + str(b) + ']')


###############
# c) 
###############

pop_delez = podatki[podatki["""'IZOBRAZBA'"""] <= 38]["""'IZOBRAZBA'"""].count() / N
print('Delež družin z iskano lastnostjo v populaciji je ' + str(pop_delez))

stand_napaka = math.sqrt( (N-n) / (N-1) / n * pop_delez * (1-pop_delez) )
print('Standardna napaka deleža v populaciji je ' + str(stand_napaka))

razlika_delez = abs(delez - pop_delez)
razlika_napaka = abs(stand_napaka_vzorca - stand_napaka)
print('Razlika med deležema je ' + str(razlika_delez))
print('Razlika med standardnima napakama je ' + str(razlika_napaka))


###############
# d), e)
###############

intervali = [[a,b]]
delezi = [delez]
stand_odkloni = []
k = 0 # število intervalov, ki pokrijejo populacijski delež

for i in range(99):
    vzorec = podatki.sample(n=n)

    delez = vzorec[vzorec["""'IZOBRAZBA'"""] <= 38]["""'IZOBRAZBA'"""].count() / n
    delezi.append(delez)

    stand_napaka_vzorca = math.sqrt( (N-n) / (N-1) / n * delez * (1-delez) )
    stand_odkloni.append(stand_napaka_vzorca)
    
    a = delez - stand_napaka_vzorca * z_alfa
    b = delez + stand_napaka_vzorca * z_alfa
    intervali.append([a,b])

    if pop_delez >= a and pop_delez <= b:
        k += 1

# PLOTANJE!
print(k)


###############
# f) 
###############


