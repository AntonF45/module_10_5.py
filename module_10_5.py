
import time
from datetime import timedelta
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start = time.time()
    for filename in filenames:
        read_info(filename)
    end = time.time() - start
    formatted_time = str(timedelta(seconds=end))
    print(f'{formatted_time} (линейный)')

    # Многопроцессный
    start = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end = time.time() - start
    formatted_time = str(timedelta(seconds=end))
    print(f'{formatted_time} (многопроцессный)')
