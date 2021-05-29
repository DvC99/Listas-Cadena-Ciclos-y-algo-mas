import detector_virus as dt


#coronavirus
secVirus = input("Digite la secuencia del virus que se decea buscar entre las personas:\n")
#ravus,ra,vus,aus,ar,vara,suvar
secSangre = input("Digite la secuencia de la sangre de las personas separadas por , :\n").split(",")
postivos, negativos = dt.dectarVirus(secVirus,secSangre)

print("\nLos positivos son:")
for i in range(len(postivos)):
  print(str(postivos[i]))

print("\nLos negativos son:")
for i in range(len(negativos)):
  print(str(negativos[i])) 
