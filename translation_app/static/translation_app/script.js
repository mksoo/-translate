// 페이지가 로드되면 source-text의 글자수를 세는 기능
document.addEventListener('DOMContentLoaded', function() {
    var source_text_length = document.getElementById('source-text').value.length;
    document.getElementById('current-char-count').textContent = source_text_length;
});

// 버튼을 클릭하면 source-text, sourcelanguage, targetlanguage를 가져와서 새 URL로 이동하는 기능
document.getElementById('translate-button').addEventListener('click', function() {
    // 입력
    var sourceText = document.getElementById('source-text').value;
    var sourceLanguage = document.getElementById('language-select-source').value;
    var targetLanguage = document.getElementById('language-select-target').value;

    var currentUrl = window.location.href;
    var newUrl = currentUrl.split('?')[0] + "?sl=" + encodeURIComponent(sourceLanguage) + "&tl=" + encodeURIComponent(targetLanguage) + "&st=" + encodeURIComponent(sourceText);

    // 텍스트 길이
    var sourceTextLength = sourceText.length;

    // 텍스트 길이가 3000자 이상이면 경고창을 띄우고 번역을 하지 않음
    if (sourceTextLength > 3000){
        alert('3000자 이상의 텍스트는 번역할 수 없습니다.');
        return;
    }

    // 언어가 같으면 경고창을 띄우고 번역을 하지 않음
    if (sourceLanguage != targetLanguage){
        // 새 URL로 이동 (쿼리 파라미터 포함)
        window.location.href = newUrl;
    }else {
        alert('같은 언어로는 번역할 수 없습니다.');
    }
});

// 언어 선택 옵션을 동적으로 생성하는 기능
document.getElementById('language-select-source').addEventListener('change', function() {
    var selectedLanguage = this.value;
    var targetSelect = document.getElementById('language-select-target');
    var options = targetSelect.options;

    // language-select-target의 모든 옵션을 숨김 상태로 초기화
    for (var i = 0; i < options.length; i++) {
        options[i].style.display = "block";
    }

    // 선택된 언어와 일치하는 옵션을 숨김
    for (var i = 0; i < options.length; i++) {
        if (options[i].value === selectedLanguage) {
            options[i].style.display = "none";
            break;
        }
    }
});

// 텍스트를 복사하는 기능
document.getElementById('copy-translated-text').addEventListener('click', function() {
    var translatedText = document.getElementById('translated-text').value;

    // 텍스트를 복사하기 위한 임시 textarea 생성
    var tempArea = document.createElement('textarea');
    tempArea.value = translatedText; // 복사할 텍스트를 textarea에 넣음
    document.body.appendChild(tempArea); // body에 textarea를 추가
    tempArea.select(); // textarea를 선택
    document.execCommand('copy'); // 복사
    document.body.removeChild(tempArea); // body에서 textarea를 제거

    // 사용자에게 텍스트가 복사되었다는 것을 알리는 것이 좋음
    alert('텍스트가 복사되었습니다.');
});

// 번역 언어 교환
document.getElementById('change-language-button').addEventListener('click', function() {
    var sourceSelect = document.getElementById('language-select-source');
    var targetSelect = document.getElementById('language-select-target');

    // 현재 선택된 언어를 저장
    var currentSourceLanguage = sourceSelect.value;
    var currentTargetLanguage = targetSelect.value;

    // 언어 선택 옵션을 교환
    sourceSelect.value = currentTargetLanguage;
    targetSelect.value = currentSourceLanguage;
});

// 글자수 세는 기능
document.getElementById('source-text').addEventListener('input', function() {
    var textLength = this.value.length;
    document.getElementById('current-char-count').textContent = textLength;

    if (textLength > 3000)
        document.getElementById('current-char-count').style.color = "red";
    else
        document.getElementById('current-char-count').style.color = "#6c757d";
});

