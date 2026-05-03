# Password Generator API 🔐
![CI Status](https://github.com/111qqq222www333eee/password-generator/actions/workflows/ci.yml/badge.svg)

Prosty i bezpieczny serwis API do generowania silnych haseł.
TEst123


## 🚀 Uruchomienie lokalne
1. `python -m venv .venv`
2. `source .venv/bin/activate`  # Windows: .venv\Scripts\activate
3. `pip install -r requirements.txt`
4. `uvicorn app.main:app --reload`

## 🧪 Testy
Uruchomienie testów jednostkowych:
- `pytest`

## 🐳 Docker
Obraz jest automatycznie budowany i publikowany na Docker Hub:
- **Obraz:** `111qqq222www333eee/password-generator:latest`

Aby pobrać i uruchomić:
```bash
docker pull 111qqq222www333eee/password-generator:latest
docker run -d -p 8000:8000 --name pwd-gen 111qqq222www333eee/password-generator
Link do obrazu: https://hub.docker.com/r/111qqq222www333eee/password-generator
