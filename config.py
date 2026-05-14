import os

# Groq API Key
GROQ_API_KEY = "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"

# Model settings (Groq uses different models)
MODEL_NAME = "llama-3.1-8b-instant"
TEMPERATURE = 0.5
MAX_TOKENS = 200

# Safety settings
DANGEROUS_KEYWORDS = [
    "suicide",
    "kill myself",
    "overdose",
    "prescription",
    "antibiotic dose"
]