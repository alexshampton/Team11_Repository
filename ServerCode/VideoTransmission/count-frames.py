import os

input_vid = "output.mp4"
output_vid = "test.mp4"

cmd = (
    f"""ffmpeg -i """
    + input_vid
    + """ -vf "drawtext=fontfile=Arial.ttf: text='%{frame_num}': start_number=1: x=(w-tw)/2: y=h-(2*lh): fontcolor=black: fontsize=20: box=1: boxcolor=white: boxborderw=5" -c:a copy """
    + output_vid
)

print(cmd)

os.system(cmd)

# ffmpeg -i incrementing.mp4 -vf "drawtext=fontfile=Arial.ttf: text='%{frame_num}': start_number=1: x=(w-tw)/2: y=h-(2*lh): fontcolor=black: fontsize=20: box=1: boxcolor=white: boxborderw=5" -c:a copy output.mp4
