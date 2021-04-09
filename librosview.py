from libros import libros
from libroscontroller import libroscontroller

con = libroscontroller()

while True:
    
    opcion =0
    print("Menu principal")
    print("1-añadir libros")
    print("2-borrar libros")
    print("3-modificar libros")
    print("4-listar clasificacion")
    print("5-Mostrar libros con la misma nota")
    while True:
        try:       
            opcion = int(input("Opción: ")) 
            break     
        except ValueError:
            print("Sólo números")

    if opcion ==1:

        while True:
            try:         
                isbn = int(input("Dime el isbn"))
                break
            except ValueError:
                print("Tiene que ser un numero")    

        titulo = input("Dime el titulo")    
        autor = input("Dime el autor")
        while True:
            try:
                paginas = int(input("Dime las paginas"))
                break
            except ValueError:
                print("Tiene que ser un numero")
        while True:
            try:
                cla = int(input("Dime la clasificacion"))
                break
            except ValueError:
                print("Tiene que ser un numero")
        
        libro = libros(isbn,titulo,autor,paginas,cla)

        if con.addlibros(libro):
            print("Se ha guardado el libro")
        else:
            print("No se ha guardado")    

    if opcion ==2:
        while True:
            try:         
                isbn = int(input("Dime el isbn"))
                break
            except ValueError:
                print("Tiene que ser un numero")   

        if con.borrarlibro(isbn):
            print("se ha borrado correctamente")

        else:
            print("no se ha borrado")    

    if opcion ==3:
        while True:
            try:         
                isbn = int(input("Dime el isbn"))
                break
            except ValueError:
                print("Tiene que ser un numero")   
        titulo = input("Dime el titulo")    
        autor = input("Dime el autor")
        while True:
            try:
                paginas = int(input("Dime las paginas"))
                break
            except ValueError:
                print("Tiene que ser un numero")
        while True:
            try:
                cla = int(input("Dime la clasificacion"))
                break
            except ValueError:
                print("Tiene que ser un numero")
        
        if con.modificarlibro(libro):
            print("Se ha modificado el libro")
        else:
            print("No se ha modificado")    

    if opcion ==4:
        print("***LISTAR LIBROS***")
        listalibros = con.listar()
        if(len(listalibros)== 0):
            print("Aun no hay libros")
        else: 
            for i in listalibros:
                print("ISBN",listalibros[i].getisbn())
                print("Titutlo",listalibros[i].getitulo())
                print("Autor",listalibros[i].getautor())
                print("Paginas",listalibros[i].getpaginas())
                print("Clasificacion",listalibros[i].getcla())
            
            for i in max(listalibros):
                print ("Clasifiacion maxima",listalibros[i].getcla())
            for i in min(listalibros):
                print ("Clasifiacion minima",listalibros[i].getcla())
    if opcion ==5:
        nota =int(input("Dime la clasificación"))
        listalibros = con.listar()
        for i in listalibros:
            if nota == listalibros[i].getcla():
                print("ISBN",listalibros[i].getisbn())
                print("Titutlo",listalibros[i].getitulo())
                print("Autor",listalibros[i].getautor())
                print("Paginas",listalibros[i].getpaginas())
                print("Clasificacion",listalibros[i].getcla())
