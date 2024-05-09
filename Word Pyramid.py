def word_pyramid(word):
    for i in range(len(word)):
        print(' '*(len(word)-i-1)+word[:i+1])
def main():
    user_input = input("Enter a word: ")
    word_pyramid(user_input)
if __name__=="__main__":
    main()
    
