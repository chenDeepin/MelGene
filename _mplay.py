# Play the generated music using a MIDI library (e.g., mido)
# Created by Chenran Jiang @chenDeepin (2025.1.25)

import mido
from mido import MidiFile, MidiTrack, Message

def play_music(music_sequence, music_type):
    """
    Plays the generated music sequence using a MIDI library.
    """
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    for key in music_sequence:
        track.append(Message('note_on', note=key, velocity=64, time=480))
        track.append(Message('note_off', note=key, velocity=64, time=480))

    mid.save(f'{music_type}_gene_music.mid')
    print(f"MIDI file saved as '{music_type}_gene_music.mid'")
    print("Playing music...")
    with mido.open_output() as port:
        for msg in mid.play():
            port.send(msg)
            print(msg)
            print("Music finished playing.")
            break
