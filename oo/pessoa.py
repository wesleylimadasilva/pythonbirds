class Pessoa:
    def __init__(self, *filhos, nome=None, idade=27):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá {self.nome}"

if __name__ == '__main__':
    filho1 = Pessoa(nome="Fulano")
    filho2 = Pessoa(nome="Sicrano")
    maria = Pessoa(filho1,nome="Maria")
    maria.filhos.append(filho2)
    print(maria.nome)
    print(filho1.nome)
    for filho in maria.filhos:
        print(f"{filho.nome} é filho de {maria.nome}")