from django.shortcuts import render

from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

LIST_OF_LANGUAGES = [
    ("ko_KR", "한국어"),
    ("en_XX", "영어"),
    ("ja_XX", "일어"),
    ("zh_CN", "중국어"),
    ("ar_AR", "아라비아어"),
    ("cs_CZ", "체코어"),
    ("de_DE", "독일어"),
    ("es_XX", "스페인어"),
    ("et_EE", "에스토니아어"),
    ("fi_FI", "핀란드어"),
    ("fr_XX", "프랑스어"),
    ("hi_IN", "힌두어"),
    ("it_IT", "이태리어"),
]


def translation(source_language, target_language, source_text):
    model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
    tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

    tokenizer.src_lang = source_language
    encoded_ar = tokenizer(source_text, return_tensors="pt")
    generated_tokens = model.generate(
        **encoded_ar,
        forced_bos_token_id=tokenizer.lang_code_to_id[target_language]
    )
    return tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)


def index(request):
    source_language = request.GET.get('sl', '')
    target_language = request.GET.get('tl', '')
    # source_text = request.GET.get('st', '')
    # translated_text = ''
    #
    # if source_language and target_language and source_text:
    #     translated_text = translation(source_language, target_language, source_text)

    source_text = "Hello, my name is John. I am 20 years old."
    translated_text = ["안녕하세요, 제 이름은 존입니다. 저는 20 살입니다."]

    return render(request, 'translation_app/index.html',
                  {
                      "source_text": source_text,
                      "translated_text": translated_text[0],
                      "source_language": source_language,
                      "target_language": target_language,
                      "list_of_languages": LIST_OF_LANGUAGES,
                  })
