# -*- coding: utf-8 -*-
import word_of_the_day
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
from pprint import pprint


def debug(text):
    on = 1
    if on == 1:
        print ("Debug: " + text)
        print ("-"*10)



debug("Getting words")
danish, english = word_of_the_day.get_word()

danish_word = unicode(danish[0], 'utf-8')
danish_sent = unicode(danish[1], 'utf-8')

lastline=0

inky_display = InkyWHAT("red")
inky_display.set_border(inky_display.RED)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

fontsize = 100

fontsizesmall = 100

font1 = ImageFont.truetype("/home/pi/.fonts/Bebas.ttf", fontsize, encoding="utf-8")
font1eng = ImageFont.truetype("/home/pi/.fonts/Bebas.ttf", fontsize, encoding="utf-8")
font2 = ImageFont.truetype("/home/pi/.fonts/Yantramanav-Regular.ttf", fontsizesmall, encoding="utf-8")
font2eng = ImageFont.truetype("/home/pi/.fonts/Yantramanav-Regular.ttf", fontsizesmall, encoding="utf-8")

def get_font_size(font, text):
    path = font.path
    for size in range(100, 10, -1):
        word_width, word_height = font.getsize(text)

        if word_width > inky_display.WIDTH:
            font = ImageFont.truetype(path, size)

        else:
            break

    font.word_width = word_width
    font.word_height = word_height
    

    return font

def get_last_line(line):
    for lines in range(line, inky_display.HEIGHT, 1):
        empty_line = []
        for x in range(0, inky_display.WIDTH, 1):
            pixel = img.getpixel((x, lines))
            empty_line.append(pixel)
        if 0 not in empty_line:
            lastline = lines
            break
        if lines == 300:
            lastline = 292
    return lastline



debug ("Calculating size of Danish header")
font1 = get_font_size(font1, danish_word)

debug ("Calculating size of English header")
font1eng = get_font_size(font1eng, english[0])

debug ("Calculating size of Danish sentence")
font2 = get_font_size(font2, danish_sent)

debug ("Calculating size of English sentence")
font2eng = get_font_size(font2eng, english[1])

debug ("Calculating items on screen")
draw.text((((inky_display.WIDTH/2)-(font1.word_width/2), -8)), danish_word, inky_display.BLACK, font=font1)
draw.text((((inky_display.WIDTH/2)-(font1eng.word_width/2), font1.word_height-8)), english[0], inky_display.RED, font=font1eng)

box_start = (font1.word_height+font1eng.word_height+8)

draw.rectangle((0, box_start, inky_display.WIDTH, inky_display.HEIGHT), inky_display.BLACK)

draw.text((((inky_display.WIDTH/2)-(font2.word_width/2)), font1.word_height+font1eng.word_height+10), danish_sent, inky_display.WHITE, font=font2)
draw.text((((inky_display.WIDTH/2)-(font2eng.word_width/2)), font1.word_height+font1eng.word_height+font2eng.word_height+10), english[1], inky_display.WHITE, font=font2eng)



debug ("Finding last empty line")
box2_start = (font1.word_height+font1eng.word_height+font2eng.word_height+font2eng.word_height)

lastline = get_last_line(box2_start)


# Draw last red box
draw.rectangle((0, lastline+8, inky_display.WIDTH, inky_display.HEIGHT), inky_display.RED)


debug ("Updating screen")


 #flipped = img.rotate(180)
 #inky_display.set_image(flipped)
inky_display.set_image(img)
inky_display.show()