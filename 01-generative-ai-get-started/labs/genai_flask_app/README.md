# GenAI Flask App (IBM Skills Network Lab)

Diese Dateien wurden anhand der Lab-Anleitung "Build Your First GenAI Application The Right Way" erstellt.

## Setup in der Cloud IDE

```bash
mkdir genai_flask_app
cd genai_flask_app
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Kopiere dann alle Dateien aus diesem Ordner (app.py, config.py, model.py, llm_test.py, capital.py,
templates/index.html) in dein `genai_flask_app`-Verzeichnis in der Cloud IDE.

## Statische Dateien (CSS/JS) selbst herunterladen

Diese zwei Dateien werden im Lab per `wget` von einem GitHub Gist geladen und konnten hier
NICHT automatisch mitgeliefert werden (Netzwerk-Sandbox hat keinen Zugriff auf gist.githubusercontent.com).
Führe in der Cloud IDE aus:

```bash
mkdir static
wget -O static/script.js "https://gist.githubusercontent.com/tenzinmigmar/0168709391266a8d8da7936f1a866c71/raw/95f4f4e1a1966b3f5183dd2f822cfcfd08d2238a/script.js"
wget -O static/styles.css "https://gist.githubusercontent.com/tenzinmigmar/278575598f79a4940993a1fc8640a60a/raw/24eda98885e854b01b4a46d1756112e91d3acc10/styles.css"
```

## Ausführen

```bash
python app.py
```

Dann die App über den Port-5000-Button in der Cloud IDE öffnen.

## Testen ohne Flask (Sanity Check)

```bash
python llm_test.py
```

## Übung: JSON-Struktur erweitern (aus dem Lab)

Die Lab-Anleitung enthält eine Übung: `AIResponse` in `model.py` um ein Feld für die empfohlene
nächste Aktion des Support-Mitarbeiters erweitern. Laut der im Lab bereitgestellten Musterlösung:

```python
class AIResponse(BaseModel):
    summary: str = Field(description="Summary of the user's message")
    sentiment: int = Field(description="Sentiment score from 0 (negative) to 100 (positive)")
    category: str = Field(description="Category of the inquiry (e.g., billing, technical, general)")
    action: str = Field(description="Recommended action for the support rep")
```

Passe danach ggf. den `system_prompt` in `app.py` an, damit das Modell auch `category` und `action`
sinnvoll befüllt (z. B. "Provide a helpful, concise response, and also classify the inquiry
category and suggest a next action for the support rep.").

Diese Datei enthält bewusst NICHT die erweiterte Version, da es im Lab als eigenständige Übung
gedacht ist - probier es selbst aus und teste mit verschiedenen Nutzer-Nachrichten!
