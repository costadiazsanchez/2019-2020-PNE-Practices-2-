class Seq:
    def __init__(self, strbases):
        base = ["A", 'C', 'G', 'T']
        if strbases == '':
            print("NULL SEQUENCE.")
            self.strbases = 'NULL!'
        else:
            for i in strbases:
                if i not in base:
                    print("Invalid!")
                    self.strbases = "ERROR!"
                    return
            self.strbases = strbases
            print("New sequence created.")


    def __str__(self):
        return self.strbases

    def len(self):
        base = ["A", 'C', 'G', 'T']
        for element in self.strbases:
            if element not in base:
                return 0
        return len(self.strbases)


