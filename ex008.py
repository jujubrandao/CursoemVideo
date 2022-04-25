d = float(input('Uma distância em metros: '))

km = d / 1000
hm = d / 100
dam = d / 10
dm = d / 0.1
cm = d / 0.01
mm = d / 0.001

print('A medida de {}m corresponde a {:.3f}km\n {:.3f}hm\n {:.3f}dam\n {:.3f}dm\n {:.3f}cm\n {:.3f}\n'.format(d,km,hm,dam,dm,cm,mm))
