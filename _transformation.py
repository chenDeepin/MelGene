# This script is used to transform the Gene data into Music notes. Have fun!
# Created by Chenran Jiang @chenDeepin (2025.1.25)

from ._mtype import get_key_ranges, use_extra_keys
from ._keynotes import combine_codon_frequencies

def determine_black_key_pitch(previous_pitch, key_range):
    """
    Determines the black key's pitch based on the previous key note's pitch.
    Ensures the pitch stays within the specified range.
    """
    min_key, max_key = key_range
    # Example logic: increment by 2 semitones, but ensure it stays within the range
    new_pitch = previous_pitch + 2
    if new_pitch > max_key:
        new_pitch = min_key + (new_pitch - max_key - 1)
    return new_pitch

def map_codons_to_keys(sequence, music_type):
    most_used_range, full_range = get_key_ranges(music_type)  # Unpack the tuple of tuples
    min_key, max_key = full_range  # Use full_range for key_count calculation
    key_count = max_key - min_key + 1
    codon_to_key = {}

    all_codons = []
    new_codon_frequencies = combine_codon_frequencies(music_type)
    # Collect all codons into a flat list
    for key in new_codon_frequencies:
        all_codons.extend(new_codon_frequencies[key].keys())

    for i, codon in enumerate(all_codons):  # Use all_codons instead of new_codon_frequencies
        key = min_key + (i % key_count)
        codon_to_key[codon] = key

    # Handle sequence length not divisible by 3
    truncated_sequence = sequence[:len(sequence) - (len(sequence) % 3)]
    return [codon_to_key.get(truncated_sequence[i:i+3], min_key) 
            for i in range(0, len(truncated_sequence), 3)]

def generate_music_sequence(mrna_sequence, music_type):
    # Skip the start codon (AUG)
    if mrna_sequence.startswith('AUG'):
        mrna_sequence = mrna_sequence[3:]
    
    most_used_range, full_range = get_key_ranges(music_type)
    
    # Split the mRNA sequence into three parts (truncate if needed)
    part_length = len(mrna_sequence) // 3
    part_a = mrna_sequence[:part_length]
    part_b = mrna_sequence[part_length:2*part_length]
    part_c = mrna_sequence[2*part_length:]
    
    # Map codons to keys
    part_a_sequence = map_codons_to_keys(part_a, music_type)
    part_b_sequence = map_codons_to_keys(part_b, music_type)
    part_c_sequence = map_codons_to_keys(part_c, music_type)
    
    # Apply extra keys to Part C
    part_c_sequence = use_extra_keys(part_c_sequence, most_used_range, full_range)
    music_sequence = part_a_sequence + part_b_sequence + part_c_sequence +part_a_sequence + part_b_sequence
    print(f"Generated music sequence: {music_sequence}")     
    
    return music_sequence
