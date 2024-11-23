import time
import multiprocessing

def read_info(name):
    """
    Создает локальный список all_data, открывает файл name для чтения, считывает информацию построчно
    (readline), пока считанная строка не окажется пустой. Во время считывания добавляет каждую строку в
    список all_data.
    """
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line.strip())
            line = file.readline()

filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f"Время выполнения линейного вызова: {end_time - start_time} секунд")

    # Многопроцессный
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Время выполнения многопроцессного вызова: {end_time - start_time} секунд")