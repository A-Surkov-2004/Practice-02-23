import Data

data = Data.v

class Functions:
    def __init__(self):
        pass


    def search (self, message):
        # answers[i] = ans = [[Опред, ключ],[int]]
        answers = [int] * len(data)
        for i in range(len(data)):
            answers[i] = [data[i], 0]
        ls = message.text[len(message.text)-1]
        if(ls == '?' or ls == '.' or ls == '!' or ls == ','):
            question = message.text[:len(message.text) - 1].lower().split()
        else:
            question = message.text.lower().split()


        for word in question:
            for ans in answers:
                if ans[0] == ['','']:
                    break
                for kword in ans[0][1].split():
                    if kword == word:
                        ans[1] += 1

        def sort_key(array):
            return array[1]
        s = sorted(answers, key=sort_key, reverse=True)
        return(s[0][0][0])



