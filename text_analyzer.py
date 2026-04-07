# ---- Funciones provistas (NO modificar) ----

def count_vowels(text):
    """Dado un texto, retorna la cantidad de vocales (a, e, i, o, u) que contiene."""
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

def count_consonants(text):
    """Dado un texto, retorna la cantidad de consonantes que contiene."""
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1
    return count

# ---- Funciones a implementar ----

def total_letters(text):
    """
    Retorna la cantidad total de letras en el texto.
    Debe USAR las funciones count_vowels y count_consonants.
    """
    return count_vowels(text)+  count_consonants(text)  

def vowel_percentage(text):
    """
    Retorna el porcentaje de vocales sobre el total de letras, redondeado a 1 decimal.
    Si no hay letras, retorna 0.0.
    Debe USAR las funciones count_vowels y total_letters.

    Ejemplo: "hola" tiene 2 vocales de 4 letras → 50.0
    """
    total_porcentaje = total_letters(text)
    if total_porcentaje == 0:
        return 0.0

    vowels = count_vowels(text)
    porcentaje_vowels = (vowels / total_porcentaje) * 100
    return round(porcentaje_vowels, 1)

def analyze_text(text):
    """
    Retorna un string con el análisis completo del texto usando el siguiente formato:
    "V:{vowels} C:{consonants} T:{total} P:{percentage}%"

    Debe USAR las funciones count_vowels, count_consonants, total_letters y vowel_percentage.

    Ejemplo: analyze_text("hola") → "V:2 C:2 T:4 P:50.0%"
    """
    contar_vowels = count_vowels(text)
    contar_consonantes = count_consonants(text)
    total_letras = total_letters(text)
    porcentaje_de_vowels = vowel_percentage(text)

    return f"V:{contar_vowels} C:{contar_consonantes} T:{total_letras} P:{porcentaje_de_vowels}%" 
