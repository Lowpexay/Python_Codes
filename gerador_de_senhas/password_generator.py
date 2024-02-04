import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, numbers=True, specials=True):
    characters = ""
    
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if specials:
        characters += string.punctuation

    if not any([uppercase, lowercase, numbers, specials]):
        print("Erro: Pelo menos uma opção deve ser ativada.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    # Exemplo simples de verificação de força (pode ser aprimorado)
    if len(password) < 8:
        return "Fraca"
    elif len(password) < 12:
        return "Moderada"
    else:
        return "Forte"

if __name__ == "__main__":
    print("Gerador de Senhas")

    length = int(input("Comprimento da senha: "))
    uppercase = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    lowercase = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    numbers = input("Incluir números? (s/n): ").lower() == 's'
    specials = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

    generated_password = generate_password(length, uppercase, lowercase, numbers, specials)

    if generated_password:
        print(f"\nSenha gerada: {generated_password}")
        print(f"Força da senha: {password_strength(generated_password)}")
