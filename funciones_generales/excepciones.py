class Excepciones(Exception):
    def __init__(self):
        super().__init__()
    
    @staticmethod
    def validar_Main(n):
        if n > 4 or n <= 0:
            raise Excepciones