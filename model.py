import json
from pathlib import Path

contacts_path = Path("contacts.json")

class AppError(Exception):
    """Базовая ошибка приложения."""
    pass


class UserError(AppError):
    """Базовая ошибка, связанная с пользователем."""
    pass


class PhoneAlreadyExists(UserError):
    """Ошибка: такой номер телефона уже существует."""
    pass


class OnlyNumbersError(AppError):
    """Ошибка: номер телефона должен содержать только цифры."""
    pass


class FileNotExist(AppError):
    """ошибка: файл не существует"""
    pass


class PhoneNotExist(UserError):
    """Ошибка: телефон не найден"""
    pass


class WrongCommand(AppError):
    pass


class Model:
    def load_contacts(self) -> list[dict]:
        contacts = []
        with open(contacts_path, "r", encoding="UTF-8") as contacts_file:
            for line in contacts_file:
                contact = json.loads(line)
                contacts.append(contact)
        return contacts

    def save_contacts(self, contacts: list[dict]) -> None:
        with open(contacts_path, "w", encoding="UTF-8") as contacts_file:
            for contact in contacts:
                json.dump(contact, contacts_file, ensure_ascii=False)
                contacts_file.write("\n")

    def new_reg(self) -> list[dict]:
        contacts: list[dict] = []
        """Создаём список для хранения существующих контактов."""

        if contacts_path.exists():
            """Проверяем, существует ли файл с контактами"""
            contacts = self.load_contacts()
        return contacts

    def phone_exists(self, phone: int) -> bool:
        """Проверяет, существует ли контакт с таким номером."""
        contacts = self.load_contacts()
        for contact in contacts:
            if contact["phone"] == phone:
                return True

        return False

    def add_contact(self, phone_list: dict) -> None:
        """Добавляет контакт в файл."""
        if self.phone_exists(phone_list["phone"]):
            raise PhoneAlreadyExists("Такой номер уже существует")

        with open(contacts_path, "a", encoding="UTF-8") as contacts_file:
            json.dump(phone_list, contacts_file, ensure_ascii=False)
            contacts_file.write("\n")

    def read_contacts(self) -> dict:
        contacts = self.load_contacts()
        if not contacts_path.exists():
            raise FileNotExist("файл не найден")
        print(json.dumps(contacts, indent=4))

    def find_contact(self, phone: int) -> dict:
        contacts = self.load_contacts()
        for contact in contacts:
            if contact["phone"] == phone:
                return contact
        raise PhoneNotExist("Номер не найден")

    def edit_contact(self,phone: int,new_name: str,new_phone: int,new_comment: str) -> None:
        """Изменяет контакт и сохраняет изменения в файл."""
        contacts = self.load_contacts()

        for contact in contacts:
            if phone == contact["phone"]:
                """Ищем контакт по старому номеру"""
                contact["name"] = new_name
                contact["phone"] = new_phone
                contact["comment"] = new_comment
                break
        else:
            raise PhoneNotExist("Телефон не найден")

        try:
            self.save_contacts(contacts)
            """Сохраняем все контакты обратно в файл"""
        finally:
            pass

    def delete_contact(self, phone: int) -> None:
        """Изменяет контакт и сохраняет изменения в файл."""
        contacts = self.load_contacts()

        for contact in contacts:
            if contact["phone"] == phone:
                """Ищем контакт по старому номеру"""
                contacts.remove(contact)
                break
        else:
            raise PhoneNotExist("Телефон не найден")

        try:
            self.save_contacts(contacts)
            """Сохраняем все контакты обратно в файл"""
        finally:
            pass


