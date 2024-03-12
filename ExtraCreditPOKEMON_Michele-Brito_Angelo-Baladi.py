#----------------------------------------------------------------------------------- PARTE 1
import random

class Jugador:
    def __init__(self, nombre, edad, lugar_origen):
        self.nombre = nombre
        self.edad = edad
        self.lugar_origen = lugar_origen
        self.companero = None
        self.starter = None

    def seleccionar_companero(self):
        if self.lugar_origen == "Pueblo Paleta":
            return "Ash"
        elif self.lugar_origen == "Ciudad Plateada":
            return "Gary"
        else:
            return "Misty"

    def seleccionar_starter(self, tipo_starter):
        if tipo_starter == "Fuego":
            return Pokemon("Charmander", "Fuego")
        elif tipo_starter == "Agua":
            return Pokemon("Squirtle", "Agua")
        else:
            return Pokemon("Bulbasaur", "Planta")

class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = 100
        self.ataques = {
            "Ataque1": 10,
            "Ataque2": 15,
            "Ataque3": 20,
            "Ataque4": 5,
            "Ataque5": 12,
            "Ataque6": 25,
            "Ataque7": 30,
            "Ataque8": 7,
            "Ataque9": 18,
            "Ataque10": 22
        }

    def atacar(self, ataque, oponente):
        if ataque in self.ataques:
            dano = self.ataques[ataque]
            oponente.recibir_dano(dano)
            print(f"{self.nombre} ha usado {ataque} y ha hecho {dano} de daño a {oponente.nombre}.")
        else:
            print("¡Ataque no válido!")

    def recibir_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            print(f"{self.nombre} ha sido derrotado.")
        else:
            print(f"{self.nombre} tiene {self.vida} de vida restante.")

# Crear perfil de jugador
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
lugar_origen = input("Ingrese su lugar de origen (Pueblo Paleta/Ciudad Plateada/otro): ")

jugador = Jugador(nombre, edad, lugar_origen)
print(f"Bienvenido/a, {jugador.nombre}!")
print(f"Tu compañero es {jugador.seleccionar_companero()}.")

# Elegir un starter
tipo_starter = input("Elige tu starter (Fuego/Agua/Planta): ")
jugador.starter = jugador.seleccionar_starter(tipo_starter)
print(f"Has elegido a {jugador.starter.nombre} como tu starter.")

# Crear compañero humano con el mismo starter
companero = Jugador("Companero Humano", 20, "Pueblo Paleta")
companero.starter = jugador.starter

# Realizar la batalla entre los starters
print("Tu compañero, " + jugador.seleccionar_companero() + ", ha elegido a", companero.starter.nombre, "como su starter.")
print("¡Comienza la batalla entre los starters!")

# Simular batalla por turnos entre los Pokémon
while jugador.starter.vida > 0 and companero.starter.vida > 0:
    # Turno del jugador
    print("\nTurno del jugador:")
    print("Ataques disponibles:  ['Ataque1', 'Ataque2', 'Ataque3']")
    ataque_elegido = input("Elige un ataque: ")
    if ataque_elegido in jugador.starter.ataques:
        jugador.starter.atacar(ataque_elegido, companero.starter)
    else:
        print("¡Ataque no válido! Inténtalo de nuevo.")

    # Verificar si el oponente ha sido derrotado
    if companero.starter.vida <= 0:
        break

    # Turno del compañero humano
    print("\nTurno del compañero humano:")
    ataque_aleatorio = random.choice(list(companero.starter.ataques.keys()))
    companero.starter.atacar(ataque_aleatorio, jugador.starter)

# Mostrar resultado de la batalla
if companero.starter.vida <= 0:
    print("¡Felicidades! ¡Has ganado la batalla!")
else:
    print("¡Has perdido la batalla! ¡Mejor suerte la próxima vez!")
#----------------------------------------------------------------------------------- PARTE 2
    
class Ubicacion:
    def __init__(self, nombre, criatura=None):
        self.nombre = nombre
        self.criatura = criatura

class Criatura:
    def __init__(self, nombre, vida, ataques):
        self.nombre = nombre
        self.vida = vida
        self.ataques = ataques

def sanar(jugador):
    jugador.starter.vida = 70
    print(f"{jugador.starter.nombre} ha sido sanado. Vida restablecida a {jugador.starter.vida}.")

def avanzar_ubicacion():
    global posicion_actual
    posicion_actual += 1
    if posicion_actual >= len(ubicaciones):
        print("¡Has completado la Liga Pokémon! ¡Felicidades!")
        return True
    return False

def regresar_ubicacion():
    global posicion_actual
    posicion_actual -= 1
    if posicion_actual < 0:
        print("¡Estás en el inicio del viaje!")
        return True
    return False

lider = Jugador("Líder Humano", 30, "Pueblo Paleta")
lider.starter = lider.seleccionar_starter("Fuego")
def enfrentar_lider(jugador, lider):
    # Simular batalla por turnos entre los Pokémon
    while jugador.starter.vida > 0 and lider.starter.vida > 0:
        # Turno del jugador
        print("\nTurno del jugador:")
        print("Ataques disponibles:", list(jugador.starter.ataques.keys()))
        ataque_elegido = input("Elige un ataque: ")
        if ataque_elegido in jugador.starter.ataques:
            jugador.starter.atacar(ataque_elegido, lider.starter)
        else:
            print("¡Ataque no válido! Inténtalo de nuevo.")

        # Verificar si el oponente ha sido derrotado
        if lider.starter.vida <= 0:
            break

        # Turno del líder humano
        print("\nTurno del líder humano:")
        ataque_aleatorio = random.choice(list(lider.starter.ataques.keys()))
        lider.starter.atacar(ataque_aleatorio, jugador.starter)

    # Mostrar resultado de la batalla
    if lider.starter.vida <= 0:
        print("¡Felicidades! ¡Has derrotado al Líder!")
    else:
        print("-----------------------------")
        
