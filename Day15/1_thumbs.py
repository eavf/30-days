import os
from tkinter.tix import INTEGER
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image


source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')

thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-frame')
thumbnail_per_ms_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-ms')
thumbnail_per_halfs_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-halfs')

os.makedirs(thumbnail_dir, exist_ok=True)
os.makedirs(thumbnail_per_frame_dir, exist_ok=True)
os.makedirs(thumbnail_per_ms_dir, exist_ok=True)
os.makedirs(thumbnail_per_halfs_dir, exist_ok=True)

clip = VideoFileClip(source_path)
print (clip.reader.fps)
print (clip.reader.nframes)
print (clip.duration)

duration = clip.duration
max_duration = int(duration) + 1

for i in range(0, max_duration):
    frame = clip.get_frame(int(i))
    # print(frame)
    new_img_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")
    #print (f"frame at {i} seconds saved at {new_img_filepath}")
    new_img = Image.fromarray(frame)
    new_img.save(new_img_filepath)


for i, frame in enumerate(clip.iter_frames()):
    #print(frame)
    new_img_filepath = os.path.join(thumbnail_per_frame_dir, f"{i}.jpg")
    #print (f"frame at {i} seconds saved at {new_img_filepath}")
    new_img = Image.fromarray(frame)
    new_img.save(new_img_filepath)


fps = clip.reader.fps
nframes = clip.reader.nframes
seconds = nframes/(fps*1.0)

for i, frame in enumerate(clip.iter_frames()):
    if i % fps == 0:
        current_ms = int((i/ fps) * 1000)
        # print(frame)
        new_img_filepath = os.path.join(thumbnail_per_ms_dir, f"{current_ms}.jpg")
        #print (f"frame at {i} seconds saved at {new_img_filepath}")
        new_img = Image.fromarray(frame)
        new_img.save(new_img_filepath)


for i, frame in enumerate(clip.iter_frames()):
    if i % int(fps / 2) == 0:
        current_ms = int((i / fps) * 10000)
        # print(frame)
        new_img_filepath = os.path.join(thumbnail_per_halfs_dir, f"{current_ms}.jpg")
        #print (f"frame at {i} seconds saved at {new_img_filepath}")
        new_img = Image.fromarray(frame)
        new_img.save(new_img_filepath)