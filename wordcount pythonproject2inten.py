def count_words(text):
    """Function to count the number of words in the given text."""
    words = text.split()  # Splitting the text by spaces
    return len(words)  # Returning the word count

def main():
    """Main function to handle user input and display the word count."""
    user_input = input("Enter a sentence or paragraph: ").strip()
    
    if not user_input:
        print("Error: No input provided. Please enter some text.")
    else:
        word_count = count_words(user_input)
        print(f"Word Count: {word_count}")

if _name_ == "_main_":
    main()


Enter a sentence or paragraph: The quick brown fox jumps over the lazy dog.
Word Count: 9
