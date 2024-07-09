import random


def get_numbers_ticket(min, max, quantity): 

    if min < 1 or max > 1000 or not(min <= quantity <= max):
        return []
    
    unique_numbers = random.sample(range(min, max + 1), quantity)

    unique_numbers.sort()

    return unique_numbers

    




        
        
