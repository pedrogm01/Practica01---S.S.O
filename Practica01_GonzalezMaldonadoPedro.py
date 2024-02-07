"""
Alumno:    González Maldonado, Pedro
Código:    215348836
Profesor:  Rosales Martínez, Javier
Clave:     I7030
NRC:       164138
Sección:   D07
"""

# Convierte una cadena hexadecimal en una cadena de números decimales separados por puntos.
def hex_to_decimal(hex_str):
    return '.'.join(str(int(x, 16)) for x in hex_str.split(':'))

# Convierte una cadena de números decimales separados por puntos en una cadena hexadecimal.
def decimal_to_hex(decimal_str):
    return '.'.join(format(int(x), 'X') for x in decimal_str.split('.'))

# Procesa una línea del archivo de entrada de acuerdo con las instrucciones dadas.
# Devuelve una cadena formateada con la segunda cadena, los números en decimal y los números en hexadecimal.
def process_line(line):
    parts = line.strip().split(', ')
    
    hex_values = parts[0].split(':')
    decimal_values = ' : '.join(hex_to_decimal(parts[0]).split('.'))
    second_string = parts[2]
    ip_address = parts[5]
    hex_ip = decimal_to_hex(ip_address)
    
    result = f"{second_string} : {decimal_values} : {hex_ip}"
    
    return result

# Procesa el archivo de entrada por lotes, aplicando la función process_line a cada línea y escribiendo el resultado en el archivo de salida.
def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            result = process_line(line)
            output_file.write(result + '\n')

# Archivos de entrada/salida.
input_file = 'archent_p01.txt'
output_file = 'archsal_p01.txt'

# Procesar el archivo por lotes
process_file(input_file, output_file)
