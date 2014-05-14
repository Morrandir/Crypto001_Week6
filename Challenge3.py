import gmpy2
from gmpy2 import mpz
from gmpy2 import mpfr

__author__ = 'Qubo'

N1 = '17976931348623159077293051907890247336179769789423065727343008115'
N1 += '77326758055056206869853794492129829595855013875371640157101398586'
N1 += '47833778606925583497541085196591615128057575940752635007475935288'
N1 += '71082364994994077189561705436114947486504671101510156394068052754'
N1 += '0071584560878577663743040086340742855278549092581'

N2 = '6484558428080716696628242653467722787263437207069762630604390703787'
N2 += '9730861808111646271401527606141756919558732184025452065542490671989'
N2 += '2428844841839353281972988531310511738648965962582821502504990264452'
N2 += '1008852816733037111422964210278402893076574586452336833570778346897'
N2 += '15838646088239640236866252211790085787877'

N3 = '72006226374735042527956443552558373833808445147399984182665305798191'
N3 += '63556901883377904234086641876639384851752649940178970835240791356868'
N3 += '77441155132015188279331812309091996246361896836573643119174094961348'
N3 += '52463970788523879939683923036467667022162701835329944324119217381272'
N3 += '9276147530748597302192751375739387929'

diff = 1

gmpy2.set_context(gmpy2.context(precision = 3000))

N = mpz(N3)
lowerBound = mpz(gmpy2.ceil(gmpy2.mul(2, gmpy2.sqrt(gmpy2.mul(6, N)))))

for i in range(0, diff):
    A = gmpy2.div(mpfr(gmpy2.add(lowerBound, i)), 2)
    SquareA = gmpy2.square(A)
    x = gmpy2.sqrt(gmpy2.sub(SquareA, gmpy2.mul(6, N)))
    if gmpy2.is_integer(gmpy2.div(gmpy2.sub(A, x), 3)) and gmpy2.is_integer(gmpy2.div(gmpy2.add(A, x), 2)):
        print 'p = ' + str(mpz(gmpy2.div(gmpy2.sub(A, x), 3)))
        print 'q = ' + str(mpz(gmpy2.div(gmpy2.add(A, x), 2)))
    else:
        print 'p = ' + str(mpz(gmpy2.div(gmpy2.add(A, x), 3)))
        print 'q = ' + str(mpz(gmpy2.div(gmpy2.sub(A, x), 2)))