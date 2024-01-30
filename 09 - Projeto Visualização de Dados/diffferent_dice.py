from die import Die
import pygal

# Cria dois dados D6
die_1 = Die()
die_2 = Die()

# Faz alguns lançamentos e armazena os resultados em um lista
results = []
for roll in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
#print(results)

# Analisa os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)

# Visualiza os resultados
hist = pygal.Bar()

hist._title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual2.svg')
