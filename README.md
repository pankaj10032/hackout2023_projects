# hackout2023_projects
we are here basically making the multilingual speech to speech Question Answering sysetm, Here we have first taken the Audio file as input from the user in any language like Hindi, English, marathi, bangali,Tamil or any other 

**TO run the code, first just collect the audio file using the **


**Audio Extraction**:-
foreign language and taking audio into ".flac" format since our openai/whisper-large-v2 support this format only with the frequency should be 16000HZ and time duration to be less like around 10 second or lesser, so that context widnow of the 
model doesn't get fit

**Audio(any language) to English text**:-
After that we will convert our audio into English text so that it can be easily processed by LLM, using the "openai/whisper-large-v2" model using the transformers pipeline text generation since our task is just audio to text so need to fine tune the model.
