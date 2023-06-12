from django.shortcuts import render
import openai
import os

openai.api_key = os.environ.get('API_KEY')

def translate_jp_to_en(input_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"あなたはプロの翻訳家です。自然な文章で以下の文章を英語に翻訳してください。:\n{input_text}\n\n"
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

def proofreading_to_text(input_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"以下の文章を適切な形にしてください:\n{input_text}\n\n"),
        temperature=0.7,
        max_tokens=120,
    )
    return response.choices[0].text.strip()

def top_view(request):
    return render(request,"top.html")

def talk_view(request):
    return render(request,"talk.html")

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

def proofreading_view(request):
    input_text = ""
    proofreading_text = ""
    if request.method == 'POST':
        input_text = request.POST['input_text']
        if "proofreadingBtn" in request.POST:
            print("文章校正開始")
            proofreading_text = proofreading_to_text(input_text)

    return render(request, 'proofreading.html', {'input_text': input_text, 'proofreading_text': proofreading_text})


