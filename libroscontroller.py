from libros import libros

class libroscontroller:
    def __init__(self):
        self.listalibros = {}

    def addlibros(self,librosmodel):
        if librosmodel.getisbn() not in self.listalibros:
            self.listalibros[librosmodel.getisbn()] = librosmodel
            return True
        return False       

    def borrarlibro(self,isbn):
        if isbn in self.listalibros:
            del self.listalibros[isbn]
            return True
        return False

    def modificarlibro(self, librosmodel):
        if librosmodel.getisbn() in self.listalibros:
            self.listalibros[librosmodel.getisbn()] = librosmodel
            return True
        return False    

    def listar(self):
        return self.listalibros
        
  
         