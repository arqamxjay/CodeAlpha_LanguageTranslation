import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

def translate_text():
    try:
        source_text = entry_text.get()
        target_lang = lang_map[lang_combo.get()]
        
        # Translation logic
        translated = GoogleTranslator(source='auto', target=target_lang).translate(source_text)
        
        output_label.config(text=f"Expected output: \"{translated}\"", fg="green")
    except Exception as e:
        output_label.config(text="Error: Could not translate", fg="red")

# Mapping display names to language codes
lang_map = {"Spanish": "es", "French": "fr", "German": "de", "Japanese": "ja"}

# GUI Setup
root = tk.Tk()
root.title("Project 1: Translation Tool")
root.geometry("400x250")

# 1. Title
tk.Label(root, text="### Project 1: Translation Tool", font=("Arial", 12, "bold")).pack(pady=10)

# 2. Language Selection
tk.Label(root, text="Select Target Language:").pack()
lang_combo = ttk.Combobox(root, values=list(lang_map.keys()))
lang_combo.current(0) # Default to Spanish
lang_combo.pack(pady=5)

# 3. Text Entry
tk.Label(root, text="Enter text:").pack()
entry_text = tk.Entry(root, width=40)
entry_text.insert(0, "Hello, how are you?")
entry_text.pack(pady=5)

# 4. Translate Button
btn = tk.Button(root, text="Translate", command=translate_text)
btn.pack(pady=10)

# 5. Output
output_label = tk.Label(root, text="Expected output: ", font=("Arial", 10, "italic"))
output_label.pack(pady=10)

root.mainloop()
