from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
import random
import os

class QuestionScreen(Screen):
    def __init__(self, question, options, image, correct_answer, **kwargs):
        super().__init__(**kwargs)
        self.question = question
        self.options = options
        self.image = image
        self.correct_answer = correct_answer
        self.selected_answer = None
        self.build_ui()

    def build_ui(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Проверка наличия файла изображения
        if os.path.exists(self.image):
            layout.add_widget(Image(source=self.image))
        else:
            layout.add_widget(Label(text="Image not found", halign='center'))
        
        layout.add_widget(Label(text=self.question, halign='center'))

        for option in self.options:
            btn = Button(text=option, size_hint_y=None, height=50)
            btn.bind(on_release=self.on_option_selected)
            layout.add_widget(btn)

        self.add_widget(layout)

    def on_option_selected(self, instance):
        self.selected_answer = instance.text
        if self.selected_answer == self.correct_answer:
            self.manager.current = 'result'
            self.manager.get_screen('result').update_result("Правильно!")
        else:
            self.manager.current = 'result'
            self.manager.get_screen('result').update_result("Неправильно!")

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text='', halign='center')
        layout = BoxLayout(orientation='vertical', padding=10)
        layout.add_widget(self.label)
        self.add_widget(layout)

    def update_result(self, result_text):
        self.label.text = result_text

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        questions = [
            {
                "question": "Какой вы цвет?",
                "options": ["Красный", "Синий", "Зеленый", "Желтый"],
                "image": "C:/Users/legos.sys/Desktop/imageformdk/question1.png",
                "correct_answer": "Красный"
            },
            {
                "question": "Какой вы цвет?",
                "options": ["Красный", "Синий", "Зеленый", "Желтый"],
                "image": "C:/Users/legos.sys/Desktop/imageformdk/question2.png",
                "correct_answer": "Синий"
            },
            {
                "question": "Какой вы цвет?",
                "options": ["Красный", "Синий", "Зеленый", "Желтый"],
                "image": "C:/Users/legos.sys/Desktop/imageformdk/question3.png",
                "correct_answer": "Зеленый"
            },
            {
                "question": "Какой вы цвет?",
                "options": ["Красный", "Синий", "Зеленый", "Желтый"],
                "image": "C:/Users/legos.sys/Desktop/imageformdk/question4.png",
                "correct_answer": "Желтый"
            },
            {
                "question": "Какой вы цвет?",
                "options": ["Красный", "Черный", "Зеленый", "Желтый"],
                "image": "C:/Users/legos.sys/Desktop/imageformdk/question5.png",
                "correct_answer": "Черный"
            },
            {
                "question": "Какой вы цвет?",
                "options": ["Красный", "Синий", "Белый", "Желтый"],
                "image": "C:/Users/legos.sys/Desktop/imageformdk/question6.png",
                "correct_answer": "Белый"
            },
            {
                "question": "Какой вы цвет?",
                "options": ["Красный", "Синий", "Розовый", "Желтый"],
                "image": "C:/Users/legos.sys/Desktop/imageformdk/question7.png",
                "correct_answer": "Розовый"
            },
            {
                "question": "Какой вы цвет?",
                "options": ["Фиолетовый", "Синий", "Зеленый", "Желтый"],
                "image": "C:/Users/legos.sys/Desktop/imageformdk/question8.png",
                "correct_answer": "Фиолетовый"
            },
             {
                "question": "Какой вы цвет?",
                "options": ["Красный", "Синий", "Серый", "Желтый"],
                "image": "C:/Users/legos.sys/Desktop/imageformdk/question9.png",
                "correct_answer": "Серый"
            },
            {
                "question": "Какой вы цвет?",
                "options": ["Красный", "Сизый", "Зеленый", "Желтый"],
                "image": "C:/Users/legos.sys/Desktop/imageformdk/question10.png",
                "correct_answer": "Сизый"
            },
            
        ]

        for i, q in enumerate(random.sample(questions, len(questions))):
            sm.add_widget(QuestionScreen(name=f'question{i}', question=q['question'], options=q['options'], image=q['image'], correct_answer=q['correct_answer']))

        sm.add_widget(ResultScreen(name='result'))
        return sm

if __name__ == '__main__':
    MyApp().run()
