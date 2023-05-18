from django.shortcuts import render
from django.conf import settings
import openai
import os

openai.api_key = settings.API_KEY

def translate_jp_to_en(input_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"You are a professional translator. Translate the following sentences into English in a natural way:\n{input_text}\n\n"
                "Translation:"),
        temperature=0.7,
        max_tokens=60,
    )
    return response.choices[0].text.strip()

def translate_en_to_jp(input_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"You are a professional translator. Translate the following sentences into Japanese in a natural way:\n{input_text}\n\n"
                "Translation:"),
        temperature=0.7,
        max_tokens=60,
    )
    return response.choices[0].text.strip()


def translation_view(request):
    input_text = ""
    translated_text = ""
    if request.method == 'POST':
        input_text = request.POST['input_text']
        if "transBtn" in request.POST:
            print("翻訳ボタンが押された")
            translated_text = translate_jp_to_en(input_text)
        
        if "reverseBtn" in request.POST:
            print("リバースボタンが押された")
            translated_text = translate_en_to_jp(input_text)

    return render(request, 'translation.html', {'input_text': input_text, 'translated_text': translated_text})