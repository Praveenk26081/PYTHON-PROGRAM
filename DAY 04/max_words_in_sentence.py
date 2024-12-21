sentences = ["alice and bob love apple", "i think so too", "this is great thanks very much"]
max_words = 0
for sentence in sentences:
    word_count = len(sentence.split())
    if word_count > max_words:
        max_words = word_count
print("Output:", max_words)
