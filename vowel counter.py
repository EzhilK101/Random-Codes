def vowels(string):
        vowel = "aeiouAEIOU"
        vowel_count = 0
        for char in string:
            if char in vowel:
                vowel_count +=1
        return vowel_count
a = input("Enter a string")
print("The number of vowels: ", vowels(a))
