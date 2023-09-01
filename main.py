def count_and_replace_terrible(input_text):
    word_count = 0
    words = input_text.split()
    new_words = []

    for word in words:
        if word.strip(".,?!") == "terrible":
            word_count += 1

    replace_even = False
    for word in words:
        cleaned_word = word.strip(".,?!")
        if cleaned_word == "terrible":
            if replace_even:
                new_words.append("pathetic")
            else:
                new_words.append("marvellous")
            replace_even = not replace_even
        else:
            new_words.append(word)

    new_text = " ".join(new_words)
    return word_count, new_text

def main():
    with open("file_to_read.txt", "r") as file:
        input_text = file.read()

    word_count, new_text = count_and_replace_terrible(input_text)

    with open("result.txt", "w") as file:
        file.write(new_text)

    print("Total occurrences of 'terrible':", word_count)
    print("Modified text written to 'result.txt'.")

if __name__ == "__main__":
    main()
