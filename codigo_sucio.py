# EJEMPLO 1
s = [88, 92, 79, 93, 85] # calificaciones del examen
print(sum(s)/len(s)) # imprimir media de calificaciones del examen

s1 = [x ** 0.5 * 10 for x in s] # curvar calificaciones con método de raíz cuadrada en nueva lista
print(sum(s1)/len(s1)) # imprimir media de calificaciones en curva

##########################################

# EJEMPLO 2
ages = [47, 12, 28, 52, 35]
for i, age in enumerate(ages):
    if age < 18:
        is_minor = True
        ages[i] = "minor"
    # some other code

##########################################################

# EJEMPLO 3
def count_unique_values_of_names_list_with_set(names_list):
    return len(set(names_list))