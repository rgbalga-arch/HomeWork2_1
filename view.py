from model import OnlyNumbersError, PhoneAlreadyExists
class View:

    def menu(self) ->str:
        print("1 - чтобы добавить контакт")
        print("2 - чтобы посмотреть все контакты")
        print("3 - чтобы найти контакт")
        print("4 - чтобы изменить контакт")
        print("5 - чтобы удалить контакт")

        action_menu = input("Выберите действие: ")
        return action_menu

    def ask_name(self) ->str:
        name = input("Введите имя ")
        return name

    def ask_phone(self) ->int:
        while True:
            try:
                phone = int(input("Введите номер телефона "))
                return phone
            except ValueError as err:
                self.show_message("Введите только цифры")
                print(type(err).__name__)

    def ask_comment(self) ->str:
        comment = input("Напишиет коментарий ")
        return comment

    def show_message(self, message: str) -> None:
        print(message)

    def new_name(self) -> str:
        new_name: str = input("Введите новое имя: ")
        return new_name

    def new_phone(self) -> int:
        while True:
            try:
                new_phone = int(input("Введите новый номер телефона "))
                return new_phone
            except ValueError as err:
                self.show_message("Введите только цифры")
                print(type(err).__name__)

    def new_comment(self) -> str:
        new_comment: str = input("Введите новый комментарий: ")
        return new_comment
