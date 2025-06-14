import pretty_midi

def extract_notes(midi_path):
    
    midi_data = pretty_midi.PrettyMIDI(midi_path)
    notes = []
    
    for instrument in midi_data.instruments:
        if not instrument.is_drum:
            for node_obj in instrument.notes:
                notes.append(node_obj.pitch)
    
    return notes

def save_notes(notes, output_path, velocity=100, note_duration=0.5):
    midi = pretty_midi.PrettyMIDI()
    piano = pretty_midi.Instrument(program=0)
    
    start = 0
    for pitch in notes:
        note_obj = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start+note_duration)
        piano.notes.append(note_obj)
        start += note_duration
        
        midi.instruments.append(piano)
        midi.write(output_path)
        print(f"MIDI file saved to {output_path}")