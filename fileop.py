filename = input("Enter the filename: ")
file = open(filename, "r")
text = ""
while True:
    line = file.readline()
    if not line:
        break
    text += line
file.close()

sentences = text.split('. ')
if sentences[-1] == '':
    sentences = sentences[:-1]


words = []
for i in range(len(sentences)):
    word1 = sentences[i].split(' ')
    words.append(word1)


words = [word for sentence in words for word in sentence]

def count_syllables(word):
    vowels = "aeiouy"
    word = word.lower()
    count = 0
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

sentence_count = len(sentences)
word_count = len(words) 
syllable_count = sum(count_syllables(word) for word in words)

average_sentence_length = word_count / sentence_count
average_word_length = syllable_count / word_count

flesch_index = 206.835 - (84.6 * (average_sentence_length / average_word_length))
grade_level_equivalent = 0.4 * (flesch_index + 84.6)

print("Word Count:", word_count)
print("Syllable Count:", syllable_count)
print("Flesch Index:", flesch_index)
print("Grade Level Equivalent:", grade_level_equivalent)
