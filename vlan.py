def determinar_rango_vlan(vlan):
    if 1 <= vlan <= 1005:
        return "vlan del rango normal"
    elif 1006 <= vlan <= 4094:
        return "vlan del rango extendido"
    else:
        return "numero de vlan fuera de rango"

try:
    vlan = int(input("introduce el numero de vlan: "))
    print(determinar_rango_vlan(vlan))
except VlaueError:
    print("Por favor, introduce un numero entero.") 
