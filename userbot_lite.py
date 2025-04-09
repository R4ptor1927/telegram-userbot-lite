from pyrogram import Client, filters

api_id = 123456  # Sostituisci con il tuo
api_hash = "your_api_hash"  # Sostituisci con il tuo

app = Client("userbot_lite", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.command("ping", prefixes=".") & filters.me)
async def ping(_, msg):
    await msg.reply("🏓 Pong!")

@app.on_message(filters.command("help", prefixes=".") & filters.me)
async def help_cmd(_, msg):
    text = (
        "📖 Comandi disponibili:\n"
        ".ping – Test connessione\n"
        ".listproducts – Mostra i prodotti disponibili\n\n"
        "🔐 Vuoi la versione completa con PayPal, broadcast e spam automatico?\n"
        "💬 Scrivici su @plasmonplus"
    )
    await msg.reply(text)

@app.on_message(filters.command("listproducts", prefixes=".") & filters.me)
async def listproducts(_, msg):
    prodotti = [
        "💼 Prodotto 1 – Descrizione breve",
        "📦 Prodotto 2 – Descrizione breve",
        "🎁 Prodotto 3 – Descrizione breve"
    ]
    await msg.reply("\n".join(prodotti))

@app.on_message(filters.command("start", prefixes=".") & filters.me)
async def start_notice(_, msg):
    await msg.reply(
        "✨ Benvenuto su UserBotShop Lite!\n"
        "Usa .help per vedere i comandi disponibili.\n\n"
        f"💬 Per la versione PRO → @plasmonplus"
    )

app.run()
