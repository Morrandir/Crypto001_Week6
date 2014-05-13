import gmpy2
from gmpy2 import mpz

__author__ = 'Qubo'

PrimeN = '17976931348623159077293051907890247336179769789423065727343008115'
PrimeN += '77326758055056206869853794492129829595855013875371640157101398586'
PrimeN += '47833778606925583497541085196591615128057575940752635007475935288'
PrimeN += '71082364994994077189561705436114947486504671101510156394068052754'
PrimeN += '0071584560878577663743040086340742855278549092581'

gmpy2.set_context(gmpy2.context(precision=2000))

N = mpz(PrimeN)
A = gmpy2.ceil(gmpy2.sqrt(N))
SquareA = gmpy2.square(A)

if gmpy2.is_square(gmpy2.sub(SquareA, N)):
    x = gmpy2.sqrt(gmpy2.sub(SquareA, N))
    print 'p = ' + str(A - x)
    print 'q = ' + str(A + x)
else:
    print 'x is not square, must be wrong...'