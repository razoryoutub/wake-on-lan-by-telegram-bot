from aiogram import Bot, Dispatcher, executor, types
import asyncio
import aiohttp
from wakeonlan import send_magic_packet

mac = '14.DD.A9.79.4F.41'
token = '1225831912:AAG60sUGFoeRVePSufgLFM0Xaat176T2t1o'
bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['wake'])
async def wake_by_massage(message: types.Message):
	if message.from_user.id == 214196761:
		send_magic_packet(mac, ip_address = 192.168.0.100)
		await message.answer('Разбудил ' + mac)
	else:
		await message.answer('Ты не мой повелитель УХАДИ!!')

@dp.message_handler( content_types=['text'])
async def by_massage(message: types.Message):
	await message.answer(message.text)


if __name__ == '__main__':	
	executor.start_polling(dp, skip_updates=True)