enfrentar_lider(jugador, lider)

def enfrentar_lider():
    print("--------------------------------")
    print("¡Te estás enfrentando al Líder de este Pueblo!")
    print("Debido a tus enfrentamiento en las rutas has desbloqueado los siguientes ataques: \n['Ataque4', 'Ataque5', 'Ataque6', 'Ataque7', 'Ataque8', 'Ataque9', 'Ataque10'] ")
    # Simular batalla por turnos entre los Pokémon
    while jugador.starter.vida > 0 and lider.starter.vida > 0:
        # Turno del jugador
        print("\nTurno del jugador:")
        print("Ataques disponibles:", list(jugador.starter.ataques.keys()))
        ataque_elegido = input("Elige un ataque: ")
        if ataque_elegido in jugador.starter.ataques:
            jugador.starter.atacar(ataque_elegido, lider.starter)
        else:
            print("¡Ataque no válido! Inténtalo de nuevo.")

        # Verificar si el oponente ha sido derrotado
        if lider.starter.vida <= 0:
            break

        # Turno del líder humano
        print("\nTurno del líder humano:")
        ataque_aleatorio = random.choice(list(lider.starter.ataques.keys()))
        lider.starter.atacar(ataque_aleatorio, jugador.starter)

    # Mostrar resultado de la batalla
    if lider.starter.vida <= 0:
        print("¡Felicidades! ¡Has ganado la batalla!")
    else:
        print("¡Has perdido la batalla! ¡Mejor suerte la próxima vez!")

# Definir criaturas con sus ataques y daños para la
criatura1 = Criatura("Pidgey", 50, {"Ataque Ala": 10, "Picotazo": 8})
criatura2 = Criatura("Rattata", 60, {"Ataque Rápido": 12, "Colmillo Veneno": 10})
criatura3 = Criatura("Caterpie", 40, {"Látigo": 6, "Drenadoras": 5})
criatura4 = Criatura("Ekans", 70, {"Mordisco": 15, "Ácido": 12})
criatura5 = Criatura("Spearow", 55, {"Ataque Ala": 11, "Picotazo Venenoso": 9})
criatura6 = Criatura("Sandshrew", 65, {"Arañazo": 13, "Excavar": 11})
criatura7 = Criatura("Nidoran M", 45, {"Absorber": 7, "Ácido": 8})

ubicaciones = [
    Ubicacion("Pueblo Rojo"),
    Ubicacion("Ruta 1", criatura1),
    Ubicacion("Ruta 2", criatura2),
    Ubicacion("Pueblo Naranja"),
    Ubicacion("Ruta 3", criatura3),
    Ubicacion("Ruta 4", criatura4),
    Ubicacion("Pueblo Amarillo"),
    Ubicacion("Ruta 5", criatura5),
    Ubicacion("Ruta 6", criatura6),
    Ubicacion("Pueblo Verde"),
    Ubicacion("Ruta 7", criatura7),
    Ubicacion("Liga")
]

# Inicializar jugador en la primera ubicación
posicion_actual = 0

def criatura_viva(criatura):
    return criatura.vida > 0

def jugador_vivo(jugador):
    return jugador.starter.vida > 0
while True:
    print(f"Te encuentras en: {ubicaciones[posicion_actual].nombre}")

    if ubicaciones[posicion_actual].criatura:
        batalla = random.choice([True, False])
        if batalla:
            criatura_actual = ubicaciones[posicion_actual].criatura
            print(f"¡Un {criatura_actual.nombre} salvaje aparece!")

            # Lógica de la batalla con la criatura
            while True:
                print("\nTurno del jugador:")
                print("Ataques disponibles:", list(criatura_actual.ataques.keys()))
                ataque_elegido = input("Elige un ataque: ")
                if ataque_elegido in criatura_actual.ataques:
                    dano_ataque = criatura_actual.ataques[ataque_elegido]
                    print(f"¡Has usado {ataque_elegido} y has hecho {dano_ataque} de daño a {criatura_actual.nombre}!")
                    criatura_actual.vida -= dano_ataque

                    if criatura_viva(criatura_actual):
                        print(f"{criatura_actual.nombre} tiene {criatura_actual.vida} de vida restante.")

                        # Turno de la criatura
                        ataque_criatura = random.choice(list(criatura_actual.ataques.keys()))
                        dano_ataque_criatura = criatura_actual.ataques[ataque_criatura]
                        print(f"La {criatura_actual.nombre} salvaje ha usado {ataque_criatura} y te ha hecho {dano_ataque_criatura} de daño.")
                        # Actualizar la vida del jugador
                        if not jugador_vivo(jugador):
                            print("¡Has sido derrotado! Fin del juego.")
                            break
                    else:
                        print(f"¡Has derrotado a {criatura_actual.nombre}!")
                        break
                else:
                    print("¡Ataque no válido! Inténtalo de nuevo.")

        else:
            print("No hay criaturas salvajes en esta ruta.")

    decision = input("¿Qué deseas hacer? (sanar (nota: sanar es posible 1 vez por pueblo) /enfrentar (nota: escoge una vez en la Liga)/regresar/avanzar): ").lower()

    if decision == "sanar":
        sanar(jugador)
    elif decision == "enfrentar":
        enfrentar_lider()
    elif decision == "avanzar":
        if avanzar_ubicacion():
            break
    elif decision == "regresar":
        if regresar_ubicacion():
            break
#----------------------------------------------------------------------------------- PARTE 3
      