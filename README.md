# Chatbot Ollama

이 프로젝트는 두 개의 챗봇 애플리케이션을 포함하고 있습니다.

## 프로젝트 구조

```
chatbot_ollama/
├── bank_transaction_bot.py    # 은행 거래 챗봇
├── conversation_bot.py        # 대화형 챗봇
└── README.md                  # 프로젝트 설명서
```

## 실행 방법

### 1. 은행 거래 챗봇 (bank_transaction_bot.py)

```bash
python3 bank_transaction_bot.py
```

#기능
- 입금 (1번 선택)
- 출금 (2번 선택)
- 잔액확인 (3번 선택)
- 종료 (4번 선택)

#사용법
1. 프로그램 실행 후 원하는 기능의 번호를 입력
2. 입금/출금 선택 시 금액을 입력
3. 4번을 선택하여 프로그램 종료

#2. 대화형 챗봇 (conversation_bot.py)

```bash
python3 conversation_bot.py
```

#기능
- 사용자와의 자연스러운 대화
- 질문에 대한 답변 제공
- 대화 종료 기능

#사용법
1. 프로그램 실행 후 질문이나 메시지 입력
2. 챗봇의 응답 확인
3. '종료' 또는 'quit' 입력하여 프로그램 종료

#시스템 요구사항

- Python 3.x
- macOS, Linux, Windows 지원

## 설치 및 실행

1. 프로젝트 클론
```bash
git clone https://github.com/codfin02/chatbot_ollama.git
cd chatbot_ollama
```

2. 프로그램 실행
```bash
# 은행 거래 챗봇 실행
python3 bank_transaction_bot.py

# 대화형 챗봇 실행
python3 conversation_bot.py
```

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 