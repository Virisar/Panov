from time import sleep, time
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Время выполнения функций
start_time = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time()
print(f"Работа функций {end_time - start_time:.6f} секунд")

# Время выполнения потоков
start_time = time()
threads = []
threads.append(Thread(target=write_words, args=(10, 'example5.txt')))
threads.append(Thread(target=write_words, args=(30, 'example6.txt')))
threads.append(Thread(target=write_words, args=(200, 'example7.txt')))
threads.append(Thread(target=write_words, args=(100, 'example8.txt')))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time = time()
print(f"Работа потоков {end_time - start_time:.6f} секунд")
