from email.mime import image
import os
from tkinter import Frame
from turtle import shape, width
import cv2


path = "D:/Proyectos de la escuela/Quinta etapa/Clase 105/ProyectoClase105/Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.png', '.jpg']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

readImage = cv2.imread(images[0])
height, width, channels = readImage.shape
size = (width, height)
print(size)
      
   
writeVideo = cv2.VideoWriter("Project.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 1, size)

    
for indice in range(0, count, 1):
    frame = cv2.imread(images[indice])
    writeVideo.write(frame)
writeVideo.release()
print("Listo")