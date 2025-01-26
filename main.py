# This script is used to transform the Gene data into Music notes. Have fun!
# Created by Chenran Jiang @chenDeepin (2025.1.25)

from src._transformation import generate_music_sequence
from src._mplay import play_music

# Example mRNA sequence
mrna_sequence = input("Enter mRNA sequence: ").strip().upper()
music_type = input("Enter music type (pop, classical, r&b, jazz, electronic, rock, blues): ").strip().lower()

# Generate music sequences
music_sequence = generate_music_sequence(mrna_sequence, music_type)

# Play the music
play_music(music_sequence, music_type)