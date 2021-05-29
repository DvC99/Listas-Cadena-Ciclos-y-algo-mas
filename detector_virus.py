def dectarVirus(secVirus, secSangre):
  positivo = []
  negativo = []
  temSecSangre = []
  for p in secSangre:
    for i in range(len(p)):
      temSecSangre.append(p[i])
    ind = []
    for i in range(len(temSecSangre)):
      ind.append(secVirus.index(temSecSangre[i]))
    count = 1
    for i in range(0,len(ind)-1):
      if( ind[i] < ind[i+1]):
        count = count +1
    if(count == len(ind)):
      positivo.append(p)
    else:
      negativo.append(p)
  return positivo, negativo