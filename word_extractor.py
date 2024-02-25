import os

output_folder = "txt files"
letters = int(input("\nHow long should the words be in letters?\nType in the number >> "))

os.makedirs(output_folder, exist_ok=True)

with open("dict.txt", "r") as input_dictionary:
    words = input_dictionary.read().lower().split()

long_words = [word for word in words if len(word) == letters]

output_file_path = os.path.join(output_folder, str(letters) + "-letter-words.txt")

with open(output_file_path, "w") as output_dictionary:
    output_dictionary.write("\n".join(long_words))

print("Script is executed.")