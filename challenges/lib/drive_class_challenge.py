import math

class GrammarStats:
    def __init__(self):
        self.words_checked = []
 
    def check(self, text):
        if text == '':
            raise Exception('No text given')
        # elif text[0].islower() and text[-1] not in '.!?':
        #     self.progress = 0
        # elif text[0].islower() or text[-1] not in '.!?':
        #     self.progress = 50
        else:
            #self.progress = 100
                result = text[0].isupper() and text[-1] in '.!?'
                self.words_checked.append(result)
                return result

        #return False
    
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
  
    def percentage_good(self):
        if len(self.words_checked) == 0:
             raise Exception('N/A')
        else:
            self.correct = self.words_checked.count(True)
            self.incorrect = self.words_checked.count(False)
            self.progress = self.correct / (self.correct + self.incorrect) * 100
            return f"{math.floor(self.progress)}%"
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.