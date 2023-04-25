def make_snippet(string):
    words = string.split()
    word_count = len(words)
    preview = ' '.join(words[0:5]) + ' ...'
    if word_count > 5:
        return preview
    else: return string

# 02_test_drive_a_single_function.md
# Challenge

def count_words(string):
    words = string.split()
    word_count = len(words)
    return word_count



