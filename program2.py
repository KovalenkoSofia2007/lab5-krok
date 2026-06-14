from urllib.parse import unquote
import pyperclip

encoded_url = "https://uk.wikipedia.org/wiki/%D0%A8%D1%82%D1%83%D1%87%D0%BD%D0%B8%D0%B9_%D1%96%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D1%82"

decoded_url = unquote(encoded_url)

print("Оригінальне посилання:\n" + encoded_url)
print("\nРозкодоване посилання:\n" + decoded_url)

pyperclip.copy(decoded_url)
print("\n[Успіх] Розкодоване посилання успішно скопійовано до буфера обміну!")