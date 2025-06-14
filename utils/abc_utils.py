from music21 import converter, note, chord

def extract_notes(abc_path):

    stream = converter.parse(abc_path)
    notes = []
    
    for element in stream.flat.notes:
        if isinstance(element, note.Note):
            notes.append(str(element.pitch))
        elif isinstance(element, chord.Chord):
            notes.append('.'.join(str(n) for n in element.normalOrder))
    
    return notes