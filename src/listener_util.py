import logic
import re

from messages import *
from repository import Repository
from bot import bot


async def start(bot: bot):
    repository = Repository()
    async for event in bot.listen():
        chat_id = event.message.chat.id
        if event.message.chat.type != 'private':
            # Greeting message when the bot has been added to the conversation.
            if event.message.new_chat_members is not None:
                if any((await bot.get_me()).id == x.id for x in event.message.new_chat_members):
                    await bot.send_message(chat_id, GREETING + logic.curr_week_msg())
                    print(f'bot is added to chat {chat_id}')

            elif event.message.text is not None:
                # Message with setup instructions.
                if re.search('@parityhelper_bot.+(?:помощь|help)', event.message.text):
                    await bot.send_message(chat_id, SETTING + logic.curr_week_msg())

                # Setup process.
                elif '@parityhelper_bot' in event.message.text:
                    splitted = event.message.text.replace('@parityhelper_bot', '').strip(',').split('|')
                    # If setup message is correct.
                    if len(splitted) == 2:
                        even_week_name = splitted[0].strip()
                        odd_week_name = splitted[1].strip()
                        # If the bot is an admin.
                        user_bot = await bot.get_me()
                        if await bot.is_user_admin_in_chat(user_bot.id, chat_id):
                            # If a user is an admin.
                            user_id = event.message.message_from.id
                            if await bot.is_user_admin_in_chat(user_id, chat_id):
                                # Repository update.
                                repository.change_chat(chat_id, even_week_name, odd_week_name)
                                await bot.send_message(chat_id, SUCCESS)
                                new_name = odd_week_name if logic.get_curr_week_parity() else even_week_name
                                await bot.change_chat_title(chat_id, new_name)
                                print(f'bot is updated in chat {chat_id}')
                            else:
                                await bot.send_message(chat_id, USER_IS_NOT_ADMIN)
                        else:
                            await bot.send_message(chat_id, BOT_IS_NOT_ADMIN)
                    else:
                        await bot.send_message(chat_id, ERROR)
                        await bot.send_message(chat_id, SETTING + logic.curr_week_msg())
