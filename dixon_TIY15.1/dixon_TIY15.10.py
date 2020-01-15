import matplotlib.pyplot as plt
from random_walks import RandomWalk
from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die
from random import choice

while True:

    die_1 = Die()
    die_2 = Die()

    results = []
    for roll_num in range(50_000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    x_values = list(range(2, max_result+1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Result', 'dtick': 1}
    y_axis_config = {'title': 'Frequency of Result'}
    my_layout = Layout(title='Results of rolling Two D8s 1000 Times', xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')

    print(frequencies)

    #The randokm walk

    x_distance = choice([die_1.num_sides])
    y_distance = choice([die_2.num_sides])

    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

