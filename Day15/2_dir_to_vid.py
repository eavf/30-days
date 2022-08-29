import os
import this
from tkinter.tix import INTEGER
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image


thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-frame')
thumbnail_per_ms_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-ms')
thumbnail_per_halfs_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-halfs')
output_video = os.path.join(SAMPLE_OUTPUTS, 'thumbs.mp4')

this_dir = os.listdir(thumbnail_dir)
filepaths = [os.path.join(thumbnail_dir, fname) for fname in this_dir if fname.endswith("jpg")]

# Toto je prepis do dlhej formy
#filepath = []
#for fname in this_dir:
#    if fname.endswith("jpg"):
#        path = os.path.join(thumbnail_dir, fname)
#        filepaths.append(path)
    
#print(filepaths)
#clip = ImageSequenceClip(filepaths, fps = 1)
#clip.write_videofile(output_video)
# Tut to bolo nie v poradí, takže to zoradíme

directory = {}

for root, dirs, files in os.walk(thumbnail_per_frame_dir):
    for fname in files:
        filepath = os.path.join(root, fname)
        try:
            key = float(fname.replace(".jpg", ""))
        except:
            key = None
        if key != None:
            directory[key] = filepath


new_paths = []
for k in sorted(directory.keys()):
    filepath = directory[k]
    new_paths.append(filepath)

#pôvodný spôsob
#clip = ImageSequenceClip(new_paths, fps = 10)
#clip.write_videofile(output_video)

#iný spôsob - každý obrázok je jeden frame

my_clips = []
for path in list(new_paths):
    frame = ImageClip(path)
    #print(dir(frame))
    my_clips.append(frame.img)

clip = ImageSequenceClip(my_clips, fps = 30)
#clip.write_videofile(output_video)