# 113vr

/Volumes/MacPro/downloads/113_PlantVR-main/Assets/TutorialSystem/Files/audio

```
import edge_tts
import asyncio
import os
import pandas as pd
import argparse


async def run_tts(text: str, output: str, speaker: str) -> None:
    print(speaker)
    if speaker == "default_image" or speaker == "default":
        voice = 'zh-TW-HsiaoYuNeural'
        communicate = edge_tts.Communicate(text, voice, rate="+20%", volume="+0%")
    elif speaker == "小綠":
        voice = 'zh-TW-HsiaoChenNeural'
        communicate = edge_tts.Communicate(text, voice, rate="+30%", volume="+0%")
    else:
        voice = 'zh-TW-YunJheNeural'  # 使用另一個語音作為默認
        communicate = edge_tts.Communicate(text, voice, rate="+25%", volume="+0%")

    await communicate.save("tmp.mp3")
    try:
        os.rename("tmp.mp3", output)
    except FileExistsError:
        os.remove(output)
        os.rename("tmp.mp3", output)

async def main(overwrite = False):
    print("Start")
    os.makedirs('output', exist_ok=True)
    df = pd.read_csv('../text.csv')
    df['step'] = df['step'].apply(lambda x: str(int(x)) if pd.notna(x) else x)
    df['historyId'] = df['historyId'].apply(lambda x: str(int(x)) if pd.notna(x) else x)
    df['audio-自學'] = df['audio-自學'].apply(lambda x: str(int(x)) if pd.notna(x) else x)
    df['audio-導學'] = df['audio-導學'].apply(lambda x: str(int(x)) if pd.notna(x) else x)    
    
    texts = []
    audios = []
    speakers = []
    for row in df.columns:
        if row.startswith("text"):
            texts.append(row)            
        if row.startswith("audio"):
            audios.append(row)
        if row.startswith("speaker"):
            speakers.append(row)
            speakers.append(row)
    
    processing = {}
    for idx, row in df.iterrows():
        for text, audio, speaker in zip(texts, audios, speakers):            
            if (pd.notna(row[text]) and not str(row[text]).startswith('<')):
                temp = {"audio": row[audio], "text": row[text], "speaker": row[speaker]}             
                processing[row[audio]] = temp
                
    for audio, dic in processing.items():
        if not os.path.exists(f'output/{audio}.mp3') or overwrite:
            text = dic["text"]
            speaker = dic["speaker"]
            print(f"Processing {audio} => {text}")
            await asyncio.gather(run_tts(text, f'output/{audio}.mp3', speaker))
    
    print("Done")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--overwrite', action='store_true')
    args = parser.parse_args()
    asyncio.run(main(args.overwrite))
```
