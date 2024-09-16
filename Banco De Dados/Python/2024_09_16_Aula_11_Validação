def validarSenha(senha):
    if len(senha)< 8 :
        return False
    elif not any(char.isdigit()for char in senha) :
        return False
    elif not any(char.isalpha()for char in senha) :
        return False
    else :
        return True
    
senha = "Eclipseeee2"
resultado = validarSenha(senha)
print(resultado)