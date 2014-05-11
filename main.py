import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.properties import NumericProperty,StringProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import *
from random import random
from kivy.storage.jsonstore import JsonStore

class EduAppScreen(FloatLayout):
    label_text = StringProperty('Start The Game')
    btn_text1 = StringProperty('Start')
    btn_text2 = StringProperty('Start')
    btn_text3 = StringProperty('Start')
    btn_text4 = StringProperty('Start')
    question_text = StringProperty('Hi')
    scores = NumericProperty(0)
    solution_result = NumericProperty(0)
    def __init__(self, **kwargs):
        super(EduAppScreen, self).__init__(**kwargs)

    def change_text(self):
        question_text= self.gen_question_text()
        self.label_text = 'Scores: ' + str(self.update_score(0)) + '\n' + question_text
        correct_position = int(random()*3)
        print 'correct_position: '
        print correct_position
        if correct_position == 0:
           self.btn_text1 = self.change_solution_text('result')
        else:
           self.btn_text1 = self.change_solution_text('f1')
        if correct_position == 1:
           self.btn_text2 = self.change_solution_text('result')
        else:
           self.btn_text2 = self.change_solution_text('f2')
        if correct_position == 2:
           self.btn_text3 = self.change_solution_text('result')
        else:
           self.btn_text3 = self.change_solution_text('f3')
        if correct_position == 3:
           self.btn_text4 = self.change_solution_text('result')
        else:
           self.btn_text4 = self.change_solution_text('f4')
         
        return self.label_text
 
    def set_solution_value(self,value):
        solution_result = value
        return solution_result 

    def update_score(self,value):
        self.scores = self.scores + value
        return self.scores

    def save_values(self,value1,value2,rsvalue):
        store = JsonStore('result.json')
        store['first'] = {'first': value1}
        store['second'] = {'second': value2}
        store['result'] = {'result': rsvalue}
        store['f1'] = {'f1': rsvalue + int(random()*20) + 1}
        store['f2'] = {'f2': rsvalue - int(random()*20) - 1}
        store['f3'] = {'f3': rsvalue * int(random()*20) + 20}
        store['f4'] = {'f4': rsvalue - int(random()*25) - 1}
        print(store.get('first'))
        print(store.get('second'))
        print(store.get('result'))

    def gen_question_text(self):
        firstvalue = int(round(random()*100))
        secondvalue = int(round(random()*100))
        result = firstvalue + secondvalue
        question_text = str(firstvalue) + '+' + str(secondvalue) + '= ?'
        self.save_values(firstvalue,secondvalue,result)
        return question_text

    def change_solution_text(self,value): 
        store = JsonStore('result.json')
        value = store.get(value).values().pop()
        #print value
        result = self.set_solution_value(value)
        self.btn_text = str(result)
        return self.btn_text

    def check_btn_solution(self,value):
        store = JsonStore('result.json')
        jsonvalue = store.get('result').values().pop()
        value = int(value)
        #print ('value=',type(value), type(jsonvalue))
        if value == jsonvalue:
           #print 'its correct! change text and need to update score! +2'
           self.update_score(2)
           self.change_text()
        #else:
           #print 'here is something wrong'
           
        return self.btn_text

    def check_solution(self,value):
        if self.btn_text1 == 'Start':
           self.change_text()         
        else:
           if value == 1:
              self.check_btn_solution(self.btn_text1)
           if value == 2:
              self.check_btn_solution(self.btn_text2)
           if value == 3:
              self.check_btn_solution(self.btn_text3)
           if value == 4:
              self.check_btn_solution(self.btn_text4)

class EduApp(App):
    
    def build(self):
        return EduAppScreen() 
             
if __name__ == '__main__':
    EduApp().run()
