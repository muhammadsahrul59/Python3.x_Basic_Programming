# latihan konversi satuan temperature

# program konversi celcius ke satuan lain

print("PROGRAM KONVERSI TEMPERATURE\n")

celcius = float(input('Masukan suhu dalam celcius : '))
print("suhu adalah ", celcius, "Celcius")

# reamur'
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ", reamur, "Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam farenheit adalah ", fahrenheit, "fahrenheit")

#kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah ", kelvin, "kelvin")

# Tugas

## Konversi Fahrenheit ke kelvin
fahrenheit = float(input('Masukan suhu dalam fahrenheit : '))
print("suhu adalah ", fahrenheit, "Fahrenheit")

kelvin =  (5/9 * (fahrenheit - 32)) + 273
print("suhu dalam kelvin adalah ", kelvin, "kelvin")

## Konversi Kelvin ke Fahrenheit

kelvin = float(input('Masukan suhu dalam kelvin : '))
print("suhu adalah ", kelvin, "Kelvin")

fahrenheit = (9/5 *(kelvin-273)) + 32
print("suhu dalam kelvin adalah ", fahrenheit, "fahrenheit")
