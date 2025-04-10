import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_home_screen():
    red = "\033[31m"
    blue = "\033[34m"
    black = "\033[30m"
    reset = "\033[0m"
    ascii_art = f"""{red}
 █████╗ ██╗  ████████╗███████╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔══██╗██║  ╚══██╔══╝██╔════╝██╔══██╗██║ ██╔╝██╔════╝╚██╗ ██╔╝
███████║██║     ██║   █████╗  ██████╔╝█████╔╝ █████╗   ╚████╔╝ 
██╔══██║██║     ██║   ██╔══╝  ██╔══██╗██╔═██╗ ██╔══╝    ╚██╔╝  
██║  ██║███████╗██║   ███████╗██║  ██║██║  ██╗███████╗   ██║   
╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   
{reset}"""
    print(ascii_art)
    print(blue + "T H E   A L T E R N A T I N G   C I P H E R" + reset, end=" ")
    print(red + "Version 1.00" + reset)
    print(black + "By Joshua M Clatney - Ethical Pentesting Enthusiast" + reset)
    print("-----------------------------------------------------")
    print("Options:")
    print("1. Encrypt text")
    print("2. Decrypt text\n")

def encrypt(text: str, keyword: str) -> str:
    text = text.upper()
    keyword = keyword.upper()
    k = len(keyword)
    plain_alpha = [c for c in text if c.isalpha()]
    encrypted_alpha = []
    total_letters = len(plain_alpha)
    block_count = (total_letters + k - 1) // k 

    for block_index in range(block_count):
        start = block_index * k
        end = start + k
        block = plain_alpha[start:end]
        if block_index % 2 == 0:
            key_block = keyword[:len(block)]
        else:
            key_block = plain_alpha[start - k:start]
        for i, char in enumerate(block):
            shift = ord(key_block[i]) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_alpha.append(encrypted_char)
    result = []
    alpha_index = 0
    for char in text:
        if char.isalpha():
            result.append(encrypted_alpha[alpha_index])
            alpha_index += 1
        else:
            result.append(char)
    return "".join(result)

def decrypt(cipher_text: str, keyword: str) -> str:
    cipher_text = cipher_text.upper()
    keyword = keyword.upper()
    k = len(keyword)
    cipher_alpha = [c for c in cipher_text if c.isalpha()]
    decrypted_alpha = []
    
    total_letters = len(cipher_alpha)
    block_count = (total_letters + k - 1) // k

    for block_index in range(block_count):
        start = block_index * k
        end = start + k
        block = cipher_alpha[start:end]
        if block_index % 2 == 0:
            key_block = keyword[:len(block)]
        else:
            key_block = decrypted_alpha[start - k:start]
        for i, char in enumerate(block):
            shift = ord(key_block[i]) - ord('A')
            plain_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            decrypted_alpha.append(plain_char)
    result = []
    alpha_index = 0
    for char in cipher_text:
        if char.isalpha():
            result.append(decrypted_alpha[alpha_index])
            alpha_index += 1
        else:
            result.append(char)
    return "".join(result)

def process_encrypt():
    text = input("Enter text to encrypt: ")
    keyword = input("Enter keyword: ").replace(" ", "")
    
    text = text.upper()
    keyword = keyword.upper()
    
    if not any(c.isalpha() for c in text):
        print("Error: Text must contain at least one alphabetic character.")
        return

    if not keyword.isalpha() or keyword == "":
        print("Error: Keyword must consist of alphabetic characters only.")
        return

    result = encrypt(text, keyword)
    print("\nEncrypted text:", result)

def process_decrypt():
    text = input("Enter text to decrypt: ")
    keyword = input("Enter keyword: ").replace(" ", "")
    
    text = text.upper()
    keyword = keyword.upper()
    
    if not any(c.isalpha() for c in text):
        print("Error: Text must contain at least one alphabetic character.")
        return

    if not keyword.isalpha() or keyword == "":
        print("Error: Keyword must consist of alphabetic characters only.")
        return

    result = decrypt(text, keyword)
    print("\nDecrypted text:", result)

def main():
    while True:
        clear_screen()
        print_home_screen()
        choice = input("Choose an option (1 or 2): ").strip()
        if choice == '1':
            process_encrypt()
        elif choice == '2':
            process_decrypt()
        else:
            print("Invalid option. Please choose 1 or 2.")

        input("\nPress Enter to return to the home screen...")

if __name__ == "__main__":
    main()