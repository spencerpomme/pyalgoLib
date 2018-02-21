class Dog:
    def __init__(self, name):
        self.name = name
    @staticmethod
    def __naming(name):
        return name.upper()
    def __str__(self):
        return self.name



if __name__ == "__main__":
    d = Dog('jack')
    print(d)
