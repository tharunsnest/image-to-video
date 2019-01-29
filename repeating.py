#!/usr/bin/env python

#time1,time2 entry box
#loop entry box
#picture1,picture2 tkFileDialog.askopenfilename()
#framesDestination tkFileDialog.askdirectory()
#videoDestination tkFileDialog.askdirectory()


import subprocess
import shutil
import Tkinter, tkFileDialog
t = [0.0,0.0, 0.0,0.0,0.0,0.0]
loop = 1
number_of_images = 2
root = Tkinter.Tk()
root.title("Image to Video")
picture = ['i','i','i','i','i']
# picture = ['C:/Users/Venkateswarlu/PycharmProjects/repeating/Emoticons/happy (1).png','C:/Users/Venkateswarlu/PycharmProjects/repeating/Emoticons/happy (1).png','C:/Users/Venkateswarlu/PycharmProjects/repeating/Emoticons/happy (1).png','C:/Users/Venkateswarlu/PycharmProjects/repeating/Emoticons/happy (1).png','C:/Users/Venkateswarlu/PycharmProjects/repeating/Emoticons/happy (1).png']
filler = ""
frameDestination = ""
videoDestination = ""


# def F_time1():
#     global t
#     t[1] = float(E_time1.get())
#     print t

# def F_time2():
#     global t
#     t[2] = float(E_time2.get())
#     print t

def F_loop():
    global loop,t,number_of_images
    t[1] = float(E_time1.get())
    t[2] = float(E_time2.get())
    t[3] = float(E_time3.get())
    t[4] = float(E_time4.get())
    t[5] = float(E_time5.get())
    number_of_images = int(E_num_images.get())
    loop = int(E_loop.get())

def F_pic1():
    global picture
    picture[0] = tkFileDialog.askopenfilename()
    # print picture

def F_pic2():
    global picture
    picture[1] = tkFileDialog.askopenfilename()

def F_pic3():
    global picture
    picture[2] = tkFileDialog.askopenfilename()

def F_pic4():
    global picture
    picture[3] = tkFileDialog.askopenfilename()

def F_pic5():
    global picture
    picture[4] = tkFileDialog.askopenfilename()
# print picture

def F_filler():
    global filler
    filler = tkFileDialog.askopenfilename()

def F_frame():
    global frameDestination
    frameDestination = tkFileDialog.askdirectory()
    # print frameDestination

def F_video():
    global videoDestination
    videoDestination = tkFileDialog.askdirectory()
    # print videoDestination
def F_main():
    # print("success")
    global videoDestination, frameDestination, loop, t, picture, filler, number_of_images
    # n = [t[i] * 60 for i in range(len(t))]
    n = t

    fill = 0
    for i in range(loop):
        # for j in range(len(picture)):
        for j in range(number_of_images):
            for j1 in range(int(sum(n[0:j + 1])), int(sum(n[0:j + 2]))):
                # print frameDestination
                shutil.copy2(picture[j], frameDestination+'/a{:05d}.png'.format(j1 + int(sum(n)) * i + 60 * fill))
            for j2 in range (j1  + 60 * fill + 1, j1 + 60 * fill + 60 + 1):
                shutil.copy2(filler, frameDestination + '/a{:05d}.png'.format(j2 + int(sum(n)) * i))
            fill = fill + 1
    subprocess.call(
            ['ffmpeg', '-y', '-r', '60', '-f', 'image2', '-s', '1920x1080', '-i', frameDestination + '/a%05d.png',
             '-vcodec', 'libx264', '-crf', '25', '-pix_fmt', 'yuv420p', videoDestination + '/video1.mp4'], shell=True)


L_number_images = Tkinter.Label(root, text="Number of images")
E_num_images = Tkinter.Entry(root)

L_time1 = Tkinter.Label(root, text="Time1")
E_time1 = Tkinter.Entry(root)
#B_time1 = Tkinter.Button(root, text="enter", command=F_time1)


L_time2 = Tkinter.Label(root, text="Time2")
E_time2 = Tkinter.Entry(root)
#B_time2 = Tkinter.Button(root, text="enter", command=F_time2)

L_time3 = Tkinter.Label(root, text="Time3")
E_time3 = Tkinter.Entry(root)

L_time4 = Tkinter.Label(root, text="Time4")
E_time4 = Tkinter.Entry(root)

L_time5 = Tkinter.Label(root, text="Time5")
E_time5 = Tkinter.Entry(root)


L_loop = Tkinter.Label(root, text="loop")
E_loop = Tkinter.Entry(root)
B_loop = Tkinter.Button(root, text="enter", command=F_loop)

B_filler = Tkinter.Button(root, text= "select filler image", command= F_filler)
B_pic1 = Tkinter.Button(root, text= "select picture 1", command= F_pic1)
B_pic2 = Tkinter.Button(root, text= "select picture 2", command= F_pic2)
B_pic3 = Tkinter.Button(root, text= "select picture 3", command= F_pic3)
B_pic4 = Tkinter.Button(root, text= "select picture 4", command= F_pic4)
B_pic5 = Tkinter.Button(root, text= "select picture 5", command= F_pic5)

B_frame = Tkinter.Button(root, text= "empty directory destination", command=F_frame)

B_video = Tkinter.Button(root, text= "video destination", command=F_video)

B_main = Tkinter.Button(root, text= "generate" , command= F_main)
L_number_images.grid(row = 0,column = 0)
E_num_images.grid(row = 0, column = 1)
L_time1.grid(row= 1,column = 0)
E_time1.grid(row= 1,column = 1)
#B_time1.grid(row= 0,column = 2)

L_time2.grid(row= 2,column = 0)
E_time2.grid(row= 2,column = 1)
#B_time2.grid(row= 1,column = 2)
L_time3.grid(row= 3,column = 0)
E_time3.grid(row= 3,column = 1)
L_time4.grid(row= 4,column = 0)
E_time4.grid(row= 4,column = 1)
L_time5.grid(row= 5,column = 0)
E_time5.grid(row= 5,column = 1)
L_loop.grid(row= 6,column = 0)
E_loop.grid(row= 6,column = 1)
B_loop.grid(row= 6,column = 2)

B_filler.grid(row=7)
B_pic1.grid(row=8)
B_pic2.grid(row=9)
B_pic3.grid(row=10)
B_pic4.grid(row=11)
B_pic5.grid(row=12)

B_frame.grid(row=13)
B_video.grid(row=14)
B_main.grid(row=15)

root.mainloop()
