import picamera
import time
from os import system
n=1
camera = picamera.PiCamera()
camera.rotation=180
nombre = raw_input ("Buen dia, cual es tu nombre?\n")
modo = raw_input ("Queres sacar una foto o filmar un video?\n")
nombre_archivo=raw_input ("Con que nombre queres guardar el archivo?\n")
if modo == "foto":
    cantidad=int(raw_input("Cuantas fotos?\n"))
    time_lapse=int(raw_input("Con que time lapse?\n"))
    print "none, negative, solarize, sketch, denoise, emboss, oilpaint, hatch, gpen, pastel, watercolor, film, blur, saturation, colorswap, washedout, posterise, colorpoint, colorbalance, cartoon, deinterlace1, or deinterlace2"
    efecto=raw_input("Con que efecto?\n")
    camera.image_effect = efecto
    camera.start_preview()
    for x in range(0,cantidad):
        camera.annotate_text=nombre + "'s picture"
        camera.capture('/home/pi/share/Pythoncamera/Pictures/' + nombre_archivo + '%s.jpg'%x) 
        time.sleep(time_lapse)
        n=n+1
    camera.stop_preview()
    gif=raw_input("Queres transformar todas tus recientes fotos en un gif?\n")
    if gif == "si":
        intervalo_gif=int(raw_input("Con cuanto delay (ms) lo queres?\n"))
        loop_gif=int(raw_input("Cuantos loops queres que haga? o infinito(0)?\n"))
        nombre_gif=raw_input("Con que nombre queres guardar el gif?\n")
        system ('convert -delay ' + str(intervalo_gif) + ' -loop ' + str(loop_gif) + ' ' + str(nombre_archivo) + '*.jpg ' + str(nombre_gif) + '.gif')
if modo == "video":
    tiempo_video=int(raw_input("De cuantos segundos?\n"))
    print "none, negative, solarize, sketch, denoise, emboss, oilpaint, hatch, gpen, pastel, watercolor, film, blur, saturation, colorswap, washedout, posterise, colorpoint, colorbalance, cartoon, deinterlace1, or deinterlace2"
    efecto=raw_input("Con que efecto?\n")
    camera.image_effect = efecto
    camera.annotate_text=nombre + "'s video"
    camera.start_preview()
    camera.start_recording('/home/pi/share/Pythoncamera/Videos/' + nombre_archivo + '.h264')
    time.sleep(tiempo_video)
    camera.stop_recording()
    camera.stop_preview()
    system ('MP4Box -add ' + '../Videos/' + nombre_archivo + '.h264 ' + '../Videos/' + nombre_archivo + '.mp4')
    
    
    



