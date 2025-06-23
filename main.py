import asyncio
from handlers import common
from contextlib import suppress
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from logging import basicConfig, INFO
from aiogram_i18n import I18nMiddleware
from aiogram.client.default import DefaultBotProperties
from aiogram_i18n.cores.fluent_runtime_core import FluentRuntimeCore

TOKEN = ""


async def main():
    basicConfig(level=INFO)
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    # i18n middleware
    i18n = I18nMiddleware(
        core=FluentRuntimeCore(path="locales/{locale}/LC_MESSAGES"),
        default_locale="en"
    )
    i18n.setup(dp)

    dp.include_router(common.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    with suppress(KeyboardInterrupt):
        asyncio.run(main())
