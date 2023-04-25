def manage_reading_time(wpm, text):
    words = text.split()
    word_count = len(words)
    reading_time = word_count / wpm
    if reading_time < 1:
        return 1
    else: return reading_time