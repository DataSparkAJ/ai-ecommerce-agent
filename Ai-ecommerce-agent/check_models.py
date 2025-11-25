import google.generativeai as genai

# Enter API key manually here between quotes
genai.configure(api_key="AIzaSyBwsV4N2iE8ZXy73adaKVBnG-pEjcEXp5s")

from google.generativeai import list_models

print("\n=== Available Gemini Models ===\n")
for m in list_models():
    print(m.name)
