# 1 Напишите 2-мя способами генератор который принимает список
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] и
# возвращает новый список только с положительными
# числами с обработкой исключений.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_numbers1 = [num for num in numbers if num > 0]
print(positive_numbers1)


def positive_numbers2(list_numbers):
    for num in list_numbers:
        try:
            if num > 0:
                yield num
        except TypeError:
            print(
                f"Входные данные содержат нечисловые значения. "
                f"Будут выведены только числовые значения."
            )


print(list(positive_numbers2([34.6, -203.4, 44.9, 68.3, -12.2, 44.6, "df"])))

# 2 Необходимо составить список чисел которые
# указывают на длину слов в строке: sentence = " thequick
# brown fox jumps over the lazy dog", но только если слово
# не "the" с обработкой исключений


sentence = "thequick brown fox jumps over the lazy dog"
words = sentence.split(" ")
len_sentence1 = [len(words) for words in words if words != "the"]
print(len_sentence1)

len_sentence2 = []
for i in words:
    if i != "the":
        try:
            len_sentence2.append(len(i))
        except:
            pass
print(len_sentence2)


def len_sentence3(sentence):
    for word in sentence.split(" "):
        try:
            if word != "the":
                yield len(word)
        except:
            pass


print(list(len_sentence3("thequick brown fox jumps over the lazy dog")))
