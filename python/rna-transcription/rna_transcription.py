def to_rna(dna_strand):
    TRANSCRIPTION = {
        "G":"C",
        "C":"G",
        "T":"A",
        "A":"U"
    }
    
    result = ""
    for c in dna_strand:
        result += TRANSCRIPTION[c]
    return result
    