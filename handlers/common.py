from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_i18n import I18nContext, LazyFilter
from keyboards.default import main_keyboard

router = Router(name=__name__)


@router.message(CommandStart())
async def start(message: Message, i18n: I18nContext) -> None:
    name = message.from_user.mention_html()
    await message.answer(
        text=i18n.get("hello", user=name),
        reply_markup=main_keyboard
    )


@router.message(LazyFilter("help"))
async def help_handler(message: Message, i18n: I18nContext) -> None:
    await message.answer(i18n.help())


@router.message(F.text.in_(["🇺🇿 Uzbek", "🇷🇺 Русский", "🇬🇧 English"]))
async def language_selector(message: Message, i18n: I18nContext) -> None:
    lang_map = {
        "🇺🇿 Uzbek": "uz",
        "🇷🇺 Русский": "ru",
        "🇬🇧 English": "en"
    }
    selected_locale = lang_map.get(message.text, "en")
    await i18n.set_locale(selected_locale)

    await message.answer(
        i18n.get("hello", user=message.from_user.full_name),
        reply_markup=main_keyboard
    )
