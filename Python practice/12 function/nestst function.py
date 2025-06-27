def greet(lang):
    def eng():
        return "Hello " + lang

    def ban():
        return "Hello " + lang

    if lang == "en":
        return eng()
    else:
        return ban()


s = greet("en")
print(s)