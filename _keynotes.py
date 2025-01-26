# This script is used to define the keys. Have fun!
# Created by Chenran Jiang @chenDeepin (2025.1.25)

# Define codon frequencies for white keys
codon_frequencies = {
    'C': {'UUA': 7.7, 'UUG': 12.9, 'CUU': 13.2, 'CUC': 19.6, 'CUA': 7.2, 'CUG': 39.6,
          'CGU': 4.5, 'CGC': 10.4, 'CGA': 6.2, 'CGG': 11.4, 'AGA': 12.2, 'AGG': 12.0},
    'D': {'GCU': 18.4, 'GCC': 27.7, 'GCA': 15.8, 'GCG': 7.4, 'GAA': 29.0, 'GAG': 39.6},
    'E': {'GGU': 10.8, 'GGC': 22.2, 'GGA': 16.5, 'GGG': 16.3, 'AUU': 16.0, 'AUC': 20.8, 'AUA': 7.5},
    'F': {'AAA': 24.4, 'AAG': 31.9, 'UGU': 10.4, 'UGC': 12.6},
    'G': {'UCU': 15.2, 'UCC': 17.7, 'UCA': 12.2, 'UCG': 4.4, 'AGU': 12.1, 'AGC': 19.5, 'GAU': 21.8, 'GAC': 25.1},
    'A': {'ACU': 13.1, 'ACC': 18.9, 'ACA': 15.1, 'ACG': 6.1, 'CCU': 17.5, 'CCC': 19.8, 'CCA': 16.9, 'CCG': 6.9},
    'B': {'GUU': 11.0, 'GUC': 14.5, 'GUA': 7.1, 'GUG': 28.3}
}

# Define the white keys and their corresponding amino acids and frequencies
def get_white_keys():
    white_keys = {
        'C': {'amino_acids': ['Leucine', 'Arginine'], 'frequency': 15.1},
        'D': {'amino_acids': ['Alanine', 'Glutamic Acid'], 'frequency': 13.7},
        'E': {'amino_acids': ['Glycine', 'Isoleucine'], 'frequency': 12.1},
        'F': {'amino_acids': ['Lysine', 'Cysteine'], 'frequency': 7.5},
        'G': {'amino_acids': ['Serine', 'Aspartic Acid'], 'frequency': 11.3},
        'A': {'amino_acids': ['Threonine', 'Proline'], 'frequency': 11.1},
        'B': {'amino_acids': ['Valine'], 'frequency': 6.6}
    }
    return white_keys

# Define the black key groups and their corresponding amino acids and frequencies
def get_black_key_groups():
    """
    Returns the black key groups with their corresponding codons and frequencies.
    """
    black_key_groups = {
        1: {'codons': ['UGG', 'UUU', 'UUC'], 'frequency': 5.2},  # Tryptophan, Phenylalanine
        2: {'codons': ['CAU', 'CAC', 'AUG'], 'frequency': 4.7},  # Histidine, Methionine
        3: {'codons': ['AAU', 'AAC'], 'frequency': 4.4},         # Asparagine
        4: {'codons': ['CAA', 'CAG'], 'frequency': 4.0},         # Glutamine
        5: {'codons': ['UAU', 'UAC'], 'frequency': 3.2}          # Tyrosine
    }
    return black_key_groups

# Define the black key sequences for each music type
def get_black_key_sequence(music_type):
    sequences = {
        'pop': ['F#', 'G#', 'D#', 'A#', 'C#'],
        'classical': ['F#', 'D#', 'G#', 'A#', 'C#'],
        'r&b': ['G#', 'F#', 'A#', 'D#', 'C#'],
        'jazz': ['G#', 'D#', 'A#', 'F#', 'C#'],
        'electronic': ['F#', 'G#', 'D#', 'A#', 'C#'],
        'rock': ['F#', 'G#', 'D#', 'A#', 'C#'],
        'blues': ['F#', 'G#', 'D#', 'A#', 'C#']
    }
    return sequences.get(music_type, [])

def combine_codon_frequencies(music_type):
    """
    Combines white key codons and black key codons into a single dictionary based on the music type.
    """
    # Get white key codons
    white_keys = codon_frequencies
    
    # Get black key groups
    black_key_groups = get_black_key_groups()
    
    # Get black key sequence for the specified music type
    black_key_sequence = get_black_key_sequence(music_type)
    
    # Initialize new_codon_frequencies with white key codons
    new_codon_frequencies = white_keys.copy()
    
    # Add black key codons to new_codon_frequencies
    for i, key in enumerate(black_key_sequence):
        group = i + 1  # Groups are 1-indexed
        new_codon_frequencies[key] = black_key_groups[group]
    
    return new_codon_frequencies


