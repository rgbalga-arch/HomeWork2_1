import json
from model import Model, PhoneAlreadyExists, WrongCommand, FileNotExist, PhoneNotExist
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def new_reg(self) -> None:

        while True:
            phone = self.view.ask_phone()
            try:
                if self.model.phone_exists(phone):
                    raise PhoneAlreadyExists
            except PhoneAlreadyExists as err:
                self.view.show_message(str(err))
                print(type(err).__name__)
                return
            name = self.view.ask_name()
            comment = self.view.ask_comment()

            phone_list = {"name" : name, "phone" : phone, "comment" : comment}
            try:
                self.model.add_contact(phone_list)
            except PhoneAlreadyExists as err:
                self.view.show_message(str(err))
                print(type(err).__name__)
                continue

            self.view.show_message("номер добавлен")
            break

    def see_all(self) -> None:
        try:
            print(self.model.read_contacts())
        except FileNotExist as err:
            self.view.show_message(str(err))
            print(type(err).__name__)

    def find_one(self) -> None:
            phone = self.view.ask_phone()

            try:
                print(self.model.find_contact(phone))
            except PhoneNotExist as err:
                self.view.show_message(str(err))
                print(type(err).__name__)

    def edit_one(self) -> None:
        """Управляет редактированием контакта."""
        phone = self.view.ask_phone()
        try:
            if not self.model.phone_exists(phone):
                raise PhoneNotExist()
        except PhoneNotExist as err:
            self.view.show_message(str(err))
            print(type(err).__name__)
            return
        new_name = self.view.new_name()
        new_phone = self.view.new_phone()
        new_comment = self.view.new_comment()
        """Запрашиваем новые данные только после проверки"""

        try:
            self.model.edit_contact(phone,new_name,new_phone,new_comment)
            self.view.show_message("Контакт сохранён.")

        except PhoneNotExist as err:
            self.view.show_message(str(err))
            print(type(err).__name__)

    def delete_one(self) -> None:
        phone = self.view.ask_phone()

        try:
            self.model.delete_contact(phone)
            self.view.show_message("Контакт удален")
        except PhoneNotExist as err:
            self.view.show_message(str(err))
            print(type(err).__name__)

    def start(self) -> None:
        while True:
            action = self.view.menu()

            try:
                if action == "1":
                    self.new_reg()
                elif action == "2":
                    self.see_all()
                elif action == "3":
                    self.find_one()
                elif action == "4":
                    self.edit_one()
                elif action == "5":
                    self.delete_one()
                else:
                    raise WrongCommand("Неверная команад")
            except WrongCommand as err:
                self.view.show_message(str(err))
                print(type(err).__name__)


