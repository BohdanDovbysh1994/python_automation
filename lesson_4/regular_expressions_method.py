# text = "john marta james Morgan Adam Maria huang"
#
# names = text.split(' ')
# updated_names = []
# for name in names:
#     updated_names.append(name.title())
#
# print(updated_names)
# text = " ".join(updated_names)
# print(text)


# friends = ["John", "Marta", "James", "Amanda", "Marianna"]
#
# for friend in friends:
#     print(friend.rjust(10))


# query_string = "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             "
#
# query_string = query_string.strip()
# params = query_string.split('&')
# pairs = {}
#
# for param in params:
#     if param:
#         key, value = param.split('=', maxsplit=1)
#         pairs[key] = value
#
# print(pairs)
import re

# camel_case_names = ["FirstItem", "FriendsList", "MyTuple"]
# snake_case_names = []
#
# for name in camel_case_names:
#     some = re.sub(r"([A-Z][a-z]+)([A-Z][a-z]+)", r"\1_\2", name).lower()
#     print(some)


# text = """Многие думают, что Lorem Ipsum - взятый с потолка псевдо-латинский набор слов, но это не совсем так.
# Его корни уходят в один фрагмент классической латыни 45 года н.э., то есть более двух тысячелетий назад.
# Ричард МакКлинток, профессор латыни из колледжа Hampden-Sydney, штат Вирджиния, взял одно из самых странных слов в Lorem Ipsum, "consectetur", и занялся его поисками в классической латинской литературе. В результате он нашёл неоспоримый первоисточник Lorem Ipsum в разделах 1.10.32 и 1.10.33 книги "de Finibus Bonorum et Malorum" ("О пределах добра и зла"), написанной Цицероном в 45 году н.э. Этот трактат по теории этики был очень популярен в эпоху Возрождения.
# Первая строка Lorem Ipsum, "Lorem ipsum dolor sit amet..", происходит от одной из строк в разделе 1.10.32."""
#
# sentences = re.findall(r"^[А-Я].+\.$", text)
# print(sentences)