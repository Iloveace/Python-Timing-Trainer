#! C:\Users\Mayeu\OneDrive\Desktop\BPM\venv\Scripts\python.exe
import librosa

def detect_bpm(audio_file):
    # Load audio file
    y, sr = librosa.load(audio_file)

    # Calculate onset envelope
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)

    # Detect beats
    tempo, _ = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)

    return tempo

# Example usage
bpm = detect_bpm('venv/Take It Off.mp3')
print("Estimated BPM:", bpm)
