# This script is used to define the range of musical keys based on the type of music. Have fun!
# Created by Chenran Jiang @chenDeepin (2025.1.25)

from ._keynotes import get_black_key_groups, get_black_key_sequence

EXTRA_KEY_RATIO = 0.35  # 35% of the keys in Part C will be from the extra range

# Assign black keys based on the music type
def assign_black_keys(music_type):
    black_key_groups = get_black_key_groups()
    black_key_sequence = get_black_key_sequence(music_type)
    
    if not black_key_sequence:
        raise ValueError("Invalid music type. Choose from: pop, classic, R&B, jazz, electronic, rock, blues.")
    
    black_keys = {}
    for i, key in enumerate(black_key_sequence):
        group = i + 1  # Groups are 1-indexed
        black_keys[key] = black_key_groups[group]
    
    return black_keys

def get_key_ranges(music_type):
    """
    Returns the most often used range (80%) and the full range (100%) for a given music type.
    """
    if music_type == 'classical':
        full_range = (36, 84)  # C2 to C6
        most_used_range = (48, 72)  # C3 to C5
    elif music_type == 'pop':
        full_range = (60, 84)  # C4 to C6
        most_used_range = (64, 76)  # E4 to E5
    elif music_type == 'r&b':
        full_range = (48, 72)  # C3 to C5
        most_used_range = (52, 68)  # E3 to G4
    elif music_type == 'jazz':
        full_range = (36, 84)  # C2 to C6
        most_used_range = (48, 72)  # C3 to C5
    elif music_type == 'electronic':
        full_range = (24, 84)  # C1 to C6 (low for sub-bass, mid-high for leads)
        most_used_range = (48, 72)  # C3 to C5
    elif music_type == 'rock':
        full_range = (36, 84)  # C2 to C6
        most_used_range = (48, 72)  # C3 to C5
    elif music_type == 'blues':
        full_range = (36, 84)  # C2 to C6
        most_used_range = (48, 72)  # C3 to C5
    else:
        raise ValueError("Unsupported music type. Choose from: classical, pop, r&b, jazz, electronic, rock, blues.")

    return most_used_range, full_range

def use_extra_keys(part_c_sequence, most_used_range, full_range):
    """
    Ensures that Part C uses the extra keys (outside the most often used range) with a specific ratio.
    """
    extra_keys = set(range(full_range[0], full_range[1] + 1)) - set(range(most_used_range[0], most_used_range[1] + 1))
    extra_keys = list(extra_keys)
    
    # Calculate how many extra keys to use
    num_extra_keys = int(len(part_c_sequence) * EXTRA_KEY_RATIO)
    
    # Replace some keys in Part C with extra keys
    for i in range(num_extra_keys):
        part_c_sequence[i] = extra_keys[i % len(extra_keys)]
    
    return part_c_sequence