
import numpy as np

def random_predict(number: int = 1) -> int:
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
    #Run benchmarking to score effectiveness of all algorithms


def game_core_v3(number):
    # устанавливаем предполагаемое  число в половину от диапазона
    predict = 50
    # устанавливаем счетчик
    count = 1
    # Пишем условие
    # если предполагаемое число меньше загаданного проверки делим пополам предполагаемое число и прибавляем к предыдущему предполагаемому числу , прибавляем попытку

    if predict < number:
        predict += 25
        count += 1
    # если предполагаемое число меньше загаданного проверки делим пополам предполагаемое число и прибавляем к предыдущему предполагаемому числу , прибавляем попытку    
        if predict < number:
            predict += 12
            count += 1
    # если предполагаемое число меньше загаданного проверки делим пополам предполагаемое число и прибавляем к предыдущему предполагаемому числу , прибавляем попытку        
            if predict < number:
                predict += 7
            else:
                predict -= 6
    # если предполагаемое число больше загаданного проверки делим пополам предполагаемое число и вычитаем от предыдущего предполагаемого числа , прибавляем попытку            
        elif predict > number:
            predict -= 12
            count += 1
            if predict < number:
                predict += 7
            else:
                predict -= 6
    # если предполагаемое число больше загаданного проверки делим пополам предполагаемое число и вычитаем от предыдущего предполагаемого числа , прибавляем попытку                       
    elif predict > number:
        predict -= 25
        count += 1
    # если предполагаемое число меньше загаданного проверки делим пополам предполагаемое число и прибавляем к предыдущему предполагаемому числу , прибавляем попытку    
        if predict < number:
            predict += 12
            count += 1
    # если предполагаемое число меньше загаданного проверки делим пополам предполагаемое число и прибавляем к предыдущему предполагаемому числу , прибавляем попытку        
            if predict < number:
                predict += 7
            else:
                predict -= 6
    # если предполагаемое число больше загаданного проверки делим пополам предполагаемое число и вычитаем от предыдущего предполагаемого числа , прибавляем попытку            
        elif predict > number:
            predict -= 12
            count += 1
            if predict < number:
                predict += 7
            else:
                predict -= 6
    # окончательно угадываем число            
    while predict < number:
        predict += 1
        count += 1
    while predict > number:
        predict -= number
        count += 1
    return count
 
print(max(map(game_core_v3, range(1, 101))))


print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)