from tkinter import *
from tkinter import ttk
from tkinter.messagebox import * ## Paquete para mostrar mensajes
from tkinter import messagebox
import random

##from PIL import Image, ImageTk

## Clases importadas
from ListaNombres import ListaNombres
from Digipymon import Digi
from Inventario import Inventario
from Jugador import Jugador
from Enemigo import Enemigo

def main():
    global label_resultado, inventario, jugador, nuevo_digipymon, pelea_iniciada
    root = Tk()
    root.title("Digipymon")
    root.geometry("1000x720")
    root.iconbitmap("imagenes/pokeball.ico")# Icono de la ventana
    root.resizable(False, False)

    # Declarar label_resultado como una variable global

    generar_digipymon_aleatorio_volcan = None

    # Crear un Canvas para la imagen de fondo
    canvas = Canvas(root, width=1000, height=720)
    canvas.pack()

    # Cargar la imagen de fondo
    background_image = PhotoImage(file="imagenes/djpokemon.png")
    canvas.create_image(0, 0, anchor=NW, image=background_image)

    

    ############ BOTON MENU###########
    # Crear la barra de menú
    menubar = Menu(root)  # Asegúrate de usar tk.Menu
    root.config(menu=menubar)  # Configura la barra de menú para la ventana principal

    # Menú "Información"
    info_menu = Menu(menubar, tearoff=0)  # tearoff=0 para evitar separación

    def show_info():
        messagebox.showinfo("Informacion", "Hola")  # Mostrar un mensaje de información

    info_menu.add_command(label="Autores", command=show_info)

    menubar.add_cascade(label="Informacion", menu=info_menu)  # Añadir al menubar


    # Cargar el archivo CSS
    style = ttk.Style()
    style.theme_create("estilo", parent="clam")  # Crear un nuevo tema basado en el tema 'clam'
    style.theme_use("estilo")  # Aplicar el nuevo tema

    # Cargar estilos desde el archivo CSS
    style.configure("Label.TLabel", font=("Arial", 40), foreground="black", background="#baab53", borderradius=2, relief="radius", padx=10, pady=5)
    style.configure("Button.TButton", font=("Arial", 16),borderwidth=0, padding=10, background="#baab53",relief="radius", padx=10, pady=5)

 #Fondo Y Etiqueta
    frame1 = Frame(canvas)
    frame1.place(relx=0.5, rely=0.1, anchor=CENTER)  ## relx es de derecha a izq // rely es de arriba abajo
    frame_image = PhotoImage(file="imagenes/djpokemon.png")
    
    #Esplorar Inventario y salir
    frame2 = Frame(canvas, bg="#baab53")
    frame_canvas = Canvas(frame2)
    frame_image = PhotoImage(file="imagenes/djpokemon.png")
    frame2.place(relx=0.5, rely=0.5, anchor=CENTER)

    #Luchar
    frame3 = Frame(canvas, bg="#baab53")
    frame3.place(relx=0.5, rely=0.5, anchor=CENTER)

    #Hospital y tienda
    frame4 = Frame(canvas, bg="#baab53")
    frame4.place(relx=0.2, rely=0.5, anchor=CENTER)
    
    #Inventario y Buscar
    frame5 = Frame(canvas, bg="#baab53")
    frame5.place(relx=0.8, rely=0.5, anchor=CENTER)

    # Cargar la imagen de fondo en el Canvas
    frame_image = PhotoImage(file="imagenes/djpokemon.png")
    frame_canvas.create_image(0, 0, anchor=NW, image=frame_image)

    # Colocar el Frame en su posición deseada
    frame2.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    label_resultado = None

    background_image_abrir = None
    # Crear instancia de jugador
    jugador = Jugador("Kike")
    #crea e instancia el inventario
    inventario = Inventario()
        #Objetos con los que empiezas
    def Objetos_iniciales():
        inventario.añadir_objeto("Digipyball", 5)
        inventario.añadir_objeto("Pocion", 2)

    Objetos_iniciales()
    ######################## INVENTARIO ############################
    

    def mostrar_inventario(inventario):
        ventana = Toplevel()
        ventana.title("Inventario del jugador")
        ventana.geometry("1000x720")
        ventana.iconbitmap("imagenes/pokeball.ico")
        ventana.resizable(False, False)
        
        # Crear un Frame principal
        frame = Frame(ventana)
        frame.pack(fill=BOTH, expand=True)
        
        # Cargar la imagen de fondo
        background_image = PhotoImage(file="imagenes/djpokemon.png")
        background_label = Label(frame, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Label para mostrar información del inventario
        global label_resultado  # Asegúrate de tener la declaración global
        
        
        label1 = Label(frame, text="Informacion del inventario", font=("Arial", 20), bg="#baab53")
        label1.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        label_resultado = Label(frame, text="Resultado", font=("Arial", 20), bg="#baab53")
        label_resultado.place(relx=0.5, rely=0.3, anchor=CENTER)

    
        inventario_button = ttk.Button(frame, text="Ver tu inventario", style="Button.TButton", command=lambda: inventario.mostrar_inventario(label_resultado))
        inventario_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        ventana.mainloop()


    ######################## PELEA ############################
    pelea_iniciada = False
    def lucha():
        global label_resultado
        pestaña = Toplevel()
        pestaña.title("Menu de atacar")
        pestaña.geometry("1200x1024")
        pestaña.iconbitmap("imagenes/pokeball.ico")
        pestaña.resizable(False, False)

        # Crear un Frame principal
        frame = Frame(pestaña)
        frame.pack(fill=BOTH, expand=True)

        # Cargar la imagen de fondo
        background_image = PhotoImage(file="imagenes/grande.png")
        background_label = Label(frame, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Label encima del fondo
        label1 = Label(frame, text="Menu de atacar", font=("Arial", 20), bg="#baab53")
        label1.place(relx=0.5, rely=0.1, anchor=CENTER)

        global label_resultado
        label_resultado = Label(frame, text="Resultado", font=("Arial", 15), bg="#baab53")
        label_resultado.place(relx=0.5, rely=0.5, anchor=CENTER)

        lucha_button = ttk.Button(frame, text="Combatir", style="Button.TButton", command=iniciar_pelea)
        enemi_button = ttk.Button(frame, text="Buscar Contrincante", style="Button.TButton", command=buscar_enemigo)

        lucha_button.place(relx=0.20, rely=0.7, anchor=E)
        enemi_button.place(relx=0.20, rely=0.8, anchor=E)
        
        pestaña()
    
    
        
    def buscar_enemigo():
        global pelea_iniciada
        # Generar enemigo con la misma cantidad de digipymons que el jugador
        lista_nombres = ListaNombres()
        nombre_enemigo = lista_nombres.obtener_nombre_entrenador()
        enemigo = Enemigo(nombre_enemigo, 0, 0, "", 0)  # Crear instancia de Enemigo
        if jugador.digicoins >= 1:
            if not pelea_iniciada:
                # Reducir un Digicoin por buscar enemigo, excepto la primera vez
                if pelea_iniciada:
                    jugador.digicoins -= 1
                pelea_iniciada = True
                # Agregar digipymons al enemigo según la cantidad del jugador
                for _ in jugador.lista_digipymon:
                    enemigo.añadir_digipymon(Digi("EnemigoDigipymon", random.randint(10, 20), random.randint(1, 10), random.choice(["Agua", "Fuego", "Planta"]), random.randint(1, 3)))
                label_resultado.config(text="Buscando contrincante...")
                label_resultado.after(2000, lambda: label_resultado.config(text=enemigo.__str__()))
            else:
                label_resultado.config(text="No tienes suficientes Digicoins para buscar enemigos.")

            
        return enemigo
    
    def iniciar_pelea():
        global pelea_iniciada

        if pelea_iniciada:  # Solo permitir iniciar pelea si se ha buscado un enemigo
            # Buscar un enemigo
            enemigo = buscar_enemigo()
            
            # Combatir entre el jugador y el enemigo
            victorias_jugador = 0
            derrotas_jugador = 0
            
            for i in range(min(len(jugador.lista_digipymon), len(enemigo.lista_digipymon))):
                jugador_digipymon = jugador.lista_digipymon[i]
                enemigo_digipymon = enemigo.lista_digipymon[i]
                
                if jugador_digipymon.ataque > enemigo_digipymon.ataque:
                    enemigo_digipymon.vida -= (jugador_digipymon.ataque - enemigo_digipymon.ataque)
                    victorias_jugador += 1
                elif jugador_digipymon.ataque < enemigo_digipymon.ataque:
                    jugador_digipymon.vida -= (enemigo_digipymon.ataque - jugador_digipymon.ataque)
                    derrotas_jugador += 1
            
            # Gestionar recompensas y penalizaciones
            if victorias_jugador > derrotas_jugador:
                jugador.digicoins += victorias_jugador
                resultado = f"¡Ganaste la batalla y ganaste {victorias_jugador} Digicoins!"
            elif victorias_jugador < derrotas_jugador:
                jugador.digicoins = max(0, jugador.digicoins - derrotas_jugador)
                resultado = f"Perdiste la batalla y perdiste {derrotas_jugador} Digicoins."
            else:
                resultado = "La batalla terminó en empate."
            pelea_iniciada = False  # Reiniciar el estado de pelea
        else:
            resultado = "Primero debes buscar un enemigo."

        # Actualizar el resultado en el Label
        label_resultado.config(text=resultado)
        
    ###################### HOSPITAL ######################
    def curar_digipymon(digipymon):
        global label_resultado, inventario
        # Objeto de curación
        objeto_curacion = "Pocion" 
        cantidad_necesaria = 1  

            # Verificar si hay suficientes pociones en el inventario
        if isinstance(inventario, Inventario):
            if objeto_curacion in inventario.objetos and inventario.objetos[objeto_curacion] >= cantidad_necesaria:
                digipymon.curar()  # Curar el Digipymon
                inventario.usar_objeto(objeto_curacion, cantidad_necesaria)  # Usar la poción
                if label_resultado:
                    label_resultado.config(text=f"{digipymon.nombre} ha sido curado usando una poción.")
            else:
                label_resultado.config(text="No tienes mas pociones.")

   


    def chetar_digipymon(digipymon):
        global label_resultado, inventario
        # Objeto de fuerza
        objeto_chetar= "Anabolizantes" 
        cantidad_necesaria = 1  

            # Verificar si hay suficientes anabolizantes en el inventario
        if isinstance(inventario, Inventario):
            if objeto_chetar in inventario.objetos and inventario.objetos[objeto_chetar] >= cantidad_necesaria:
                digipymon.chetar()  # Chetar el Digipymon
                inventario.usar_objeto(objeto_chetar, cantidad_necesaria)  # Usar lel anabolizante
                if label_resultado:
                    label_resultado.config(text=f"{digipymon.nombre} ha sido mas fuerte en un 50% mas por un anabolizante.")
            else:
                label_resultado.config(text="No tienes mas anabolizantes.")
    def mostrar_informacion_digipymon(digipymon):
        global label_resultado
        # Actualizar el resultado si existe un label_resultado
        if label_resultado:
            resultado = str(digipymon)  # Convertir el objeto Digipymon a string
            label_resultado.config(text=resultado)
       # messagebox.showinfo("Información del Digipymon", str(digipymon))

    def hospital():
        global label_resultado
        pestaña = Toplevel()
        pestaña.title("Hospital")
        pestaña.geometry("1200x1024")
        pestaña.resizable(False, False)
        
        # Crear un Canvas para la imagen de fondo
        frame_canvas = Canvas(pestaña, width=1000, height=720)
        frame_canvas.pack(fill=BOTH, expand=True)
        
        # Cargar la imagen de fondo en el Canvas
        frame_image = PhotoImage(file="imagenes/grande.png")
        frame_canvas.create_image(0, 0, anchor=NW, image=frame_image)
        
        # Label encima del fondo
        label1 = Label(pestaña, text="Hospital Digipymon", font=("Arial", 20), bg="#baab53")
        label1.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        global label_resultado
        label_resultado = Label(pestaña, text="Resultado", font=("Arial", 20), bg="#baab53")
        label_resultado.place(relx=0.5, rely=0.2, anchor=CENTER)
    
        # Obtener la lista de Digipymon del jugador
        lista_digipymon = jugador.lista_digipymon
        
        # Crear botones para cada Digipymon en la lista del jugador
        for i, digipymon in enumerate(lista_digipymon):
            # Crear un botón con el nombre del Digipymon
            boton = ttk.Button(pestaña, text=digipymon.nombre, style="Button.TButton")
            # Asociar la función mostrar_informacion_digipymon al evento de clic en el botón
            boton.config(command=lambda dp=digipymon: mostrar_informacion_digipymon(dp))
            # Posicionar los botones
            boton.place(relx=0.5, rely=0.4 + i*0.1, anchor=CENTER)
            
        #crea el botón para curar el digipymon
        Curar = ttk.Button(pestaña, text="Curar Digipymon", style="Button.TButton", command=lambda: curar_digipymon(digipymon))
        Curar.place(relx=0.20, rely=0.7, anchor=E)
        
        #crea el botón para dopar el digipymon
        Anabolizante = ttk.Button(pestaña, text="Dopar Digipymon", style="Button.TButton", command=lambda: chetar_digipymon(digipymon)) 
        Anabolizante.place(relx=0.20, rely=0.8, anchor=E)
        
        pestaña.mainloop()
        
      
 
    ###################### TIENDA ##################################

      
    def comprar_digipyball():
        global label_resultado
        if jugador.digicoins >= 5:  # Verificar que el jugador tiene suficiente dinero
            jugador.digicoins -= 5  # Restar el costo del objeto del saldo del jugador
            
            # Verificar si el objeto ya está en el inventario
            if "Digipyball" in inventario.objetos:
                # Si está, incrementa la cantidad
                inventario.objetos["Digipyball"] += 1
            else:
                # Si no está, añade el objeto con la cantidad inicial
                inventario.añadir_objeto("Digipyball", 1)
            
            resultado = "¡Has comprado un Digipyball y se ha añadido a tu inventario!"
        else:
            resultado = "No tienes suficientes Digicoins para comprar un Digipyball."

        if label_resultado:
            label_resultado.config(text=resultado)  # Esto debería estar indentado al mismo nivel que el bloque 'else'



    def comprar_pocion():
        global label_resultado
        if jugador.digicoins >= 4:  # Verificar que el jugador tiene suficiente dinero
            jugador.digicoins -= 4  # Restar el costo del objeto del saldo del jugador
            
            # Verificar si el objeto ya está en el inventario
            if "Pocion" in inventario.objetos:
                # Si está, incrementa la cantidad
                inventario.objetos["Pocion"] += 1
            else:
                # Si no está, añade el objeto con la cantidad inicial
                inventario.añadir_objeto("Pocion", 1)
            
            resultado = "¡Has comprado una Pocion y se ha añadido a tu inventario!"
        else:
            resultado = "No tienes suficientes Digicoins para comprar una Pocion."

        if label_resultado:
            label_resultado.config(text=resultado)  # Esto debería estar indentado al mismo nivel que el bloque 'else'

    def comprar_anabolizantes():
        global label_resultado
        if jugador.digicoins >= 3:  # Verificar que el jugador tiene suficiente dinero
            jugador.digicoins -= 3  # Restar el costo del objeto del saldo del jugador
            
            # Verificar si el objeto ya está en el inventario
            if "Anabolizantes" in inventario.objetos:
                # Si está, incrementa la cantidad
                inventario.objetos["Anabolizantes"] += 1
            else:
                # Si no está, añade el objeto con la cantidad inicial
                inventario.añadir_objeto("Anabolizantes", 1)
            
            resultado = "¡Has comprado un Anabolizantes y se ha añadido a tu inventario!"
        else:
            resultado = "No tienes suficientes Digicoins para comprar un Anabolizantes."

        if label_resultado:
            label_resultado.config(text=resultado)  # Esto debería estar indentado al mismo nivel que el bloque 'else'
        
    def tienda():
        global label_resultado, jugador
        top = Toplevel()
        top.resizable(False, False)
        
        # Crear un Canvas para la imagen de fondo
        frame_canvas = Canvas(top, width=1000, height=720)
        frame_canvas.pack(fill=BOTH, expand=True)
        
        # Cargar la imagen de fondo en el Canvas
        frame_image = PhotoImage(file="imagenes/djpokemon.png")
        frame_canvas.create_image(0, 0, anchor=NW, image=frame_image)
        
        # Obtener la cantidad de Digicoins del jugador
        cantidad_digicoins = jugador.digicoins
        
        # Crear el texto para el título con la cantidad de Digicoins
        titulo_texto = f"Tienda Digipymon - Digicoins: {cantidad_digicoins}"
        
        # Label encima del fondo con el título actualizado
        label1 = Label(top, text=titulo_texto, font=("Arial", 20), bg="#baab53")
        label1.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        global label_resultado
        label_resultado = Label(top, text="Resultado", font=("Arial", 20), bg="#baab53")
        label_resultado.place(relx=0.5, rely=0.3, anchor=CENTER)

        Digipyballs = ttk.Button(top, text="Digipyballs", style="Button.TButton", command=comprar_digipyball)

        Pociones = ttk.Button(top, text="Pociones", style="Button.TButton", command=comprar_pocion)
        Anabolizantes = ttk.Button(top, text="Anabolizantes", style="Button.TButton", command=comprar_anabolizantes)
        
           
        Digipyballs.place(relx=0.5, rely=0.5, anchor=CENTER)
        Pociones.place(relx=0.5, rely=0.6, anchor=CENTER)
        Anabolizantes.place(relx=0.5, rely=0.7, anchor=CENTER)
        
        

            
        top.mainloop()



     ##################### FUNCIONES BUSCAR POKEMON ###########################
    def capturar_digipymon():
            global label_resultado, inventario, jugador, nuevo_digipymon


            # Probabilidad de captura (por ejemplo, 50%)
            probabilidad_captura = 0.5
            if random.random() < probabilidad_captura:
                # El Digipymon es capturado
                jugador.añadir_digipymon(nuevo_digipymon)
                label_resultado.config(text=f"¡Has capturado a {nuevo_digipymon.nombre}!")
                # Quitar una Digipyball del inventario si está disponible
                if "Digipyball" in inventario.objetos and inventario.objetos["Digipyball"] > 0:
                    inventario.usar_objeto("Digipyball", 1)
                else:
                    label_resultado.config(text="No tienes Digipyballs")
            else:
                # El Digipymon escapa
                if "Digipyball" in inventario.objetos and inventario.objetos["Digipyball"] > 0:
                    inventario.usar_objeto("Digipyball", 1)
                    label_resultado.config(text=f"{nuevo_digipymon.nombre} escapó. Perdiste una Digipyball.")
                else:
                    label_resultado.config(text="¡El Digipymon escapó y no tienes Digipyballs para capturarlo!")

    def generar_digipymon_aleatorio_volcan():
        global label_resultado, inventario, jugador, nuevo_digipymon
            
        # Generar un Digipymon aleatorio de tipo Volcan
        nivel = random.randint(1, 3)
        vida = random.randint(10, 20)
        ataque = random.randint(1, 10)
        lista_nombres = ListaNombres()
        nombre = lista_nombres.obtener_nombre_digipymon_fuego()
        nuevo_digipymon = Digi(nombre, vida, ataque, "Fuego", nivel)

        # Actualizar el resultado si existe un label_resultado
        if label_resultado:
            resultado = str(nuevo_digipymon)  # Convertir el objeto Digipymon a string
            label_resultado.config(text=resultado)


            
    def generar_digipymon_aleatorio_jardin():
        global label_resultado, inventario, jugador, nuevo_digipymon
        
        # Generar un Digipymon aleatorio de tipo Volcan
        nivel = random.randint(1, 3)
        vida = random.randint(10, 20)
        ataque = random.randint(1, 10)
        lista_nombres = ListaNombres()
        nombre = lista_nombres.obtener_nombre_digipymon_planta()
        nuevo_digipymon = Digi(nombre, vida, ataque, "Planta", nivel)

        # Actualizar el resultado si existe un label_resultado
        if label_resultado:
                resultado = str(nuevo_digipymon)  # Convertir el objeto Digipymon a string
                label_resultado.config(text=resultado)

                
                
    def generar_digipymon_aleatorio_lago():
        global label_resultado, inventario, jugador, nuevo_digipymon
        
        # Generar un Digipymon aleatorio de tipo Volcan
        nivel = random.randint(1, 3)
        vida = random.randint(10, 20)
        ataque = random.randint(1, 10)
        lista_nombres = ListaNombres()
        nombre = lista_nombres.obtener_nombre_digipymon_agua()
        nuevo_digipymon = Digi(nombre, vida, ataque, "Agua", nivel)

        # Actualizar el resultado si existe un label_resultado
        if label_resultado:
                resultado = str(nuevo_digipymon)  # Convertir el objeto Digipymon a string
                label_resultado.config(text=resultado)
        
        ## Funcion abrir
    def buscar_digipymons():
        global label_resultado, jugador, inventario
        top = Toplevel()
        top.title("Buscar Digipymon")
        top.resizable(False, False)
        
        # Crear un Canvas para la imagen de fondo
        frame_canvas = Canvas(top, width=1000, height=720)
        frame_canvas.pack(fill=BOTH, expand=True)
        
        # Cargar la imagen de fondo en el Canvas
        frame_image = PhotoImage(file="imagenes/djpokemon.png")
        frame_canvas.create_image(0, 0, anchor=NW, image=frame_image)
        
        # Label encima del fondo
        label1 = Label(top, text="Selecciona donde buscar los Digipymon ", font=("Arial", 20), bg="#baab53")
        label1.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        global label_resultado
        label_resultado = Label(top, text="Resultado ", font=("Arial", 20), bg="#baab53")
        label_resultado.place(relx=0.5, rely=0.3, anchor=CENTER)

        volcan = ttk.Button(top, text="Volcan", style="Button.TButton", command=generar_digipymon_aleatorio_volcan)

        lago = ttk.Button(top, text="Lago", style="Button.TButton", command=generar_digipymon_aleatorio_lago)
        
        jardin = ttk.Button(top, text="Jardín", style="Button.TButton", command= generar_digipymon_aleatorio_jardin)
        
        capturar = ttk.Button(top, text="Capturar Digipymon", style="Button.TButton",command= capturar_digipymon)
        
        volcan.place(relx=0.5, rely=0.5, anchor=CENTER)
        lago.place(relx=0.5, rely=0.6, anchor=CENTER)
        jardin.place(relx=0.5, rely=0.7, anchor=CENTER)
        
        capturar.place(relx=0.59, rely=0.6, anchor=W)
        
        top()
     
    def salir():
        root.quit()  # Cerrar la ventana principal

            
            
#################### BOTONES PRINCIPALES #################################

    labelprincipal = ttk.Label(frame1, text="Digipymon", style="Label.TLabel")
    labelprincipal.pack(side="top", anchor="n")
    

    luchautton_image = PhotoImage(file="imagenes/luchaBuena2.png")
    luchautton_image = luchautton_image.subsample(1, 1)
    luchautton = ttk.Button(frame3, style="Button.TButton", image=luchautton_image, command=lucha)


    hospital_image = PhotoImage(file="imagenes/hospital.png")
    hospital_image = hospital_image.subsample(2, 2)
    hospital = ttk.Button(frame4, style="Button.TButton", image=hospital_image, command=hospital)


    tienda_image = PhotoImage(file="imagenes/tienda.png")
    tienda_image = tienda_image.subsample(2, 2)
    tienda = ttk.Button(frame4, style="Button.TButton", image=tienda_image, command=tienda)


    inventario_image = PhotoImage(file="imagenes/inventario.png")
    inventario_image = inventario_image.subsample(1, 1)
    inventariobutton = ttk.Button(frame5, image=inventario_image, style="Button.TButton", command=lambda: mostrar_inventario(inventario))


    buscar_image = PhotoImage(file="imagenes/buscar.png")
    buscar_image = buscar_image.subsample(1, 1) ##Redimensionar imagen del boton
    buscarbutton = ttk.Button(frame5, image=buscar_image, style="Button.TButton", command=buscar_digipymons)


    # Empaquetar los botones en la parte inferior de frame2 y centrarlos horizontalmente

    inventariobutton.pack(side="bottom",pady=(10, 20))

    luchautton.pack(side="bottom",pady=(10, 20))

    hospital.pack(side="bottom",pady=(10, 20))

    tienda.pack(side="bottom",pady=(10, 20))

    buscarbutton.pack(side="bottom",pady=(10, 20))

    # Mensaje a la hora de ejecutar el programa
    showinfo("Digipymon", "Bienvenido al mundo de Digipymon")


    #################Cierre####################


    root.mainloop()
    Inventario.mainloop()
main()
