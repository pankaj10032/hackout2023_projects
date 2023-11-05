from audio_function import record_and_save_audio
from audio_cleaning import transcribe_audio
from llama2_text_2_text import setup_and_run_llm
from mbart_translator import translate_text
from text_to_speech_in_any_language import generate_audio
from Audio_play import play_audio_with_pygame
output_path=record_and_save_audio(16000, 5, '/home/naive123/nlp/Sumit/hackout/audio_file.flac')
# print(output_path)
model_id = 'meta-llama/Llama-2-7b-chat-hf'
query = "tell me about duronto express?"
transcription = transcribe_audio(output_path)
answer = setup_and_run_llm(model_id, query)

