def count_ocurrences(path: str, word: str) -> int:
    file = open(path, "r")  # começando agr VQV
    read_data = file.read()
    word_count = read_data.lower().count(word.lower())
    return word_count
