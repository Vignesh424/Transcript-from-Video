import assemblyai as aai

aai.settings.api_key = "API_CODE"

audio_url = "letitroll.mp3"

config = aai.TranscriptionConfig(language_detection=True)
transcriber = aai.Transcriber(config=config)

transcript = transcriber.transcribe(audio_url)
print(transcript.text)

