import datetime
import multiprocessing as mp
import image
from PIL import Image
from queue import Empty

def resize_image(image_paths, pipe: mp.Pipe, stop_event):
    for image_path in image_paths:
        image = Image.open(image_path)
        image.resize((800, 600))
        image.save(image_path)
        pipe.send(image_path)
    stop_event.set()

def change_color(pipe: mp.Pipe, stop_event):
    while not stop_event.is_set():
        image_path = pipe.recv(timeout=5)
        image = Image.open(image_path)
        image = image.convert('L')
        image.save(image_path)

if __name__ == '__main__':
    data = []
    conn1, conn2 = mp.Pipe()
    stop_event = mp.Event()
    for Image in range(1, 10):
        data.append(f'./images/img_{image}.jpg')

    resize_process = mp.Process(target=resize_image, args=(data, conn1))
    change_process = mp.Process(target=change_color, args=(conn2,))
    start = datetime.datetime.now()
    resize_process.start()
    change_process.start()

    resize_process.join()
    change_process.join()
    end = datetime.datetime.now()
    print(end - start)