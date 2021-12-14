# Tworzenie klasy
class String:
    # Zwykly konstruktor
    def __init__(self, string):
        self.string = string
    # Print nasz obiekt
    def __repr__(self):
        return 'Object: {}'.format(self.string)
    # Add, mozemy dzieki tej funkcji tak jakby
    #obslugiwac 'dodanie' do naszego obiektu
    def __add__(self, other):
        return self.string + other

# Driver Code
if __name__ == '__main__':
    # Korekcja obiektu
    string1 = String('Hello')
    # Printuj lokalizacje obiektu
    print(string1)
    # Polacz obiekt stringa z stringiem
    print(string1 + ' world')