import gmpy2
from gmpy2 import mpz

__author__ = 'Qubo'

N1 = '17976931348623159077293051907890247336179769789423065727343008115'
N1 += '77326758055056206869853794492129829595855013875371640157101398586'
N1 += '47833778606925583497541085196591615128057575940752635007475935288'
N1 += '71082364994994077189561705436114947486504671101510156394068052754'
N1 += '0071584560878577663743040086340742855278549092581'

p1 = '134078079299425970995740249982058461274793658205923933777235614437'
p1 += '21764030073662768891111614362326998675040546094339320838419523375'
p1 += '986027530441562135724301'

q1 = '134078079299425970995740249982058461274793658205923933777235614437'
q1 += '21764030073778560980348930557750569660049234002192590823085163940'
q1 += '025485114449475265364281'

ct1 = '22096451867410381776306561134883418017410069787892831071731839143'
ct1 += '6761356001205380042823296504735094243439462197515122564658399679'
ct1 += '4288946076454204058156474898801373486412045232522932017648791666'
ct1 += '6402997509188729971690526083222067771600019329260870009579993724'
ct1 += '077458967773697817571267229951148662959627934791540'

gmpy2.set_context(gmpy2.context(precision=3000))

ct = mpz(ct1)
N = mpz(N1)
p = mpz(p1)
q = mpz(q1)
e = mpz(65537)

phi_N = gmpy2.mul(gmpy2.sub(p, 1), gmpy2.sub(q, 1))

d = gmpy2.invert(e, phi_N)

pt = gmpy2.powmod(ct, d, N)

pt_hex = hex(pt).replace('0x', '0')

pt_hex = pt_hex[pt_hex.find('00') + 2:]

pt_str = pt_hex.decode('hex')

print pt_str