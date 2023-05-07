from django.shortcuts import render
import openai
import os

openai.api_key = os.getenv("APIKEY")

def translate(input_text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"Translate the following text from English to Japanese:\n{input_text}\n\n"
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
        if input_text:
            translated_text = translate(input_text)
    return render(request, 'translation.html', {'input_text': input_text, 'translated_text': translated_text})
