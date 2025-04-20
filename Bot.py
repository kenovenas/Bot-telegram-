# Gerar novo código com suporte a dois canais de origem e filtro de mensagem
codigo_bot_completo = """
from telethon import TelegramClient, events
import os

# === SEUS DADOS ===
api_id = 20225004
api_hash = '8f4c78e858658cd2aa21967a087bf819'
phone_number = '+5519971432718'

# === Canais ===
canais_origem = [
    'https://t.me/+pWGgztndN9dlZjkx',
    'https://t.me/+eHQosWdSn-ZmMDEx'
]
canal_destino = 'https://t.me/+pHVeR_oSuldmMzFh'

# === INICIALIZAÇÃO DO CLIENTE ===
client = TelegramClient('sessao_usuario', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)
    print("Bot iniciado e aguardando mensagens...")

    @client.on(events.NewMessage(chats=canais_origem))
    async def handler(event):
        texto = event.raw_text
        if texto.startswith("Entrada confirmada"):
            try:
                await client.send_message(canal_destino, event.message)
                print("Mensagem replicada:", texto)
            except Exception as e:
                print("Erro ao enviar mensagem:", e)
        else:
            print("Mensagem ignorada:", texto)

    await client.run_until_disconnected()

# === EXECUTA O BOT ===
if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
"""

# Salvar no arquivo replicador.py
file_path_completo = "/mnt/data/replicador.py"
with open(file_path_completo, "w") as f:
    f.write(codigo_bot_completo)

file_path_completo
