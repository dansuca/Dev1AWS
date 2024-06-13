phone= 9 #int 
phone_inches_height= 2.5 #float
phone_inches_width= 2.6 # float
phone_model = "i500" #str
phone_make = "Example" #str
phone_variable = True #bool
phone_area= phone_inches_height * phone_inches_width
phone_name = phone_make + " " + phone_model
# Construir una cadena formateada a partir de variables en python
# con el prefijo f
phone_name = f"{phone_make}{phone_model}"
print(f"{phone_name} is {phone_area:.5} squere inches")