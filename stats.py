import re


def count_words(file_contents: str) -> int:
    words = file_contents.split()
    return len(words)


def count_characters(
    file_contents: str
) -> dict[str, int]:
    words = re.split(r'(\s+)', file_contents)
    
    characters_found = []
    for word in words:
        lowered_word = word.lower()
        for character in lowered_word:
            if character not in characters_found:
                characters_found.append(character)
            
    characters_count_dict = {char : 0 for char in characters_found}
    for character in characters_found:
        character_count = 0
        for word in words:
            lowered_word = word.lower()
            if character in lowered_word:
                for letter in lowered_word:
                    if letter == character:
                        character_count += 1
        characters_count_dict[character] = character_count
    
    return characters_count_dict