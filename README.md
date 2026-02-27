# Message-To-Morse-Code-Converter

 Morse Code Audio Generator

A Python project that converts any user input message into Morse Code audio.

The program reads pre-recorded Morse code audio files (A-Z, 0-9) from a folder and combines them into a single exported `.mp3` file.

---

 📌 Features

- Convert any text message to Morse code audio
- Supports letters A–Z
- Supports numbers 0–9
- Automatically skips unsupported characters
- Exports combined Morse audio as `output_morse.mp3`
- Adjustable letter and word spacing

All audio file names must exactly match their characters (e.g., `A.mp3`, `B.mp3`, `1.mp3`).

---

 # Requirements

- Python 3.12
- pydub
- ffmpeg (must be installed and added to PATH)

---

# Installation

1. Install Python 3.12
2. Install required library:

   
---

## How It Works

1. Takes user input
2. Converts message to uppercase
3. Loads matching letter audio files
4. Combines them with silence gaps
5. Exports final Morse code audio

---

# Example

Input: "Hi Im Mr Frily"
prosess: convert Each letters Morese code And Add the Mp3 File together With silence Separated Audio;
output: Each File Is Saved Into "Output mp3 " Audio File . New File / New Execution Is Appended In to This Mp3 File 


# Enjoy 
