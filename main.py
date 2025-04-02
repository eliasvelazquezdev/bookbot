import sys

from stats import count_words, count_characters

    
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
        
        report = f"============ BOOKBOT ============\n"
        report += f"Analyzing book found at {file_path}...\n"
        
        report += f"----------- Word Count ----------\n"
        report += f"Found {word_count} total words\n"
        
        report += "--------- Character Count -------\n"
        
        for k, v in sorted_dict.items():
            report += f"{k}: {v}\n"
        
        report += "============= END ==============="
        print(report)



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    main(file_path)