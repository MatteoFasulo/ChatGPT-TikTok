import subprocess
import os

jsonData = {"series": "Epic stories", 
            "part": 2,
            "outro": "Follow us for more",
            "outfile": "EpicStories",
            "path": "C:\\Users\\Mario\\Desktop\\Tiktok\\ChatGPT-TikTok\\Audio-Output",
            "texts": ["Oliver had always been fascinated by the ocean and dreamed of exploring its depths. He spent years studying marine biology and scuba diving, and finally, he had the opportunity to join a research expedition to the Mariana Trench. As he descended into the depths of the ocean, he was in awe of the strange and beautiful creatures that surrounded him. Suddenly, he felt a sharp pain in his arm and realized that he had been stung by a jellyfish. He quickly radioed to the surface for help, but the pain was unbearable, and he started to lose consciousness. When he woke up, he was in a hospital bed, and the doctors told him that he had suffered a severe allergic reaction to the jellyfish venom.", 
                      "Jennifer had just moved into a new apartment, but she soon began to notice strange things happening. She heard footsteps in the hallway at night, and objects moved on their own. One evening, as she was getting ready for bed, she heard whispering voices coming from her closet. She slowly opened the door, and to her horror, she saw a shadowy figure huddled in the corner. She tried to scream, but no sound came out. The figure slowly turned its head towards her, revealing glowing red eyes that stared directly into her soul. Jennifer never spoke of the experience again, but every night she heard the whispers in her dreams, reminding her of the terror that lurked in her closet.", 
                      "Lila had always been an optimistic person, and her positivity had paid off in more ways than one. She had won the lottery not once, but twice, and had also narrowly escaped a major car accident without a scratch. One day, while hiking alone in the mountains, Lila slipped and fell off a steep ledge. She tumbled down the rocky slope, sure that she would die. But miraculously, a tree broke her fall and she landed safely on a soft bed of leaves. After catching her breath, Lila realized that she had only suffered a few bruises and scrapes. She felt incredibly lucky to have survived such a dangerous fall, and knew that she would never take her life for granted again.", 
                      "John had always been a gambler at heart, and he loved nothing more than testing his luck at the casinos in Las Vegas. One night, John hit the jackpot on a slot machine, winning over a million dollars. Feeling invincible, John decided to celebrate his good fortune by taking a helicopter ride over the city. But as the helicopter rose higher and higher, the engine suddenly sputtered and died. The helicopter began to spin out of control, hurtling towards the ground. Just when it seemed like all was lost, the helicopter miraculously landed in a shallow pool of water. John emerged unscathed, and was hailed as the luckiest man in Vegas.",
                      "Samantha had always been intrigued by the abandoned house at the end of her street. It had been empty for years, and rumors swirled about why the family who lived there had suddenly vanished. One night, Samantha decided to investigate. She slipped inside and began to explore, but the house was shrouded in darkness. Suddenly, she heard creaking footsteps coming from upstairs. She froze, listening intently as the footsteps grew closer. The sound stopped at the top of the stairs, and she heard a faint whisper in the darkness. Trembling with fear, Samantha turned to leave, but she was suddenly blinded by a bright light. As her eyes adjusted, she saw a ghostly figure standing before her, its eyes fixed on her with a menacing glare. Samantha screamed and ran out of the house, vowing never to return again."]}

def main(text):
    series = jsonData['series']
    outro = jsonData['outro']
    outfile = jsonData['outfile']
    path = jsonData['path']
    
    if os.path.isdir(f"{path}\\{series}"):
       pass
    else:
        os.mkdir(f"{path}\\{series}")

    path = f"{path}\\{series}\\{outfile}_{part}.mp3"

    finalText = f"{series} part {part}.\n{text}\n{outro}"

    subprocess.Popen(f'edge-tts --voice en-US-ChristopherNeural --text "{finalText}" --write-media "{path}"', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    

part = jsonData['part']

for text in jsonData['texts']:
    main(text)
    part += 1