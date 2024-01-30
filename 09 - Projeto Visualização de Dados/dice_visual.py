from dice import Dice
import pygal

# Cria um D6
dice = Dice()

# Faz alguns lançamentos e armazena os resultados em um lista
results = []
for roll in range(1000):
    result = dice.roll()
    results.append(result)
    
#print(results)

# Analisa os resultados
frequencies = []
for value in range(1, dice.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)

# Visualiza os resultados
hist = pygal.Bar()

hist._title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('dice_visual.svg')
