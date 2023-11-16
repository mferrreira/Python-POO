class Camera:

    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando')
            return 
        
        print(f'{self.nome} está filmando')
        self.filmando = True
    
    def para_de_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando')
        
        self.filmando = False
        print(f'{self.nome} parou de filmar')

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar enquanto estiver filmando')
        
        print(f'{self.nome} tirou uma foto!')