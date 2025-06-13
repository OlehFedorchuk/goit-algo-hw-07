class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        if isinstance(reply, Comment):
            self.replies.append(reply)

    def remove_reply(self):
        # Позначаємо коментар як видалений
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, indent=0):
        prefix = " " * indent
        if self.is_deleted:
            print(f"{prefix}{self.text}")
        else:
            print(f"{prefix}{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(indent + 4)
# Основний коментар
root_comment = Comment("Яка чудова книга!", "Бодя")

# Перший рівень відповідей
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

# Додаємо відповіді до головного коментаря
root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

# Відповідь на перший коментар
reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

# Видаляємо коментар Андрія (reply1)
reply1.remove_reply()

# Виводимо ієрархію
root_comment.display()