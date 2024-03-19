from random import randint
import numpy as np


def roll_dice(rolls: int=1, sides: int=6):
    rolls = [randint(1, sides) for _ in range(rolls)]
    return rolls

def get_histogram(rolls: list):
    histogram = [rolls.count(roll) for roll in range(1, max(rolls)+1)]
    return histogram
    
def calculate_distribution(rolls: list):
    distribution = {roll: rolls.count(roll)/len(rolls) for roll in set(rolls)}
    return distribution

def print_distribution(distribution: dict):
    for roll, frequency in distribution.items():
        print(f'{roll}: {frequency:.2%}')


def animate(frame_number, bar_container):
    # simulate new data coming in
    rolls = roll_dice(rolls=1000)
    histogram = get_histogram(rolls)
    for bar, h in zip(bar_container, histogram):
        bar.set_height(h)

    return bar_container