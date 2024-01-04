class CustomButton:

    def __init__(self, text, **kwargs):
        self.text = text
        self.config(**kwargs)

    def config(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def click(self):
        try:
            self.command()
        except AttributeError:
            print('Кнопка не настроена')
        except TypeError:
            print('Кнопка сломалась')

def func():
    print('Оно живое')

if __name__ == '__main__':
    btn = CustomButton(text="Hello", bd=20, bg='#ffaaaa')
    btn.click()
    btn.config(command=func)
    btn.click()