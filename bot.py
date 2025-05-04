import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler, Application, ContextTypes
import telegram.error

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

FURIA_MATCHES = [
    {
        "time1": "FURIA",
        "time2": "The MongolZ",
        "data": "10/05",
        "hora": "05:00",
        "torneio": "PGL Astana 2025",
    }
]

FURIA_STATS = {
    "win_streak": 0,
    "win_rate": "33.3%",
    "last_5_matches": ["🔴", "🔴", "🔴", "🟢", "🔴"],
    "ranking": "# 17",
    "map_stats": {
        "Dust2": "44.4%",
        "Mirage": "42.9%",
        "Inferno": "40.0%",
        "Train": "40.0%",
        "Anubis": "37.5%",
        "Nuke": "25.0%"
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Bem-vindo ao Bot Furioso de CS:GO!"
    )
    await show_option_buttons(update, context)

async def show_option_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE, from_callback: bool = False) -> None:
    keyboard = [
        [InlineKeyboardButton("Próximos Jogos", callback_data='proximos_jogos')],
        [InlineKeyboardButton("Estatísticas", callback_data='estatisticas')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if from_callback:
        await update.callback_query.edit_message_text(
            text='Escolha uma opção:',
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            text='Escolha uma opção:',
            reply_markup=reply_markup
        )

async def button_selection_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == 'proximos_jogos':
        await show_upcoming_matches(update, context)
    elif query.data == 'estatisticas':
        await show_team_stats(update, context)
    elif query.data == 'voltar':
        await show_option_buttons(update, context, from_callback=True)
    else:
        await query.edit_message_text(f'Você selecionou: {query.data.replace("_"," ").title()}')

async def show_upcoming_matches(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response = "Próximos Jogos da FURIA:\n\n"
    for match in FURIA_MATCHES:
        opponent = match["time2"] if match["time1"] == "FURIA" else match["time1"]
        response += (
            f"🆚 vs {opponent}\n"
            f"📅 {match['data']} às {match['hora']}\n"
            f"🏆 {match['torneio']}\n"
        )
    keyboard = [[InlineKeyboardButton("Voltar", callback_data='voltar')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(
        text=response,
        reply_markup=reply_markup
    )

async def show_team_stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Formata a mensagem de estatísticas
    response = (
        "📊 Estatísticas da FURIA 📊\n\n"
        f"⚡ Current Win Streak: {FURIA_STATS['win_streak']}\n"
        f"📈 Win Rate: {FURIA_STATS['win_rate']}\n"
        f"🏆 World Ranking: {FURIA_STATS['ranking']}\n\n"
        "📅 Últimos 5 resultados:\n"
        f"{' '.join(FURIA_STATS['last_5_matches'])}\n\n"
        "🗺️ Map Stats (últimos 3 meses):\n"
    )
    
    # Adiciona estatísticas dos mapas
    for map_name, win_rate in FURIA_STATS['map_stats'].items():
        response += f"• {map_name}: {win_rate} win rate\n"
    
    # Cria botão de voltar
    keyboard = [[InlineKeyboardButton("↩ Voltar", callback_data='voltar')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(
        text=response,
        reply_markup=reply_markup
    )

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a telegram message to notify the developer."""
    # Only send msg if it's a BadRequest (message not modified)
    if isinstance(context.error, telegram.error.BadRequest):
        if "Message is not modified" in str(context.error):
            return
    
    # Para outros erros, você pode querer notificar o usuário
    try:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Ocorreu um erro inesperado. Por favor, tente novamente."
        )
    except Exception:
        pass

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_selection_handler))
    application.add_error_handler(error_handler)
    application.run_polling()

if __name__ == '__main__':
    main()