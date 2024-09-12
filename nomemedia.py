class Aluno:
    def __init__(self):
        self.__nome = None
        self.__nota1 = None
        self.__nota2 = None

    def set_nome(self, nome):
        self.__nome = nome

    def set_nota1(self, nota1):
        self.__nota1 = nota1

    def set_nota2(self, nota2):
        self.__nota2 = nota2

    def get_nome(self):
        return self.__nome

    def get_nota1(self):
        return self.__nota1

    def get_nota2(self):
        return self.__nota2

    def calcular_media(self):
        return (self.__nota1 + self.__nota2) / 2

    def exibir_informacoes(self):
        media = self.calcular_media()
        print(f"aluno: {self.__nome}, media: {media:.2f}")


def main():
    aluno = Aluno()

    nome = input("digite seu nome: ")
    aluno.set_nome(nome)

    nota1 = float(input("digite a primeira nota: "))
    aluno.set_nota1(nota1)

    nota2 = float(input("digite a segunda nota: "))
    aluno.set_nota2(nota2)

    aluno.exibir_informacoes()

if __name__ == "__main__":
    main()