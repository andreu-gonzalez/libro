class libros:

    def __init__(self,isbn,titulo,autor,paginas,cla):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.cla = cla

    def getisbn(self):
        return self.isbn

    def getitulo(self):
        return self.titulo

    def getautor(self):
        return self.autor

    def getpaginas(self):
        return self.paginas

    def getcla(self):
        return self.cla


                