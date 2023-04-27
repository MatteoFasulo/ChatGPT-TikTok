import platform
import asyncio
import random

import edge_tts
from edge_tts import VoicesManager

#######################
#        STATIC       #
#######################

jsonData = {"series": "Epic stories", 
            "part": 1,
            "outro": "Follow us for more",
            "random": False,
            "path": "C:\\Users\\Mario\\Desktop\\Tiktok\\ChatGPT-TikTok\\Audio-Output",
            "texts": ["Example 1", "Example 2", "Example 3"]}


#######################
#         CODE        #
#######################

async def main():
    series = jsonData['series']
    part = jsonData['part']
    outro = jsonData['outro']
    path = jsonData['path']
    random_voice = jsonData['random']

    for text in jsonData['texts']:
        final_text, outfile = await create_full_text(path, series, part, text, outro)
        await tts(final_text, outfile=outfile, random_voice=random_voice)
        part += 1

    return True

async def create_full_text(path: str, series: str, part: int, text: str, outro: str) -> str:
    final_text = f"{series} Part {part}.\n{text}\n{outro}"
    outfile = f"{path}\\{series}\\{series.replace(' ', '')}_{part}.mp3"
    return final_text, outfile


async def tts(final_text: str, voice: str = "en-US-ChristopherNeural", random_voice: bool = False, stdout: bool = False, outfile: str = "tts.mp3"):
    voices = await VoicesManager.create()
    if random_voice:
        voices = voices.find(Gender="Male", Locale="en-US")
        voice = random.choice(voices)["Name"]
    communicate = edge_tts.Communicate(final_text, voice)
    if not stdout:
        await communicate.save(outfile)
    return True


if __name__ == "__main__":
    if platform.system()=='Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main()) # Crea il loop e lo chiude in automatico
    print("Done!")