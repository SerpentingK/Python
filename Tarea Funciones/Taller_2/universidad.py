
def get_grades():
    grades = []
    percentages = []
    total_percentage = 0
    
    while True:
        grade = float(input("Ingrese la nota obtenida: "))
        percentage = float(input("Ingrese el porcentaje de la nota: "))
        
        if total_percentage + percentage > 100:
            print("El porcentaje evaluado de una materia no puede ser mayor a 100")
            continue
        
        grades.append(grade)
        percentages.append(percentage)
        total_percentage += percentage
        
        if total_percentage == 100:
            break
        
        add_more = input("¿Faltan notas por añadir? (S/N): ")
        if add_more.upper() != "S":
            break
    
    return grades, percentages

def calculate_accumulated_grade(grades, percentages):
    accumulated_grade = sum(grade * (percentage / 100) for grade, percentage in zip(grades, percentages))
    return round(accumulated_grade, 2)

student_name = input("Ingrese su nombre: ")
subject_name = input("Ingrese el nombre de la materia: ")
grades, percentages = get_grades()
accumulated_grade = calculate_accumulated_grade(grades, percentages)
print(f"El estudiante {student_name.capitalize()} cursó la materia {subject_name.capitalize()} y obtuvo una nota acumulada de {accumulated_grade}.")
