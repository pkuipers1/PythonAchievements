from pydub import AudioSegment
from pydub.playback import play


isRunning = True

getal = 1000

while (isRunning):
    getal -= 1
    print(getal)
    if (getal < 1):
        geluidje = AudioSegment.from_file(file = "Beep.mp3", format = "mp3")
        play(geluidje)
        isRunning = False
