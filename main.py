def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = count_words(file_contents)
        chars = count_chars(file_contents)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words} words found in the document\n")

        list_chars = []
        for char in chars:
            if char.isalpha():
                list_chars.append({"char": char, "count": chars[char]})
        list_chars.sort(reverse=True, key=lambda x: x["count"])
        for dict in list_chars:
            print(f"The '{dict["char"]}' character was found {dict["count"]} times")

        print("--- End report ---")

def count_words(words):
    return len(words.split())

def count_chars(words):
    chars = {}
    words = words.split()
    for word in words:
        lowered_word = word.lower()
        for char in lowered_word:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

main()
