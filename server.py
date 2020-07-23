import asyncio

from aiogram import Dispatcher, types, executor

from app import get_bot
from app import database
from app.models import Word

bot = get_bot()
dp = Dispatcher(bot)

@dp.message_handler(types.ChatType.is_private, commands=['start', 'help'])  
async def send_help(message: types.Message):
    text = ('*/add [eng] [rus] - add new word\n'
            '*/list* - show your words\n'
            '*/del [index] - delete a word')
    await message.answer(text)

@dp.message_handler(types.ChatType.is_private, commands='add')
async def add_new_word(message: types.Message):
    text = message.text.replace('/add ', '')
    try: 
        english_word, russian_word = text.split()
    except UnboundLocalError: 
        return await message.answer('Error! Use /add [english word] [russian word].')
    await Word.create(english_word=english_word,
                      russian_word=russian_word)
    await message.answer(f'Word "{english_word}" was added.')

@dp.message_handler(types.ChatType.is_private, commands='list')
async def send_words_list(message: types.Message):
    text = ''
    for index, word in enumerate(await Word.all(), 1):
        text += f'*{index}.* {word.english_word} : {word.russian_word}\n' 
    await message.answer(text)


@dp.message_handler(types.ChatType.is_private, commands='del')
async def del_word(message: types.Message):
    try:
        index = int(message.text.replace('/del ', ''))
    except ValueError:
        return await message.answer('Error! Use /del [index] to delete a word.')
    for id, word in enumerate(await Word.all(), 1):
        if index == id:
            await word.delete()
            return await message.answer(f'Word {word.english_word} was deleted.')
    await message.answer(f'Word with index {index} not found.')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(database.init())
    executor.start_polling(dp, skip_updates=True)
    loop.close()