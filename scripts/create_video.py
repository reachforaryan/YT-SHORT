import re
from moviepy.editor import *
import os

def parse_dialogue(dialogue_path):
    with open(dialogue_path, 'r') as f:
        content = f.read()

    dialogue_lines = []
    current_emotion = "happy"  # Default emotion
    
    # Split the content by lines, but keep the emotion tags
    lines = re.split(r'(\[\w+\])', content)
    
    emotion_map = {
        "[Smug]": "smug",
        "[Angry]": "angry",
        "[Sarcastic]": "smug", # No sarcastic sprite, using smug
        "[Happy]": "happy",
        "[Sad]": "sad"
    }

    for line in lines:
        if line in emotion_map:
            current_emotion = emotion_map[line]
        elif line.strip():
            dialogue_lines.append((current_emotion, line.strip()))
            
    return dialogue_lines

def create_video(dialogue_path, sprite_dir, output_path):
    dialogue = parse_dialogue(dialogue_path)
    
    clips = []
    for emotion, text in dialogue:
        sprite_path = os.path.join(sprite_dir, f"{emotion}.png")
        
        # Create image clip
        img_clip = ImageClip(sprite_path).set_duration(3).set_pos(('center', 'center'))
        
        # Create text clip
        text_clip = TextClip(text, fontsize=40, color='white', bg_color='black', size=(600, 200)).set_duration(3).set_pos(('center', 'bottom'))
        
        # Composite clips
        video_clip = CompositeVideoClip([img_clip, text_clip], size=(1080, 1920))
        clips.append(video_clip)
        
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_path, fps=24)

if __name__ == '__main__':
    dialogue_file = "../dialogues/Beyond the List: Unpacking the Invisible Architectures That Organize the World's Information.txt"
    sprite_folder = "../sprite"
    output_video = "../video/output.mp4"
    
    create_video(dialogue_file, sprite_folder, output_video)
