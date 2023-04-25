def check_grammar(text):
    def check_capital(text):
        first_letter = text[0]
        upper_case = first_letter.upper()
        if first_letter == upper_case:
            return True
        else: return False
    
    def check_punctuation(text):
        last_char = text[-1]
        punctuation = ['.', '!', '?']
        #if any(char in punctuation for char in last_char):
        if last_char in punctuation:
            return True
        else: return False
    
    if check_capital(text) and check_punctuation(text):
        return True
    else: return False