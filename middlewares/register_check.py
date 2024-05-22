from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from db.base import get_user_by_id, create_user


class RegisterCheck(BaseMiddleware):

    def __init__(self):
        pass

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]
    ) -> Any:
        user = event.from_user
        if get_user_by_id(user.id, con=data['con']) is None:
            create_user(user.id, con=data['con'])
            await data['bot'].send_message(user.id, 'You are registered!')

        # Получаем менеджер сессий из ключевых аргументов, переданных в start_polling()
        # if not await is_user_exists(user_id=event.from_user.id, session_maker=session_maker, redis=redis):
        #     await create_user(user_id=event.from_user.id,
        #                       username=event.from_user.username, session_maker=session_maker, locale=user.language_code)
        #     await data['bot'].send_message(event.from_user.id, 'Ты успешно зарегистрирован(а)!')
        return await handler(event, data)
