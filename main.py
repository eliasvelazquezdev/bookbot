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
    
    
def main(file_path: str):
    with open(file_path) as f:
        file_contents = f.read()
        
        word_count :int = count_words(file_contents)        
        characters_in_text :dict[str, int] = count_characters(file_contents)
        sorted_dict = {
            k: v for k, v in sorted(
                characters_in_text.items(), 
                key=lambda item: item[1],
                reverse=True
            ) if k.isalpha()
        }
        
        report = f"--- Begin report of {file_path} ---\n"
        report += f"{word_count} words found in the document\n\n"
        
        for k, v in sorted_dict.items():
            report += f"The \'{k}\' character was found {v} times\n"
        
        report += "---End report---"
        print(report)



if __name__ == "__main__":
    file_path = "books/frankestein.txt"
    main(file_path)