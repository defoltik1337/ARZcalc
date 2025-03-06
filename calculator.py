import customtkinter as ctk
from tkinter import messagebox
from customtkinter import CTkImage
from PIL import Image
import webbrowser

def log(message):
    print(f"[DEBUG] {message}")

def show_main_menu():
    log("Открыто главное меню")
    clear_frame()
    add_back_button(None)
    ctk.CTkLabel(frame, text="Выберите игру", font=("Arial", 20), text_color="#E0E0E0").pack(pady=15)
    ctk.CTkButton(frame, text="Minecraft", fg_color="#66BB6A", text_color="black", command=lambda: show_servers('Minecraft')).pack(pady=5)
    ctk.CTkButton(frame, text="SAMP", fg_color="#42A5F5", text_color="black", command=lambda: show_servers('SAMP')).pack(pady=5)
    add_source_button()

def show_servers(game):
    log(f"Выбрана игра: {game}")
    clear_frame()
    add_back_button(show_main_menu)
    ctk.CTkLabel(frame, text=f"Выбрано: {game}", font=("Arial", 18), text_color="#E0E0E0").pack(pady=10)
    servers = ["HolyWorld", "Funtime"] if game == "Minecraft" else ["Servers"]
    for server in servers:
        ctk.CTkButton(frame, text=server, fg_color="#FFCA28", text_color="black", command=lambda s=server: show_calculator(game, s)).pack(pady=5)
    add_source_button()

def show_calculator(game, server):
    log(f"Выбран сервер/режим: {server} в игре {game}")
    clear_frame()
    add_back_button(lambda: show_servers(game))
    ctk.CTkLabel(frame, text=f"{game} - {server}", font=("Arial", 18), text_color="#E0E0E0").pack(pady=10)
    ctk.CTkLabel(frame, text="Введите курс (на 1КК):", text_color="#E0E0E0").pack()
    entry_kurs = ctk.CTkEntry(frame)
    entry_kurs.pack()
    ctk.CTkLabel(frame, text="Введите количество (в КК):", text_color="#E0E0E0").pack()
    entry_amount = ctk.CTkEntry(frame)
    entry_amount.pack()
    ctk.CTkButton(frame, text="Посчитать по курсу", fg_color="#29B6F6", text_color="black", command=lambda: calculate_currency(entry_kurs, entry_amount)).pack(pady=5)
    ctk.CTkButton(frame, text="Прибавить комиссию", fg_color="#FFB74D", text_color="black", command=lambda: calculate_with_fee(entry_amount)).pack(pady=5)
    add_source_button()

def calculate_currency(entry_kurs, entry_amount):
    try:
        kurs = float(entry_kurs.get())
        amount = float(entry_amount.get())
        result = kurs * amount
        log(f"Расчёт по курсу: {amount}КК * {kurs} = {result} рублей")
        messagebox.showinfo("Результат", f"{amount}КК - {result} Рублей")
    except ValueError:
        log("Ошибка ввода данных в курс или количество")
        messagebox.showerror("Ошибка", "Введите корректные числа!")

def calculate_with_fee(entry_amount):
    try:
        amount = float(entry_amount.get())
        result = (amount * 1000000) * 1.08 / 1000000
        log(f"Расчёт с комиссией: {amount}КК * 1.08 = {result:.2f}КК")
        messagebox.showinfo("Результат", f"{amount}КК с комиссией равно {result:.2f}КК")
    except ValueError:
        log("Ошибка ввода количества валюты")
        messagebox.showerror("Ошибка", "Введите корректные числа!")

def png_to_image(path, size=(20, 20)):
    image = Image.open(path).convert("RGBA")
    image = image.resize(size, Image.Resampling.LANCZOS)
    ctk_image = CTkImage(image)
    return ctk_image

def add_back_button(command):
    if command:
        back_icon = png_to_image("back_icon.png")
        ctk.CTkButton(frame, image=back_icon, text="", width=30, fg_color="transparent", command=command).pack(anchor="nw", padx=10, pady=10)

def add_source_button():
    github_icon = png_to_image("github_icon.png")
    ctk.CTkButton(frame, image=github_icon, text="Source Code", fg_color="#24292E", text_color="white", command=lambda: open_github()).pack(side="bottom", pady=10)

def open_github():
    webbrowser.open("https://github.com/defoltik1337/ARZcalc")

def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Калькулятор валюты")
root.geometry("450x400")
root.resizable(False, False)
frame = ctk.CTkFrame(root, fg_color="#2C2C2C")
frame.pack(expand=True, fill='both', padx=15, pady=15)

show_main_menu()
root.mainloop()