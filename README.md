# AlterKey
A custom, unique, and highly secure poly-alphabetic substitution cipher based on the Vigenere Autokey cipher.

# The Alternating Cipher (Version 1.00)

This repository contains a Python script that implements a unique “alternating” encryption and decryption system. It’s designed as a strong poly-alphabetic substitution cipher, but is not a standard or tested method. Below is an explanation of its features, inner workings, and usage.

---

## Overview

**Primary Purpose**:  
- Encrypt text using a custom block-based strategy with a user-chosen keyword.  
- Decrypt any text encrypted by the same cipher and keyword.  
- Present an ASCII-art interface with simple menu options.

---

## Features

- **Clear Console UI**: Keeps the interface uncluttered each time you make a choice.
- **ASCII Art Home Screen**: Displays a visually appealing title and version info.
- **Block-Based Cipher**: Uses the keyword and previously processed text to alternate how letters are shifted.
- **Non-Alphabetic Preservation**: Retains any characters that are not letters (punctuation, spaces, numbers) in their original spots.

---

## Core Mechanics

1. **Keyword and Blocks**  
   - The script breaks your input (letters only) into chunks (“blocks”) of length equal to your keyword’s length.
   - For **even** chunks (0th, 2nd, 4th, etc.), it uses the keyword directly.
   - For **odd** chunks (1st, 3rd, 5th, etc.), it uses the **previous chunk** of the text (after encryption or decryption) as the “key.”
   - Here's a clear step-by-step explanation of how your script encrypts the phrase:

**Phrase:**  

The quick brown fox jumped over the lazy dog

### Step 1: Choose a Keyword  
For this example, let's use the keyword **"JOSH"**.

### Step 2: Preprocessing
The script converts text to uppercase and isolates alphabetic letters.  
THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG

**Total letters (ignoring spaces):**  

THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG

- Keyword length (JOSH) = 4 letters
- Text length = 35 letters (spaces ignored)
- The script will process this text in blocks of 4 letters each.

### Step 3: Block Division & Encryption Logic  
The script alternates between using the keyword and the previously encrypted block for shifting:

- **Even Blocks** (Block 0, 2, 4, etc.): use keyword **"JOSH"**
- **Odd Blocks** (Block 1, 3, 5, etc.): use **previous encrypted block**

**Blocks (4 letters each, or however long your keyword is):**  

Block 0: THEQ (key: JOSH)

Block 1: UICK (key: result of Block 0)

Block 2: BROW (key: JOSH)

Block 3: NFOX (key: result of Block 2)

Block 4: JUMP (key: JOSH)

Block 5: EDOV (key: result of Block 4)

Block 6: ERTH (key: JOSH)

Block 7: ELAZ (key: result of Block 6)

Block 8: YDOG (key: JOSH)

### Step 4: Encrypting Each Block
Let's demonstrate clearly for the first two blocks to illustrate the method:

#### Encrypting Block 0 (`THEQ`) using the keyword `JOSH`:
T (19) shifted by J (9)  → (19+9)=28 mod26 → 2 = C
H (7) shifted by O (14) → (7+14)=21 → V
E (4) shifted by S (18) → (4+18)=22 → W
Q (16) shifted by H (7) → (16+7)=23 → X
Encrypted Block 0: CVWX

#### Encrypting Block 1 (`UICK`) using previous encrypted block `CVWX`:
U (20) shifted by C (2) → 22 = W
I (8) shifted by V (21) → (8+21)=29 mod26=3 → D
C (2) shifted by W (22) → (2+22)=24 → Y
K (10) shifted by X (23) → (10+23)=33 mod26=7 → H
Encrypted Block 1: WDYH

You repeat this process for each subsequent block, alternating between the keyword and previous encrypted block.

### Step 5: Recombine and Preserve Formatting
After all letters are encrypted, the script re-inserts spaces and punctuation in their original positions, preserving readability.

### Why This Matters
This alternating method means the ciphertext continuously evolves. Each encrypted block depends on either the keyword or the previous ciphertext block, significantly increasing complexity compared to simple shift methods.

---

## Usage

1. **Run the Script**  
  Git clone or download the repository.
2. **Home Screen**  
   - You’ll see the script’s ASCII art and version info, plus two main options:
     1. **Encrypt**  
     2. **Decrypt**
3. **Encrypt Process**  
   - Choose option “1” and follow the prompts to input text and keyword.
   - The script returns the encrypted text, preserving spaces and punctuation where they were.
4. **Decrypt Process**  
   - Choose option “2” and enter the text you want to decrypt (originally produced by the script) and the same keyword.
   - The output should match the original text before encryption.
5. **Repeat**  
   - After each operation, press Enter to return to the home screen or exit by entering an invalid choice.

---

## Script Breakdown

1. **`clear_screen()`**  
   - Clears the terminal using `cls` on Windows and `clear` on Unix systems.

2. **`print_home_screen()`**  
   - Displays ASCII art and menu options (encrypt or decrypt).

3. **`encrypt(text, keyword)`** and **`decrypt(cipher_text, keyword)`**  
   - Contain the main logic for shifting letters.  
   - Work block-by-block, using the keyword for even-indexed blocks, and prior output (encrypted or decrypted) for odd-indexed blocks.

4. **`process_encrypt()`** and **`process_decrypt()`**  
   - Prompt the user for text and keyword.  
   - Validate that there are alphabetic characters in the inputs.  
   - Output the results from the respective functions above.

5. **`main()`**  
   - Orchestrates the user interaction in a loop: clear the screen, show the menu, process input, and return to the menu.

---

## Limitations

- **Not a Standard Cipher**: This is a custom approach; it hasn’t been vetted for strong cryptographic security or compared to industry standard encryption methods.
- **Keyword Must Be Alphabetic**: The keyword input expects letters only (no digits or punctuation).  
- **Case Handling**: Internally, everything is converted to uppercase for simplicity.  
- **Corruption Sensitivity**: The decryption of odd blocks depends on the correct decryption of previous blocks, so any errors in the text or keyword will propagate.

--

Enjoy experimenting with **The Alternating Cipher**! Feel free to open an issue or submit a pull request with any questions or improvements.
