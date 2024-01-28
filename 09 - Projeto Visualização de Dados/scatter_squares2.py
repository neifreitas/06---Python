from matplotlib import pyplot as plt

# Define um único ponto na área do gráfico
# plt.scatter(2, 4, s=100)

# Define os valores dos eixos 'x' e 'y'
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
#plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)

# Usando um colormap
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.magma, edgecolors='none', s=40)

# Define o título do gráfico e nomeia os eixos
plt.title("Square Numbers", fontsize=30, font='arial')
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis="both", which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])

plt.show()

