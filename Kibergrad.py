import pandas
import math
import statistics
import matplotlib.pyplot as plt

podatki = pandas.read_csv(r"C:\Users\Tinka\Documents\Documents\FMF\3.letnik\Statistika\Seminarska naloga\Statistika_seminarska_naloga\Kibergrad.csv")
# 'TIP' 'CLANOV' 'OTROK' 'DOHODEK' 'CETRT' 'IZOBRAZBA'


###############
# a) 
###############

n = 200 # velikost vzorca
vzorec = podatki.sample(n=n)
delez = vzorec[vzorec["""'IZOBRAZBA'"""] <= 38]["""'IZOBRAZBA'"""].count() / n
print('a) Delež družin z iskano lastnostjo v vzorcu je ' + str(delez))


###############
# b) 
###############

N = 43886 # stevilo druzin / velikost populacije
stand_napaka_vzorca = math.sqrt( (N-n) / (n-1) / N * delez * (1-delez) )
print('b) Standardna napaka deleža v vzorcu je ' + str(stand_napaka_vzorca))

# 95% interval zaupanja: alfa = 0.05
z_alfa = 1.96
a = delez - stand_napaka_vzorca * z_alfa
b = delez + stand_napaka_vzorca * z_alfa
print('b) Interval zaupanja je [' + str(a) + ',' + str(b) + ']')


###############
# c) 
###############

pop_delez = podatki[podatki["""'IZOBRAZBA'"""] <= 38]["""'IZOBRAZBA'"""].count() / N
print('c) Delež družin z iskano lastnostjo v populaciji je ' + str(pop_delez))

pop_var = 0
izobrazba = podatki["""'IZOBRAZBA'"""].to_list() # podatki o celotni populaciji
for i in range(N):
    if izobrazba[i] <= 38:
        izobrazba[i] = 1
    else:
        izobrazba[i] = 0
    pop_var += (izobrazba[i] - pop_delez) ** 2 / (N**2)
stand_napaka = math.sqrt(pop_var)

print('c) Standardna napaka deleža v populaciji je ' + str(stand_napaka))

razlika_delez = abs(delez - pop_delez)
razlika_napaka = abs(stand_napaka_vzorca - stand_napaka)
print('c) Razlika med deležem v vzorcu in populaciji je ' + str(razlika_delez))
print('c) Razlika med standardno napako v vzorcu in populaciji je ' + str(razlika_napaka))


###############
# d)
###############

m = 100 # število vzorcev 
delezi = [delez]
stand_napake = [stand_napaka_vzorca]
delta = [stand_napaka_vzorca * z_alfa] # potrebujemo za graf
k = 0 # število intervalov, ki pokrijejo populacijski delež

if pop_delez >= a and pop_delez <= b: # preverimo interval iz prvega vzorca 
        k += 1

for i in range(m-1):
    vzorec = podatki.sample(n=n)

    delez = vzorec[vzorec["""'IZOBRAZBA'"""] <= 38]["""'IZOBRAZBA'"""].count() / n
    delezi.append(delez)

    stand_napaka_vzorca = math.sqrt( (N-n) / (n-1) / N * delez * (1-delez) )  
    delta.append(stand_napaka_vzorca * z_alfa)
    
    a = delez - stand_napaka_vzorca * z_alfa
    b = delez + stand_napaka_vzorca * z_alfa
    if pop_delez >= a and pop_delez <= b:
        k += 1

print('d) ' + str(k) + ' intervalov pokrije populacijski delež.')

plt.figure()
plt.errorbar(list(range(1,m+1)), delezi, xerr=0, yerr=delta, fmt='none')
plt.plot(list(range(1,m+1)), m * [pop_delez])
plt.show()


###############
# e) 
###############

povp_delez_vzorcev = statistics.mean(delezi)
stand_odklon = 0
for i in range(m):
    stand_odklon += (delezi[i] - povp_delez_vzorcev) ** 2
stand_odklon = math.sqrt(stand_odklon / m)

print('e) Standardni odklon vzorčnih deležev je ' + str(stand_odklon))
print('e) Razlika med pravo standardno napako in odklonom vzorčnih deležev je ' + str(abs(stand_odklon - stand_napaka)))


###############
# f) 
###############

m = 100 # število vzorcev 
n = 800 # število družin v vzorcu
delezi = []
delta = []
j = 0 # število intervalov, ki pokrijejo populacijski delež

for i in range(m):
    vzorec = podatki.sample(n=n)

    delez = vzorec[vzorec["""'IZOBRAZBA'"""] <= 38]["""'IZOBRAZBA'"""].count() / n
    delezi.append(delez)

    stand_napaka_vzorca = math.sqrt( (N-n) / (n-1) / N * delez * (1-delez) )  
    delta.append(stand_napaka_vzorca * z_alfa)

    a = delez - stand_napaka_vzorca * z_alfa
    b = delez + stand_napaka_vzorca * z_alfa
    if pop_delez >= a and pop_delez <= b:
        j += 1

povp_delez_vzorcev = statistics.mean(delezi)
stand_odklon = 0
for i in range(m):
    stand_odklon += (delezi[i] - povp_delez_vzorcev) ** 2
stand_odklon = math.sqrt(stand_odklon / m)

print('f) ' + str(j) + ' intervalov pokrije populacijski delež.')
print('f) Standardni odklon vzorčnih deležev je ' + str(stand_odklon))
print('f) Razlika med pravo standardno napako in odklonom vzorčnih deležev je ' + str(abs(stand_odklon - stand_napaka)))

plt.figure()
plt.errorbar(list(range(1,m+1)), delezi, xerr=0, yerr=delta, fmt='none')
plt.plot(list(range(1,m+1)), m * [pop_delez])
plt.show()