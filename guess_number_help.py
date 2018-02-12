"""
A class for creating random numbers and comparing numbers.
Класс для cоздания случайных чисел и сравнения чисел.
Программа guess_number.py
"""

from random import sample


class CheckingNumbers():

    def __init__(self,length_number):
        
        self.length_number = length_number
        self.coined_number = sample(range(10) , length_number)
        self.input_number = []
        self.guessed = 0
        self.place = 0
    
    
    def isint(self, str_number):
        """
        Function of definition of an integer
        Функция определения целого числа
        """
        try:
            int(str_number)
            return True
        except ValueError:
            return False

    def check_number(self, str_number):
        """
        The function checks the number and returns the result of the test.
        Функция проверяет число и возвращает результат проверки
        """
        
        if not self.isint(str_number) or len(str_number) != self.length_number:
            return False
        # Convert a string to a list number
        # Преобразование строки в список чисел
        self.input_number = [int(i) for i in str_number]
        for z in self.input_number:
            if self.input_number.count(z) > 1 :
                return False
        self.guessed = 0
        self.place = 0
        # Calculating matches
        # Вычисление совпадений
        for i in range(self.length_number):
            for j in range(self.length_number):
                if  self.coined_number[i] == self.input_number[j]:
                    self.guessed +=1
                    if i == j :
                        self.place +=1
        # Verification of victory
        # Проверка победы
        if self.guessed == self.length_number and self.place == self.length_number:
            return True
        return [self.guessed, self.place]
