class Excepciones(Exception):
    def __init__(self):
        super().__init__()
    
    @staticmethod
    def validar_Main(n):
        if n > 5 or n <= 0:
            raise Excepciones
