from matplotlib import colors
import matplotlib.pyplot as plt
from random import randrange

x1 = [randrange(4,16,3) for _ in range(7)]
y1 = [randrange(2,20,2) for _ in range(7)]

x2 = [randrange(4,20,2) for _ in range(7)]
y2 = [randrange(3,20,3) for _ in range(7)]

# plt.plot(x1, y1, label='Serie 1', color='red', linewidth=3)
# plt.plot(x2, y2, label='Serie 2', color='blue', linewidth=2)
# plt.title('Mi primer grafica con PLT')
# plt.xlabel('Axis X')
# plt.ylabel('Axis Y')
# plt.legend()
# plt.grid()
# plt.show()

# plt.bar(x1,y1, color='yellow', linewidth=2, label='Barra 1')
# plt.bar(x2,y2, color='pink', linewidth=2, label='Barra 2')
# plt.title('Grafico de barras')
# plt.xlabel('Axis X')
# plt.ylabel('Axis Y')
# plt.legend()
# plt.grid()
# plt.show()

Datos = [20,22,21,20,23,25,28,40,22,23,22,15,16,18,18,19,21,22,24,4,12,17,17,22,30,]
Rangobin=[0,10,20,20,30,40]
# plt.hist(Datos, Rangobin, histtype='bar', rwidth=0.8, color='lightblue')
# plt.title('Histograma')
# plt.xlabel('Axis X')
# plt.ylabel('Axis Y')
# plt.show()

# plt.scatter(x1, y1, color='black', label='Puntos 1')
# plt.scatter(x2, y2, color='red', label='Puntos 2',)
# plt.title('Scatter')
# plt.ylabel('Axis Y')
# plt.xlabel('Axis X')
# plt.legend()
# plt.grid()
# plt.show()

# plt.pie(x1,
#         startangle=90,
#         shadow=True,
#         explode=(0,0,0.1,0,0,0.2,0),
#         labels=['e1','e2','e3','e4','e5','e6','e7'],
#         autopct='%1.2f%%')
# plt.title('Grafico de Torta')
# plt.show()

plt.figure(figsize=(20,10))

plt.subplot2grid((2,2),(0,0))
plt.plot(x1, y1, label='Serie 1', color='red', linewidth=3)
plt.plot(x2, y2, label='Serie 2', color='blue', linewidth=2)

plt.subplot2grid((2,2),(0,1))
plt.bar(x1,y1, color='yellow', linewidth=2, label='Barra 1')
plt.bar(x2,y2, color='pink', linewidth=2, label='Barra 2')

plt.subplot2grid((2,2),(1,0))
plt.scatter(x1, y1, color='red', label='Puntos 1')
plt.scatter(x2, y2, color='blue', label='Puntos 2',)

plt.subplot2grid((2,2),(1,1))
plt.pie(x1,
        startangle=90,
        shadow=True,
        explode=(0,0,0.1,0,0,0.2,0),
        labels=['e1','e2','e3','e4','e5','e6','e7'],
        autopct='%1.2f%%')

plt.show()

