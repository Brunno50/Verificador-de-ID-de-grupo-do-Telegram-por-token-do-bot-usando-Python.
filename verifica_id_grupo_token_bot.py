import asyncio
import tkinter as tk
from tkinter import messagebox, scrolledtext
from telegram import Bot

# Função para listar os grupos do bot
async def listar_grupos_do_bot(token, output_text):
    try:
        bot = Bot(token=token)
        
        # Obtendo as atualizações (últimas mensagens ou eventos do bot)
        updates = await bot.get_updates()
        
        # Dicionário para armazenar os IDs dos grupos
        grupos_ids = set()

        for update in updates:
            if update.message and update.message.chat.type in ["group", "supergroup"]:
                grupos_ids.add(update.message.chat.id)

        # Atualizar o texto de saída
        output_text.delete(1.0, tk.END)
        if grupos_ids:
            output_text.insert(tk.END, "Grupos em que o bot está presente:\n")
            for group_id in grupos_ids:
                output_text.insert(tk.END, f"ID do Grupo: {group_id}\n")
        else:
            output_text.insert(tk.END, "Nenhum grupo encontrado.")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função para iniciar a execução da função assíncrona
def buscar_grupos():
    token = token_entry.get()
    if token:
        asyncio.run(listar_grupos_do_bot(token, output_text))
    else:
        messagebox.showwarning("Aviso", "Por favor, insira o token do bot.")

# Interface gráfica com Tkinter
root = tk.Tk()
root.title("Verificar Grupos do Bot Telegram")
root.geometry("400x300")

# Campo de entrada para o token do bot
tk.Label(root, text="Insira o Token do Bot:").pack(pady=10)
token_entry = tk.Entry(root, width=40)
token_entry.pack()

# Botão para iniciar a busca pelos grupos
buscar_button = tk.Button(root, text="Buscar Grupos", command=buscar_grupos)
buscar_button.pack(pady=10)

# Área de texto para mostrar o resultado
output_text = scrolledtext.ScrolledText(root, width=45, height=10)
output_text.pack(pady=10)

# Executa a interface
root.mainloop()
