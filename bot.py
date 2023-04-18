from keyboard import sender
import main


for event in main.bot.longpoll.listen():
    if event.type == main.VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text.lower()
        user_id = str(event.user_id)
        msg = event.text.lower()
        sender(user_id, msg.lower())
        if request == 'начать поиск':
            main.creating_database()
            main.bot.write_msg(user_id, f'Привет, {main.bot.name(user_id)}')
            main.bot.find_user(user_id)
            main.bot.write_msg(event.user_id, f'Нашёл для тебя пару, что бы продолжить нажми "Далее..."')
            main.bot.find_persons(user_id, main.offset)

        elif request == 'далее...':
            for i in main.line:
                main.offset += 1
                main.bot.find_persons(user_id, main.offset)
                break

        else:
            main.bot.write_msg(event.user_id, 'Собщение не распознано, используй кнопки управления')
