import os
from pydub import AudioSegment

"""
Folders for MP3 morese code audio 
"""
AUDIO_FOLDER = "Morse Code Mp4"

"""
Silence for between the audio
"""
LETTER_GAP = AudioSegment.silent(duration=400)
WORD_GAP = AudioSegment.silent(duration=800)


def text_to_morse_audio(message):

    message = message.upper()
    final_audio = AudioSegment.empty()

    for char in message:
        if char == " ":
            final_audio += WORD_GAP
            continue

        file_path = os.path.join(AUDIO_FOLDER, f"{char}.mp3")

        if os.path.exists(file_path):
            letter_audio = AudioSegment.from_mp3(file_path)
            final_audio += letter_audio
            final_audio += LETTER_GAP
        else:
            print(f"out of range: {char}")

    return final_audio


if __name__ == "__main__":
    print("==============================================================")
    print("=========                                         ============")
    print("========= Welcome To Text To Morse Code ConverTer ============")
    print("=========                                         ============")
    print("=========            CREATED BY KAL-B             ============")
    print("=========                                         ============")
    print("==============================================================")

    user_input = input("Enter your message To Convert In To Morse Code -> ")

    morse_audio = text_to_morse_audio(user_input)

    morse_audio.export("output_morse.mp3", format="mp3")

    print("Tnx Your Morse code audio exported as output_morse.mp3")