# tranXcribe

Transcribing audio files to text using openAI [Whisper](https://openai.com/research/whisper)
#### Supported audio formats - m4a, mp3, webm, mp4, mpga, wav, mpeg
Read FAQs [here](https://help.openai.com/en/articles/7031512-whisper-api-faq)

[CLI version](https://github.com/sacheex/tranXcribe-CLI) of this Web App
### Installation


```console
# clone the repo
$ git clone https://github.com/sacheex/tranXcribe.git

# navigate to the directory
$ cd tranXcribe

# install the requirements
$ python3 -m pip install -r requirements.txt
```

### Usage

Generate [Openai API key](https://platform.openai.com/account/api-keys) and add it to the ```.env``` file.

``` console
OPENAI_API_KEY = "<add your OPENAI API KEY here>"
```

#### Run the app

```console
$ python app.py
```
Visit ```http://127.0.0.1:5000/``` in your browser


### Screenshots

<img src="https://github.com/sacheex/tranXcribe/blob/main/static/images/screencapture-127-0-0-1-5000-generate-2023-05-19-21_24_23.png" alt="Screenshot" width="750px">

