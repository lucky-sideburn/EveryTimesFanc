import glob
import random
from PIL import Image as PILImage
from PIL import ImageEnhance as PILImageEnhance
from PIL import ImageDraw as PILImageDraw
from PIL import ImageFont as PILImageFont
import os
import time
import hashlib

def hex_code_colors():
    a = hex(random.randrange(0,256))
    b = hex(random.randrange(0,256))
    c = hex(random.randrange(0,256))
    a = a[2:]
    b = b[2:]
    c = c[2:]
    if len(a)<2:
        a = "0" + a
    if len(b)<2:
        b = "0" + b
    if len(c)<2:
        c = "0" + c
    z = a + b + c
    return "#" + z.upper()

 
def create_image(text):
    file_name = text.replace(" ", "_")#.replace("`", "").replace("'", "")
    #color = hex_code_colors()
    color = "blue"
    fill_color = 'white'
    img = PILImage.new('RGB', (1024, 800), color = color)
    d = PILImageDraw.Draw(img)
    font = PILImageFont.truetype("/usr/local/lib/python3.7/site-packages/werkzeug/debug/shared/ubuntu.ttf", 45)
    d.text((100,100), text, fill=fill_color, font=font)
    img.save('images/' + file_name + '.png')

def create_sound(name):
    hash_object = hashlib.md5(name.encode())
    md5_hash = hash_object.hexdigest()
    file_name = name.replace(" ", "_")#.replace("`", "").replace("'", "")
    text = ""
    i = 0
    while i < 5:
        i = i + 1
        text = f"{text} {name}... "
    
    os.system(f"say -v Luca \"{text}\" -o sounds/{file_name}.aiff; lame -m m sounds/{file_name}.aiff sounds/{file_name}.mp3")

def make_video(name):
    file_name = name.replace(" ", "_")#.replace("`", "").replace("'", "")
    os.system(f"ffmpeg -vb 20M -loop 1 -i images/{file_name}.png -i sounds/{file_name}.mp3 -shortest -acodec copy -vcodec mjpeg videos/{file_name}.mkv")

fuck = ", andate a fanculo"

os.system("ls videos || mkdir videos")
os.system("ls images || mkdir images")
os.system("ls sounds || mkdir sounds")

for file in glob.glob("./times/*.times"):
    f = open(file, "r")

    if file == "./times/mesi.times":
        for line in f.readlines():
            line = line.strip("\n")
            final_string = f"{line}{fuck}"
            print(final_string)
            create_image(final_string)
            create_sound(final_string)

        mesi_file = open("./times/mesi.times", "r")
        for mese in mesi_file.readlines():
            tutti_giorni_anno = open("./times/giorni.additional", "r")
            for giorno_mese in tutti_giorni_anno.readlines():
                giorno_mese = giorno_mese.strip("\n")
                mese = mese.strip("\n")
                final_string = f"è {giorno_mese}{mese.replace('è','')}{fuck}"
                print(final_string)
                create_image(final_string)
                create_sound(final_string)
    
    if file == "./times/ore.times":
        for line in f.readlines():
            line = line.strip("\n")
            final_string = f"{line}{fuck}"
            print(final_string)
            create_image(final_string)
            create_sound(final_string)
            make_video(final_string)

        ore_file = open("./times/ore.times", "r")

        for ore in ore_file.readlines():
            tutteleore_file = open("./times/tutteleore.additional", "r")
            for ora in tutteleore_file.readlines():
                ora = ora.strip("\n")
                ore = ore.strip("\n")
                final_string = f"{ore} {ora}{fuck}"
                print(final_string)
                create_image(final_string)
                create_sound(final_string)
                make_video(final_string)
    else:
        for line in f.readlines():
            line = line.strip("\n")
            final_string = f"{line}{fuck}"
            print(final_string)
            create_image(final_string)
            create_sound(final_string)
            make_video(final_string)
