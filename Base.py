
class Base:

    __slot__= ("__name", "__race", "__gender", "__level", "__totexp",
             "__curexp", "__stats", "__statsp")

    def __init__(self=None, name=None, race=None, gender=None):
        self.name = name
        self.race = race
        self.gender = gender
        self.__level = 0
        self.__totExp = 0
        self.__curExp = 0
        self.__nxtExp = 10
        self.__stats = {"Health": 1, "Attack": 1, "Defense": 1,
                      "Magic": 1, "Speed": 1}
        self.__statP = 5

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value is None:
            raise ValueError("Please, insert a name")
        elif type(value) is not str:
            raise TypeError("Please, make sure that name is a string")
        elif len(value) > 10:
            raise ValueError("Make sure the name is no longer than 10 characters")
        self.__name = value

    @property
    def race(self):
        return self.__race

    @race.setter
    def race(self, value):
        if value is None:
            raise ValueError("Please, make sure to select 1 of the valid races: Human, Elf, Dwarf, Hobbit, Orc or Slime")
        elif type(value) is not str:
            raise TypeError("Make sure the race is a string")
        if value in("Human", "Elf", "Orc", "Hobbit", "Dwarf", "Slime"):
            self.__race = value
        else:
            raise ValueError("Please, make sure to select 1 of the valid races: Human, Elf, Dwarf, Hobbit, Orc or Slime")

    @property
    def gender(self):
        return self.__gender
    
    @gender.setter
    def gender(self, value):
        if value is None:
            raise ValueError("Please, make sure to input a valid gender: Male, Female, Apache")
        elif type(value) is not str:
            raise TypeError("Please make sure the gender is a string")
        if value in ("Male", "Female", "Apache"):
            self.__gender = value
        else:
            raise ValueError("Make sure to pick 1 of the 3 valid genders: Male, Female, Apache")

    def GainExp(self, value):
        if type(value) is not int:
            raise TypeError("Invalid experience gained")
        self.__totExp += value
        self.__curExp += value
        if self.__curExp > self.__nxtExp:
            self.LevelUp()

    def LevelUp(self):
        self.__curExp = self.__curExp - self.__nxtExp
        self.__nxtExp += (self.__nxtExp / 2) 
        self.__level += 1
        self.__statP += 5
        print("Yey! Level Up!")

    def Death(self):
        self.__totExp -= (self.__curExp / 2)
        self.__curExp -= (self.__curExp / 2)
        print("Git gud, casul")

    def IncreaseStats(self, **kwargs):
        for value in kwargs.values():
            if type(value) is not int:
                raise ValueError("Make sure to enter a proper value for the stat")
        if sum(kwargs) > self.__statP:
            raise ValueError("Please, make sure you have enough stat points")
        self.__stats.update(kwargs)
        self.__statP = self.__statP - sum(kwargs)
