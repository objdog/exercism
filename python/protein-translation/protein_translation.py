def proteins(strand):
    protein = []
    stop_codon = 'STOP'
    TRANSLATIONS = {
        'Methionine':'AUG',
        'Phenylalanine': ['UUU', 'UUC'],
        'Leucine': ['UUA','UUG'],
        'Serine': ['UCU', 'UCC', 'UCA', 'UCG'],
        'Tyrosine': ['UAU', 'UAC'],
        'Cysteine': ['UGU', 'UGC'],
        'Tryptophan': 'UGG',
        'STOP': ['UAA', 'UAG', 'UGA']
        }
    if len(strand)>3:
        strand = [strand[i:i+3] for i in range(0,len(strand), 3)]
        for i in strand:
            protein.extend([key for key, value in TRANSLATIONS.items() if i in value])
    else:
        protein = [key for key, value in TRANSLATIONS.items() if strand in value]
    if stop_codon in protein:
        del protein[protein.index('STOP'):len(protein)]
    return protein
