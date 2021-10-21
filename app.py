import cv2 
import time
import dropbox
import random

start_time = time.time()

def take_picture():
    number = random.randint(1,100)
    v1 = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = v1.read()
        image = "img" + str(number) + ".png"
        cv2.imwrite(image,frame)
        start_time = time.time()
        result = False
        return image
    print("Snap Taken")
    v1.release()
    cv2.destroyAllWindows()

def upload_picture(image):
    access_token = "sl.A6zkj8BBmsaMZQsSD50IyVZHdNvuxnPMzC_s-6vdVinNB3mcjZuLvhuJaOscWOImop6s2btyRiBeKMJndtN17bXuD5lkyRG-zc3uVwGUiWmhP1ulzbAvejxYAu9vkufY73AD-RHw6Pck"
    file = image
    file_from = file
    file_to = "/automation/" + (image)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
        while(True):
            if((time.time()-start_time)>=5):
                name = take_picture()
                upload_picture(name)

main()