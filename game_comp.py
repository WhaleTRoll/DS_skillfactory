"""Угадай число для компьютера"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) #предпологаемое число
        if number == predict_number:
            break # выход из цикла если угадали
        
    return(count)

print(f'Кол-во попыток: {random_predict(10)}')


