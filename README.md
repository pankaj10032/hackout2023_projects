# hackout2023_projects
we are here basically making the multilingual speech to speech Question Answering sysetm, Here we have first taken the Audio file as input from the user in any language like Hindi, English, marathi, bangali,Tamil or any other 

**To run the code, first just collect the audio file using the file named "audio.py" **


**Audio Extraction**:-
foreign language and taking audio into ".flac" format since our openai/whisper-large-v2 support this format only with the frequency should be 16000HZ and time duration to be less like around 10 second or lesser, so that context widnow of the  model doesn't get fit
*for running Audio  extraction run the file named "audio.py" but make sure to specify the file path necessarily*

**Audio(any language) to English text**:-
After that we will convert our audio into English text so that it can be easily processed by LLM, using the "openai/whisper-large-v2" model using the transformers pipeline text generation since our task is just audio to text so need to fine tune the model.
*for converting audio to text run the file named "audio_cleaning.py" *


**Text to Text Question Answering**
In this case we have user query as obtained from the last step from audio to text we take llama for text generation model using huggingface pipeiline, we have also a pdf(data) containing some information related to the railway we first load that data, split that data into chunk size of 1024 with chunk overlap of 20, then compute embeddings of all those chunk using sentence transformers models and store chunks of fixed size in the FAISS vector store, then using the conversation chain we just get the most relevant context among all those chunk(1024) size and passing them to LLM(llama for text generation) to get the relevant answer.

**make sure before using llama you must have the access of that, you can get the access of that on meta website by filling the google form of that and also get the access from huggingface also , put the samer Email id at both the places.**

*Here we can also use OpenAI but On the industry level that will be cosly,we can also use higher versions of Llama like 13b, 70b parameters model to get the better results.*

*Our next step is to used the *
