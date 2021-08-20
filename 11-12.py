class Dessert:
    def __init__(self,name='',calories=0):
        self.__name = name
        self.__calories = calories
    def get_name(self):
        return self.__name
    def get_calories(self):
        return self.__calories
    def set_name(self,name):
        self.__name = name
    def set_calories(self,calories):
        self.__calories = calories
    def is_healthy(self):
        if(self.__calories<200): return True
        return False
    def is_delicious(self):
        return True
    def __str__(self):
        return f'name: {self.__name}, calories: {self.__calories}'
class JellyBean(Dessert):
    def __init__(self, name='', calories=0, flavor=''):
        super(JellyBean, self).__init__(name, calories)
        self.__flavor = flavor
    def __str__(self):
        return super(JellyBean, self).__str__()+f', flavor: {self.__flavor}'
    def get_flavor(self):
        return self.__flavor
    def set_flavor(self,flavor):
        self.__flavor = flavor
    def is_delicious(self):
        if self.__flavor == 'black licorice': return False
        return True


des = Dessert('Мороженка', 100)
d = JellyBean('Мармелад', 150 , 'black licorice')
print(d)
print(d.get_name())
print(d.is_delicious())
