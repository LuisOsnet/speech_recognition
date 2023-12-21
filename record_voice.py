import pyaudio
import wave

def grabar_audio(nombre_archivo, duracion=5):
    formato = pyaudio.paInt16
    canales = 1
    tasa_muestreo = 44100
    chunk = 1024
    dispositivo = None

    audio = pyaudio.PyAudio()

    stream = audio.open(format=formato,
                        channels=canales,
                        rate=tasa_muestreo,
                        input=True,
                        frames_per_buffer=chunk,
                        input_device_index=dispositivo)

    print("Grabando audio...")
    frames = []

    for i in range(0, int(tasa_muestreo / chunk * duracion)):
        data = stream.read(chunk)
        frames.append(data)

    print("¡Grabación finalizada!")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(nombre_archivo, 'wb') as wf:
        wf.setnchannels(canales)
        wf.setsampwidth(audio.get_sample_size(formato))
        wf.setframerate(tasa_muestreo)
        wf.writeframes(b''.join(frames))

    print(f"Audio guardado como {nombre_archivo}")

# Ejemplo de uso:
nombre_archivo_usuario_1 = "audio_usuario_1.wav"
grabar_audio(nombre_archivo_usuario_1)
