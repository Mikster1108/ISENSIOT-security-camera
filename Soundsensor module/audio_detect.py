import pyaudio
import numpy as np
import wave
import datetime

CHUNK = 1024  # Number of frames per buffer
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1  # Number of audio channels (1 for mono, 2 for stereo)
RATE = 44100  # Sample rate (samples per second)

THRESHOLD = 2000  # Adjust this threshold according to your needs
MIN_RECORDING_DURATION = 30  # Minimum recording duration in seconds

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
               channels=CHANNELS,
               rate=RATE,
               input=True,
               frames_per_buffer=CHUNK)

print("Listening for sound threshold...")

recording = False
frames = []
start_time = None

while True:
    data = stream.read(CHUNK)
    audio_data = np.frombuffer(data, dtype=np.int16)

    # Check if the audio amplitude exceeds the threshold
    if np.max(np.abs(audio_data)) > THRESHOLD:
        if not recording:
            print("Sound threshold reached. Recording started.")
            recording = True
            frames = []
            start_time = datetime.datetime.now()

        frames.append(data)

        # Check if recording duration exceeds the minimum duration
        if (datetime.datetime.now() - start_time).total_seconds() >= MIN_RECORDING_DURATION:
            # Stop recording and save the audio file
            print("Recording stopped.")
            recording = False

            filename = f"audio_{start_time.strftime('%Y%m%d%H%M%S')}.wav"

            wf = wave.open(filename, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

            print(f"Audio saved to {filename}")

stream.stop_stream()
stream.close()
p.terminate()

