#!/usr/bin/env python3

class Uzivatel:
    __minimalni_delka_hesla = 6
    __dalsi_id = 1

    def __init__(self, jmeno, heslo):
        self.jemno = jmeno
        self.heslo = heslo
        self.prihlaseny = False
        self.__id = Uzivatel.__dalsi_id
        Uzivatel.__dalsi_id += 1

    def prihlas_se(self, zadane_heslo):
        if self.heslo == zadane_heslo:
            self.prihlaseny = True
            return True
        else:
            return False  # hesla nesouhlasí

    def vrat_id(self):
        return self.__id

    @staticmethod
    def vrat_minimalni_delku_hesla_s():
        return Uzivatel.__minimalni_delka_hesla

    @classmethod
    def vrat_minimalni_delku_hesla_t(cls):
        return cls.__minimalni_delka_hesla

    @staticmethod
    def zvaliduj_heslo_s(heslo):
        if len(heslo) >= Uzivatel.__minimalni_delka_hesla:
            return True
        else:
            return False

    @classmethod
    def zvaliduj_heslo_t(cls, heslo):
        if len(heslo) >= cls.__minimalni_delka_hesla:
            return True
        else:
            return False

    # vytvoří aliasy pro funkce
    vrat_minimalni_delku_hesla = vrat_minimalni_delku_hesla_s
    zvaliduj_heslo = zvaliduj_heslo_s


class Trida:

    def nejaka_funkce():
        print("Tahle funkce je ve třídě!")

    def jina_funkce(text):
        print("Tahle funkce je také ve třídě!")
        print("Text je:", text)


u = Uzivatel("Tomáš Marný", "heslojeveslo")
print("ID prvního uživatele je:", u.vrat_id())
v = Uzivatel("Olí Znusinudle", "csfd1fg")
print("ID druhého uživatele je:", v.vrat_id())
print("Minimální délka hesla uživatele je:",
      Uzivatel.vrat_minimalni_delku_hesla())
print('Validnost hesla "heslo" je:',
      Uzivatel.zvaliduj_heslo("heslo"))

print("\n\n")
Trida.nejaka_funkce()
Trida.jina_funkce("parametr")
input()
