from googletrans import Translator

# Initialize the Translator
translator = Translator()

# Function to translate text
def translate_text(text, dest_lang):
    try:
        # Translate the text
        translated = translator.translate(text, dest=dest_lang)
        return translated.text
    except Exception as e:
        return f"Error: {e}"

# Example usage
text_to_translate = "Hello, how are you?"
destination_language = "fr"  # French

translated_text = translate_text(text_to_translate, destination_language)
print(f"Translated text: {translated_text}")
