from random import choice


def first(event, resp, greeting=False):
    resp = resp
    buttons = [
        {
            "title": "1",
            "hide": "true"
        },
        {
            "title": "2",
            "hide": "true"
        },
        {
            "title": "3",
            "hide": "true"
        },
        {
            "title": "4",
            "hide": "true"
        },
        {
            "title": "5",
            "hide": "true"
        },
    ]
    resp["response"]["buttons"].extend(buttons)
    resp["session_state"]["last_step"] = 1
    resp["response"]["text"] = choice(['Привет. Выберите уровень сложности от 1 до 5.',
                                       'Рад встрече! Выберите уровень сложности от 1 до 5.',
                                       'Здравствуйте. Выберите уровень сложности от 1 до 5.'])

    if "last_step" in event["state"]["session"] and event["state"]["session"]["last_step"] == 0 or greeting:
        resp["response"]["text"] = 'Выберите уровень сложности от 1 до 5.'
    return resp


def second(event, resp):
    resp = resp
    resp["response"]["buttons"].append({
        "title": "Да",
        "hide": "true"
    })
    if event["request"]["original_utterance"] in ["1", "2", "3", "4", "5",
                                                  "один", "два", "три", "четыре", "пять"]:
        resp["session_state"]["last_step"] = 2
        if event["request"]["original_utterance"] in ["1", "2", "3", "4", "5"]:
            resp["session_state"]["level"] = int(event["request"]["original_utterance"])
        if event["request"]["original_utterance"] in ["один", "два", "три", "четыре", "пять"]:
            nums = {"один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5}
            resp["session_state"]["level"] = nums[event["request"]["original_utterance"]]
        resp["response"]["text"] = choice(["Готовы слушать?", "Готовы?"])

    elif event["state"]["session"]["level"] != 0:
        resp["session_state"]["last_step"] = 2
        resp["response"]["text"] = choice(["Готовы слушать?", "Готовы?"])

    else:
        resp["response"]["text"] = choice(["Извините, я вас не понимаю.",
                                           "Без понятия, о чем вы...", "Ничего не понял"])
    return resp


class Alisa_skill:
    def __init__(self, event, context):
        all_words = {"яблоко": ['<speaker audio="dialogs-upload/'
                                'c75c9aa1-a26b-4466-9a1a-b4ae0793ea0e/f50afdb4-4550-432c-96c6-71ae6e4cb623.opus">',
                                '<speaker audio="dialogs-upload/'
                                'c75c9aa1-a26b-4466-9a1a-b4ae0793ea0e/72a279a2-06f2-40ec-83dc-e40b99951291.opus">',
                                '<speaker audio="dialogs-upload/'
                                'c75c9aa1-a26b-4466-9a1a-b4ae0793ea0e/f0b48f44-484f-4fff-9f8f-a8dbbeef4da6.opus">',
                                '<speaker audio="dialogs-upload/'
                                'c75c9aa1-a26b-4466-9a1a-b4ae0793ea0e/ebfa08e1-3a27-4c5b-a716-bb2ec2b63ed3.opus">',
                                '<speaker audio="dialogs-upload/'
                                'c75c9aa1-a26b-4466-9a1a-b4ae0793ea0e/c2494e3b-3552-4410-ab67-33a4a14cb862.opus">'],
                     "галактика": ['<speaker audio="dialogs-upload/'
                                   'c75c9aa1-a26b-4466-9a1a-b4ae0793ea0e/f5af47ab-8a76-41c5-b075-c6e1adccd25f.opus">',
                                   '<speaker audio="dialogs-upload/'
                                   'c75c9aa1-a26b-4466-9a1a-b4ae0793ea0e/a4b52d08-38b8-4914-9fdf-8d56fa15f652.opus">',
                                   '<speaker audio="dialogs-upload/'
                                   'c75c9aa1-a26b-4466-9a1a-b4ae0793ea0e/f7aa354d-825f-46c3-b7c9-1c694438f541.opus">',
                                   '<speaker audio="dialogs-upload/'
                                   'c75c9aa1-a26b-4466-9a1a-b4ae0793ea0e/46652fdf-7992-44ab-9cfa-104752bac382.opus">',
                                   '<speaker audio="dialogs-upload/'
                                   'c75c9aa1-a26b-4466-9a1a-b4ae0793ea0e/7e70c83f-e61f-4560-85bd-e95335c5d8d0.opus">']}

        last_step = 0
        if "last_step" in event["state"]["session"]:
            last_step = event["state"]["session"]["last_step"]
        level = 0
        if "level" in event["state"]["session"]:
            level = event["state"]["session"]["level"]
        help = "false"
        if "help" in event["state"]["session"]:
            help = event["state"]["session"]["help"]
        words_used = []
        if "words_used" in event["state"]["session"]:
            words_used = event["state"]["session"]["words_used"]
        new_word = "true"
        if "new_word" in event["state"]["session"]:
            new_word = event["state"]["session"]["new_word"]

        resp = {
            "version": event["version"],
            "session": event["session"],
            "response": {
                "text": "Ошибка",
                "end_session": "false",
                "buttons": [
                    {
                        "title": "Помощь",
                        "hide": "true"
                    },
                    {
                        "title": "Что ты умеешь?",
                        "hide": "true"
                    },
                    {
                        "title": "Выход",
                        "hide": "true"
                    }
                ]
            },
            "session_state": {
                "last_step": last_step,
                "help": help,
                "level": level,
                "words_used": words_used,
                "new_word": new_word
            }
        }

        if "help" in event["state"]["session"] and event["state"]["session"]["help"] == "true":
            if event["request"]["original_utterance"].lower() in ["да", "ок", "хорошо", "давай", "ага", "продолжим"]:
                resp["session_state"]["help"] = "false"
                event["state"]["session"]["help"] = "false"
            else:
                resp["response"]["buttons"].append({
                    "title": "Да",
                    "hide": "true"
                })
                resp["response"]["text"] = choice(["Извините, я вас не понимаю. Вы хотите продолжить?",
                                                   "Ничего не понятно, но очень интересно", "Без понятия, о чем вы"])

        if event["session"]["new"] or \
                (event["state"]["session"]["last_step"] == 0 and event["state"]["session"]["help"] == "false"):
            resp = first(event, resp)

        else:
            if event["state"]["session"]["last_step"] == 1 and event["state"]["session"]["help"] == "false":
                resp = second(event, resp)

            elif event["state"]["session"]["last_step"] == 2 and event["state"]["session"]["help"] == "false":
                if event["request"]["original_utterance"].lower() in ["да", "ок", "хорошо", "давай", "ага"]:
                    resp["session_state"]["last_step"] = 3
                    if event["state"]["session"]["new_word"] == "false":
                        word = event["state"]["session"]["words_used"][-1]
                        resp["session_state"]["new_word"] = "true"
                    else:
                        word = choice(list(all_words.keys()))
                        words_used.append(word)
                    resp["response"]["tts"] = all_words[word][event["state"]["session"]["level"] - 1]
                    resp["response"]["text"] = choice(["Что я сказал?", "Повтори", "Что это за слово?"])

                else:
                    resp["response"]["text"] = choice(["Извините, я вас не понимаю. Вы готовы слушать?",
                                                       "Без понятия, о чем вы...", "Ничего не понял"])

            elif event["state"]["session"]["last_step"] == 3 and event["state"]["session"]["help"] == "false":
                buttons = [
                    {
                        "title": "Повтори",
                        "hide": "true"
                    },
                    {
                        "title": "Дальше",
                        "hide": "true"
                    },
                    {
                        "title": "Изменить уровень сложности",
                        "hide": "true"
                    }
                ]
                resp["response"]["buttons"].extend(buttons)
                resp["session_state"]["last_step"] = 5
                if event["state"]["session"]["words_used"][-1] == event["request"]["original_utterance"].lower():
                    resp["response"]["text"] = choice(["Молодец", "Правильно", "Так точно!"])

                else:
                    resp["response"]["text"] = choice(["Попробуй ещё раз", "Неправильно", "Это не то слово"])

            elif event["state"]["session"]["last_step"] == 4 and event["state"]["session"]["help"] == "false":
                buttons = [
                    {
                        "title": "Повтори",
                        "hide": "true"
                    },
                    {
                        "title": "Дальше",
                        "hide": "true"
                    },
                    {
                        "title": "Изменить уровень сложности",
                        "hide": "true"
                    }
                ]
                resp["response"]["buttons"].extend(buttons)
                resp["session_state"]["last_step"] = 5
                resp["response"]["text"] = "Вы можете попросить повторить слово, прослушать " \
                                           "следующее слово и изменить уровень сложности"

            elif event["state"]["session"]["last_step"] == 5 and event["state"]["session"]["help"] == "false":
                resp["response"]["text"] = "Вы можете попросить повторить слово, прослушать " \
                                           "следующее слово и изменить уровень сложности"

        if event["request"]["command"].lower() == "помощь":
            if "Да" not in resp["response"]["buttons"][-1]["title"]:
                resp["response"]["buttons"] = [
                    {
                        "title": "Помощь",
                        "hide": "true"
                    },
                    {
                        "title": "Что ты умеешь?",
                        "hide": "true"
                    },
                    {
                        "title": "Выход",
                        "hide": "true"
                    },
                    {
                        "title": "Да",
                        "hide": "true"
                    }
                ]
            resp["response"]["text"] = 'Что-бы проиграть запись еще раз скажите "повтори".\n' \
                                       'Что-бы изменить уровень сложности скажите "измени уровень сложности"\n' \
                                       'Что-бы заменить слово скажите "давай другое слово"\n' \
                                       'Вы также можете обратится к команде "что ты умеешь"\n' \
                                       'Продолжим игру?'
            if resp["session_state"]["last_step"] > 0 and resp["session_state"]["help"] == "false":
                resp["session_state"]["last_step"] -= 1
            resp["session_state"]["help"] = "true"

        if event["request"]["command"].lower() == "что ты умеешь":
            if "Да" not in resp["response"]["buttons"][-1]["title"]:
                resp["response"]["buttons"] = [
                    {
                        "title": "Помощь",
                        "hide": "true"
                    },
                    {
                        "title": "Что ты умеешь?",
                        "hide": "true"
                    },
                    {
                        "title": "Выход",
                        "hide": "true"
                    },
                    {
                        "title": "Да",
                        "hide": "true"
                    }
                ]
            resp["response"]["text"] = 'Я умею говорить слова с разными уровнями помех.' \
                                       'С пятым уровнем слово с самыми большими помехами,' \
                                       'а с уровнем помех один слово производится без них.' \
                                       'Продолжим игру?'
            if resp["session_state"]["last_step"] > 0 and resp["session_state"]["help"] == "false":
                resp["session_state"]["last_step"] -= 1
            resp["session_state"]["help"] = "true"

        if event["request"]["command"].lower() == "выход":
            resp["response"]["end_session"] = "true"
            resp["response"]["text"] = choice(["До встречи", "До свидания", "Пока", "Ещё увидимся"])
            return resp

        if event["request"]["command"] == "1" and event["state"]["session"]["last_step"] == 1:
            resp["session_state"]["last_step"] = 2
            resp["session_state"]["level"] = 1
        if event["request"]["command"] == "2" and event["state"]["session"]["last_step"] == 1:
            resp["session_state"]["last_step"] = 2
            resp["session_state"]["level"] = 2
        if event["request"]["command"] == "3" and event["state"]["session"]["last_step"] == 1:
            resp["session_state"]["last_step"] = 2
            resp["session_state"]["level"] = 3
        if event["request"]["command"] == "4" and event["state"]["session"]["last_step"] == 1:
            resp["session_state"]["last_step"] = 2
            resp["session_state"]["level"] = 4
        if event["request"]["command"] == "5" and event["state"]["session"]["last_step"] == 1:
            resp["session_state"]["last_step"] = 2
            resp["session_state"]["level"] = 5

        if event["request"]["command"].lower() == "да" and event["state"]["session"]["last_step"] == 2:
            if event["state"]["session"]["new_word"] == "false":
                word = event["state"]["session"]["words_used"][-1]
                resp["session_state"]["new_word"] = "true"
            else:
                word = choice(list(all_words.keys()))
                words_used.append(word)
            resp["response"]["tts"] = all_words[word][event["state"]["session"]["level"] - 1]
            resp["response"]["text"] = choice(["Что я сказал?", "Повтори", "Что это за слово?"])

        if event["request"]["command"] == "повтори" and event["state"]["session"]["last_step"] in [4, 5]:
            resp["session_state"]["new_word"] = "false"
            resp = second(event, resp)
        if event["request"]["command"] == "дальше" and event["state"]["session"]["last_step"] in [4, 5]:
            resp = second(event, resp)
        if event["request"]["command"] == "изменить уровень сложности" and event["state"]["session"]["last_step"] in [4,
                                                                                                                      5]:
            resp["session_state"]["last_step"] = 0
            resp = first(event, resp, True)

        if event["request"]["command"].lower() == "да" and event["state"]["session"]["help"] == "true":
            resp["session_state"]["help"] = "false"
            event["state"]["session"]["help"] = "false"

        self.resp = resp

    def resp(self):
        return self.resp
