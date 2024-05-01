def reverse_words(sentence):
    return' '.join(word[::-1] for word in sentence.split())
input_sentence = input("Enter a sentence")
reversed_sentence= reverse_words(input_sentence)
print("Reversed sentence",reversed_sentence)
