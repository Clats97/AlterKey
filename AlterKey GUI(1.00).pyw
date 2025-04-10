import tkinter as tk
from tkinter import messagebox

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

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The Alternating Cipher GUI - Version 1.00")
        self.geometry("600x650")
        self.frames = {}
        for F in (HomeFrame, EncryptFrame, DecryptFrame):
            frame = F(parent=self, controller=self)
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)
        self.show_frame(HomeFrame)
    
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

class HomeFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ascii_art = (
            " █████╗ ██╗  ████████╗███████╗██████╗ ██╗  ██╗███████╗██╗   ██╗\n"
            "██╔══██╗██║  ╚══██╔══╝██╔════╝██╔══██╗██║ ██╔╝██╔════╝╚██╗ ██╔╝\n"
            "███████║██║     ██║   █████╗  ██████╔╝█████╔╝ █████╗   ╚████╔╝ \n"
            "██╔══██║██║     ██║   ██╔══╝  ██╔══██╗██╔═██╗ ██╔══╝    ╚██╔╝  \n"
            "██║  ██║███████╗██║   ███████╗██║  ██║██║  ██╗███████╗   ██║   \n"
            "╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   \n"
        )
        label_art = tk.Label(self, text=ascii_art, font=("Courier", 10), fg="red", justify="left")
        label_art.pack(pady=5)
        label_title = tk.Label(self, text="T H E   A L T E R N A T I N G   C I P H E R", font=("Courier", 16), fg="blue")
        label_title.pack()
        label_version = tk.Label(self, text="Version 1.00", font=("Courier", 16), fg="red")
        label_version.pack()
        label_by = tk.Label(self, text="By Joshua M Clatney - Ethical Pentesting Enthusiast", font=("Arial", 12), fg="black")
        label_by.pack(pady=5)
        divider = tk.Label(self, text="-----------------------------------------------------")
        divider.pack(pady=5)
        label_options = tk.Label(self, text="Options:", font=("Arial", 14, "bold"))
        label_options.pack(pady=5)

        btn_encrypt = tk.Button(self, text="Encrypt Text", width=20,
                                command=lambda: controller.show_frame(EncryptFrame))
        btn_encrypt.pack(pady=10)

        btn_decrypt = tk.Button(self, text="Decrypt Text", width=20,
                                command=lambda: controller.show_frame(DecryptFrame))
        btn_decrypt.pack(pady=10)

class EncryptFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Encrypt Text", font=("Arial", 14))
        label.pack(pady=10)
        self.text_frame = tk.Frame(self)
        self.text_frame.pack(pady=5)
        self.text_label = tk.Label(self.text_frame, text="Enter text to encrypt:")
        self.text_label.pack(anchor="w")
        self.text_input = tk.Text(self.text_frame, height=5, width=45)
        self.text_input.pack(side=tk.LEFT)
        btn_paste_text = tk.Button(self.text_frame, text="Paste", command=self.paste_text)
        btn_paste_text.pack(side=tk.LEFT, padx=5)
        self.key_frame = tk.Frame(self)
        self.key_frame.pack(pady=5)
        self.key_label = tk.Label(self.key_frame, text="Enter keyword:")
        self.key_label.pack(anchor="w")
        self.key_entry = tk.Entry(self.key_frame, width=45)
        self.key_entry.pack(side=tk.LEFT)
        btn_paste_key = tk.Button(self.key_frame, text="Paste", command=self.paste_key)
        btn_paste_key.pack(side=tk.LEFT, padx=5)       
        btn_process = tk.Button(self, text="Encrypt", command=self.process_encrypt)
        btn_process.pack(pady=10)
        self.output_frame = tk.Frame(self)
        self.output_frame.pack(pady=5)
        self.result_label = tk.Label(self.output_frame, text="Encrypted text:", font=("Arial", 12))
        self.result_label.pack(anchor="w")
        self.result_output = tk.Text(self.output_frame, height=5, width=45, state="disabled")
        self.result_output.pack(side=tk.LEFT)
        btn_copy_output = tk.Button(self.output_frame, text="Copy", command=self.copy_output)
        btn_copy_output.pack(side=tk.LEFT, padx=5)
        
        btn_home = tk.Button(self, text="Return Home", command=lambda: controller.show_frame(HomeFrame))
        btn_home.pack(pady=10)

    def paste_text(self):
        try:
            clipboard_text = self.controller.clipboard_get()
            self.text_input.delete("1.0", tk.END)
            self.text_input.insert(tk.END, clipboard_text)
        except tk.TclError:
            messagebox.showerror("Clipboard Error", "No text in clipboard.")

    def paste_key(self):
        try:
            clipboard_text = self.controller.clipboard_get()
            self.key_entry.delete(0, tk.END)
            self.key_entry.insert(0, clipboard_text)
        except tk.TclError:
            messagebox.showerror("Clipboard Error", "No text in clipboard.")
            
    def copy_output(self):
        output_text = self.result_output.get("1.0", tk.END).strip()
        if output_text:
            self.controller.clipboard_clear()
            self.controller.clipboard_append(output_text)
            messagebox.showinfo("Copied", "Output text copied to clipboard.")
        else:
            messagebox.showerror("Copy Error", "No text to copy.")
            
    def process_encrypt(self):
        text = self.text_input.get("1.0", tk.END).strip()
        keyword = self.key_entry.get().replace(" ", "").upper()
        text = text.upper()

        if not any(c.isalpha() for c in text):
            messagebox.showerror("Input Error", "Text must contain at least one alphabetic character.")
            return
        if not keyword.isalpha() or keyword == "":
            messagebox.showerror("Input Error", "Keyword must consist of alphabetic characters only.")
            return

        result = encrypt(text, keyword)
        self.result_output.config(state="normal")
        self.result_output.delete("1.0", tk.END)
        self.result_output.insert(tk.END, result)
        self.result_output.config(state="disabled")

class DecryptFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Decrypt Text", font=("Arial", 14))
        label.pack(pady=10)
        self.text_frame = tk.Frame(self)
        self.text_frame.pack(pady=5)
        self.text_label = tk.Label(self.text_frame, text="Enter text to decrypt:")
        self.text_label.pack(anchor="w")
        self.text_input = tk.Text(self.text_frame, height=5, width=45)
        self.text_input.pack(side=tk.LEFT)
        btn_paste_text = tk.Button(self.text_frame, text="Paste", command=self.paste_text)
        btn_paste_text.pack(side=tk.LEFT, padx=5)
        self.key_frame = tk.Frame(self)
        self.key_frame.pack(pady=5)
        self.key_label = tk.Label(self.key_frame, text="Enter keyword:")
        self.key_label.pack(anchor="w")
        self.key_entry = tk.Entry(self.key_frame, width=45)
        self.key_entry.pack(side=tk.LEFT)
        btn_paste_key = tk.Button(self.key_frame, text="Paste", command=self.paste_key)
        btn_paste_key.pack(side=tk.LEFT, padx=5)       
        btn_process = tk.Button(self, text="Decrypt", command=self.process_decrypt)
        btn_process.pack(pady=10)
        self.output_frame = tk.Frame(self)
        self.output_frame.pack(pady=5)
        self.result_label = tk.Label(self.output_frame, text="Decrypted text:", font=("Arial", 12))
        self.result_label.pack(anchor="w")
        self.result_output = tk.Text(self.output_frame, height=5, width=45, state="disabled")
        self.result_output.pack(side=tk.LEFT)
        btn_copy_output = tk.Button(self.output_frame, text="Copy", command=self.copy_output)
        btn_copy_output.pack(side=tk.LEFT, padx=5)
        btn_home = tk.Button(self, text="Return Home", command=lambda: controller.show_frame(HomeFrame))
        btn_home.pack(pady=10)

    def paste_text(self):
        try:
            clipboard_text = self.controller.clipboard_get()
            self.text_input.delete("1.0", tk.END)
            self.text_input.insert(tk.END, clipboard_text)
        except tk.TclError:
            messagebox.showerror("Clipboard Error", "No text in clipboard.")

    def paste_key(self):
        try:
            clipboard_text = self.controller.clipboard_get()
            self.key_entry.delete(0, tk.END)
            self.key_entry.insert(0, clipboard_text)
        except tk.TclError:
            messagebox.showerror("Clipboard Error", "No text in clipboard.")

    def copy_output(self):
        output_text = self.result_output.get("1.0", tk.END).strip()
        if output_text:
            self.controller.clipboard_clear()
            self.controller.clipboard_append(output_text)
            messagebox.showinfo("Copied", "Output text copied to clipboard.")
        else:
            messagebox.showerror("Copy Error", "No text to copy.")

    def process_decrypt(self):
        text = self.text_input.get("1.0", tk.END).strip()
        keyword = self.key_entry.get().replace(" ", "").upper()
        text = text.upper()

        if not any(c.isalpha() for c in text):
            messagebox.showerror("Input Error", "Text must contain at least one alphabetic character.")
            return
        if not keyword.isalpha() or keyword == "":
            messagebox.showerror("Input Error", "Keyword must consist of alphabetic characters only.")
            return

        result = decrypt(text, keyword)
        self.result_output.config(state="normal")
        self.result_output.delete("1.0", tk.END)
        self.result_output.insert(tk.END, result)
        self.result_output.config(state="disabled")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
