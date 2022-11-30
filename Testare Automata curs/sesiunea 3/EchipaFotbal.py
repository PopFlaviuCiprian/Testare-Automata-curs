jucatori_in_teren = ['Andrei','Alin','Alex','Calin','Daniel']
jucatori_intrat = input('Jucatorul nou intrat este: ')
jucator_iesit = input('Jucatorul iesit este: ')
SCHIMBARI_MAX = 3
schimbari_efectuate = int(input('Schimbari efectuate: '))
if jucator_iesit in jucatori_in_teren and SCHIMBARI_MAX-schimbari_efectuate>0:
    if jucatori_intrat in jucatori_in_teren:
        print('Nu putem face schimbarea, jucatorul este pe teren')
    else:
        print(f'Se poate efectua schimbarea a iesit {jucator_iesit}, '
              f'a intrat {jucatori_intrat} mai sunt {SCHIMBARI_MAX-schimbari_efectuate} schimbari')
elif SCHIMBARI_MAX-schimbari_efectuate<=0:
    print('Nu mai ai schimbari ramase !!!')
else:
    print(f'Nu se poate efectua schimbarea deoarece {jucator_iesit} nu mai este in teren')
jucatori_in_teren.remove(jucator_iesit)
jucatori_in_teren.append(jucatori_intrat)
print(jucatori_in_teren)