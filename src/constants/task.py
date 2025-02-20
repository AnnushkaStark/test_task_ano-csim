import enum


class TaskStatus(enum.StrEnum):
    CREATED = "Создана"
    IN_PROGRESS = "В процессе"
    DONE = "Завершена успешно"
    ERROR = "Ошибка"
