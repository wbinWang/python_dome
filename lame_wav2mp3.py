#采用lame命令，将wav文件转为MP3文件

import os
import subprocess

def traversePath(path):
    for dict , subDict , files in os.walk(path):
        for file in files:
            if str(file).endswith(".wav"):
                inputFile = os.path.join(dict , file)
                print(inputFile)
                #转换
                # wav2mp3(inputFile)
                #删除旧的wav文件
                os.remove(inputFile)

# wav2mp3
def wav2mp3(inputFile):
    name = str(inputFile).split('.')[0]
    cmd = ['lame','-h',inputFile,'%s.mp3' % name]
    subprocess.call(cmd)  

if __name__ == "__main__":
    traversePath("/Users/WB/Desktop/上打Demo/originSourceMP3")