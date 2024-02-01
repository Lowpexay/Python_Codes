import re
from collections import Counter

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def count_characters(text):
    return len(text)

def count_sentences(text):
    sentences = re.split(r'[.!?]', text)
    return len([s for s in sentences if s.strip()])

def top_words_frequency(text, n=5):
    words = re.findall(r'\b\w+\b', text)
    word_counts = Counter(words)
    return word_counts.most_common(n)

if __name__ == "__main__":
    user_input = input("Digite o texto para análise: ")

    words_count = count_words(user_input)
    characters_count = count_characters(user_input)
    sentences_count = count_sentences(user_input)
    top_words = top_words_frequency(user_input)

    print(f"\nNúmero de palavras: {words_count}")
    print(f"Número de caracteres: {characters_count}")
    print(f"Número de frases: {sentences_count}")

    print("\nPalavras mais frequentes:")
    for word, frequency in top_words:
        print(f"{word}: {frequency} vezes")
