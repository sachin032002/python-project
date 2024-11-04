import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Initialize the Translator object
translator = Translator()

# Function to perform translation
def translate_text():
    source_lang = source_lang_combo.get()
    target_lang = target_lang_combo.get()
    text_to_translate = source_text.get("1.0", tk.END).strip()

    if not text_to_translate:
        messagebox.showerror("Error", "Please enter text to translate")
        return
    
    try:
        # Perform translation
        translation = translator.translate(text_to_translate, src=source_lang, dest=target_lang)
        translated_text.delete("1.0", tk.END)
        translated_text.insert(tk.END, translation.text)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {str(e)}")

# Function to clear text fields
def clear_text():
    source_text.delete("1.0", tk.END)
    translated_text.delete("1.0", tk.END)

# Create main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("900x650")
root.configure(bg="#444d68")  # Light professional background color

# Title Label
title_label = tk.Label(root, text="Language Translator", font=("Georgia", 22, "bold"), fg="cyan", bg="#444d68")
title_label.pack(pady=20)

# Frame for language selection
frame = tk.Frame(root, bg="#444d68")
frame.pack(pady=10)

# Dropdown for source language
source_lang_label = tk.Label(frame, text="Source Language:",font=("Arial", 12,"bold"), bg="#444d68" ,fg="white")
source_lang_label.grid(row=0, column=0, padx=10, pady=10)

source_lang_combo = ttk.Combobox(frame, width=25, state="readonly", font=("Arial", 11))
source_lang_combo["values"] = list(LANGUAGES.values())
source_lang_combo.grid(row=0, column=1, padx=10, pady=10)
source_lang_combo.current(21)  # Set default to English

# Dropdown for target language
target_lang_label = tk.Label(frame, text="Target Language:", font=("Arial", 12,"bold"), bg="#444d68", fg="white")
target_lang_label.grid(row=1, column=0, padx=10, pady=10)

target_lang_combo = ttk.Combobox(frame, width=25, state="readonly", font=("Arial", 11))
target_lang_combo["values"] = list(LANGUAGES.values())
target_lang_combo.grid(row=1, column=1, padx=10, pady=10)
target_lang_combo.current(38)  # Set default to Hindi

# Textbox for source text
source_text_label = tk.Label(root, text="Enter Text to Translate:", font=("Arial", 12,"bold"), bg="#444d68", fg="white")
source_text_label.pack(pady=5)

source_text = tk.Text(root, height=5, width=60, font=("Arial", 12), bg="#ECF0F1", fg="#34495E", bd=0, highlightthickness=1, highlightbackground="#BDC3C7")
source_text.pack(pady=10)

# Translate Button
translate_button = tk.Button(root, text="Translate", command=translate_text, bg="#1ABC9C", fg="white", font=("Arial", 14, "bold"), width=20)
translate_button.pack(pady=5)

# Textbox for translated text
translated_text_label = tk.Label(root, text="Translated Text:", font=("Arial", 12,"bold"), bg="#444d68", fg="white")
translated_text_label.pack(pady=5)

translated_text = tk.Text(root, height=5, width=60, font=("Arial", 12), bg="#ECF0F1", fg="#34495E", bd=0, highlightthickness=1, highlightbackground="#BDC3C7")
translated_text.pack(pady=10)

# Clear Button
clear_button = tk.Button(root, text="Clear", command=clear_text, bg="#E74C3C", fg="white", font=("Arial", 14, "bold"), width=20)
clear_button.pack(pady=10)

# Add a footer with subtle styling
footer_label = tk.Label(root, text="© 2024 Translator App. All rights reserved.", font=("Arial", 10), bg="#444d68", fg="black")
footer_label.pack(side="bottom", pady=20)

# Start the Tkinter main loop
root.mainloop()