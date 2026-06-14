import re

def custom_sort(text):
    words = re.findall(r'\b[A-Za-zА-Яа-яЄєІіЇїҐґ_]+\b', text)

    def sort_key(word):
        word_lower = word.lower()
        is_latin = 1 if re.match(r'^[a-z]', word_lower) else 0
        
        alphabet = "а б в г ґ д е є ж з и і ї й к л м н о п р с т у ф х ц ч ш щ ь ю я"
        letter_order = {letter: index for index, letter in enumerate(alphabet.split())}
        
        word_key = []
        for char in word_lower:
            if char in letter_order:
                word_key.append(letter_order[char])
            else:
                word_key.append(ord(char))
                
        return (is_latin, word_key)

    return sorted(words, key=sort_key)

with open('text.txt', 'r', encoding='utf-8') as file:
    text_content = file.read()

print("--- Оригінальний текст ---")
print(text_content)

sorted_words = custom_sort(text_content)

print("\n--- Відсортований список слів ---")
print(sorted_words)