"""
Testet die erweiterte AIResponse-Struktur (mit category & action) aus der Übung
"Enhancing the JSON Structure" mit mehreren unterschiedlichen Nutzer-Nachrichten.
Ausführen mit: python llm_test_exercise.py
"""
from model import llama_response, granite_response, mistral_response

system_prompt = (
    "You are an AI assistant helping with customer inquiries. "
    "You must always return ALL five fields: summary, sentiment, response, "
    "category, and action. Never omit any field, especially 'response'.\n\n"
    "Example of a correctly formatted output for the message "
    "'My package never arrived':\n"
    '{"summary": "The user\'s package was never delivered.", '
    '"sentiment": 10, '
    '"response": "I\'m sorry to hear your package didn\'t arrive. '
    'We will look into this right away and keep you updated.", '
    '"category": "shipping", '
    '"action": "Check the tracking status and contact the carrier to '
    'locate the missing package."}'
)

test_messages = [
    "I was charged twice for my subscription this month, can you help?",
    "My app keeps crashing every time I try to upload a photo.",
    "How do I change the email address on my account?",
]

for msg in test_messages:
    print("\n" + "=" * 60)
    print(f"USER MESSAGE: {msg}")
    print("=" * 60)
    result = granite_response(system_prompt, msg)
    print(result)
