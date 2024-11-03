import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def roll_dice(num_rolls):
    sums = {i: 0 for i in range(2, 13)}  
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sums[total] += 1  

    probabilities = {k: v / num_rolls for k, v in sums.items()} 
    return sums, probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    prob_values = list(probabilities.values())

    plt.bar(sums, prob_values, color='skyblue')
    plt.xlabel('Суми')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.xticks(sums)
    plt.grid(axis='y')
    plt.show()


num_rolls = 100000 
sums, probabilities = roll_dice(num_rolls)
plot_probabilities(probabilities)

results_df = pd.DataFrame(list(probabilities.items()), columns=['Сума', 'Ймовірність'])
print(results_df)

results_df.to_csv('monte_carlo_dice_probabilities.csv', index=False)
