import subprocess

#######################
series = "????"
part = 1
outro = "Follow us for more"
outfile = f"text_{part}.mp3"
path = f"C:\\Users\\Mario\\Desktop\\Tiktok\\ChatGPT-TikTok\\audio{outfile}"

#######################

with open('script.txt', 'r') as file:
    text = file.read().rstrip().replace('"',"'")

final_text = f"{series}. Part {part}.\n{text}\n{outro}"

with subprocess.Popen(f'edge-tts --voice en-US-ChristopherNeural --text "{final_text}" --write-media "{path}"', stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as process:
    pass
print("Done!")