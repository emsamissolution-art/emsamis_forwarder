from telethon import TelegramClient, events

# 🔑 Datos de acceso
api_id = 20336552
api_hash = "9411b253c2af05d75a502bf1c77b00f6"
bot_token = "8488581940:AAEBmPZlbor-Isd_qeYE5ANP-tp3MiAvl9w"

# Cliente del bot
bot = TelegramClient('emsamis_forwarder', api_id, api_hash).start(bot_token=bot_token)

# IDs de los canales
source_channel = 1385109737        # Pocket Option Signals (origen)
target_channel = -1002941323953    # EMSAMIS Trading VIP (destino)

@bot.on(events.NewMessage(chats=source_channel))
async def handler(event):
    await bot.send_message(target_channel, event.message)

print("🚀 EMSAMIS Forwarder corriendo en Railway...")
bot.run_until_disconnected()
