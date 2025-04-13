def celsius_to_fahrenheit(celsius):
  return (celsius * 9 / 5) + 32

celsius_input = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius_input)  
print(f"Celsius: {celsius_input}, Fahrenheit: {fahrenheit}")
