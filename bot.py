import pyrogram 
import random
from pyrogram import Client, filters 
from pyrogram.types import Message 




api_id = 26597515 
api_hash = "ea74a2439c1f8fff561d8d86af6f1540"
bot_token = "6997698261:AAEiJJIQ_fy8PlQdUIdQLpw7V4h1rX4byBM"



app = Client(
     "ask_test",
     api_id=api_id,
     api_hash=api_hash,
     bot_token=bot_token
     )


OWNER_ID = 6905940236


# /start komutunu özel mesajlarda dinleyen bir handler tanımlıyoruz.
@app.on_message(filters.command(["start"]) & filters.private)
 async def start (client,message):
      # butonları içeren bir klavye oluşturuyoruz.
      keyboard = InlineKeyboardMarkup(
           inline_keyboard=[
                [
                   # ilk buton destek chatine yönlendiriyor.
                   InlineKeyboardButton(text="Destek 🛠", url="https://t.me/yikilmayanchat")
                ],
                [
                   # ikinci buton sahibin profiline yönlendiriyor.
                   InlineKeyboardButton(text="Owner 🐞", user_id=OWNER_ID)
                ]
           ]
      ) 
      # kullanıcıya yanıt olarak bir mesaj gönderiyoruz ve klavyeyi ekliyoruz.
      await message.reply("Merhaba, ben test deneme butonuyum. Aşağıdaki butonlardan birini seçebilirsiniz:",
           reply_markup=keyboard
      )     






# slapmessages örnekleri
slapmessages = [
    "{}, {}'in yüzüne tükürdü!",
    "{}, {}'i tekmeledi!",
    "{}, {}'e tokat attı!",
    "{}, {}'i itti!",
    "{}, {}'in saçını çekti!",
    "{}, {}'e su fırlattı!",
    "{}, {}'i güldürdü!",
    "{}, {}'i şok etti!",
    "{}, {}'in üstüne kahve döktü!"
]

@app.on_message(filters.command(["sille"]) & filters.private)
async def sille(client, message):
    # Komutun bir yanıt olup olmadığını kontrol ediyoruz
    if not message.reply_to_message:
        await message.reply("Bu komutu kullanmak için bir mesajı yanıtlamalısınız.")
        return

    # Yanıtlayan kişinin (gönderici) ve yanıtlanan kişinin (hedef) bilgilerini alıyoruz
    sender = message.from_user
    target = message.reply_to_message.from_user

    # Eğer yanıtlanan kişi OWNER_ID ise özel bir mesaj gönderiyoruz
    if target.id == OWNER_ID:
        await message.reply("Beni tokatlayamazsın!")
        return

    # Yanıtlayan ve yanıtlanan kişinin mentionlarını alıyoruz
    sender_mention = sender.mention
    target_mention = target.mention

    # Rastgele bir slap mesajı seçiyoruz ve isimlerle dolduruyoruz
    slap_message = random.choice(slapmessages).format(sender_mention, target_mention)

    # Yanıtlanan mesaja gönderilecek mesajı oluşturuyoruz
    await message.reply_to_message.reply(slap_message)








@app.on_message(filters.command("kole") & filters.group) 
async def kole(client, message):
     
    if message.from_user.id == 6905940236:
         await message.reply_text("**Sayın sahibim!şu an sorunsuz çalışıyorum.**")

    elif message.from_user.id == 7142242630:
          await message.reply_text("**tırrek sassy çalışıyorum tabiki.**")
                     
    elif message.from_user.id == 7131686379:
          await message.reply_text("** titrek karı delisin ama ben kadar değil,yorma pls.**")

    elif message.from_user.id == 7182074621:
          await message.reply_text("**sedo kardaşım sen konuşma, sen kimdir dfhkslflzjcx**")

    elif message.from_user.id == 6604549799:
          await message.reply_text("**dayı beni öldürdüler dayı,kurtar beni bunların elinden**")

    elif message.from_user.id == 2040437974:
          await message.reply_text("**göttü can kardaşım, sen iste bütün botları çalıştırayım.**")

    elif message.from_user.id == 6716279900:
          await message.reply_text("**maymuş sen iste tüm maymunları köle yapayım sana.**") 

    elif message.from_user.id == 6423044130:
          await message.reply_text("**sahibimin canı canı**")

    else:
       await message.reply_text("**seni tanımıyorum sen de kimsin.**")




# yeni bir kullanıcı gruba katıldığında çalışacak
@app.on_message(filters.new_chat_members)  # yeni bir kullanıcı gruba katıldığında bu fonksiyon tetiklenecek
def welcome(client, message):  # hoş geldin mesajı fonksiyonunu tanımlıyoruz
    for member in message.new_chat_members:  # yeni katılan her kullanıcı için döngü başlatıyoruz
        if member.id == OWNER_ID:  # eğer katılan kullanıcı bot sahibiyse
            message.reply(f"Hoş geldiniz, {member.mention}! Botun sahibinin gruba katılması büyük bir onur.")  # özel bir hoş geldin mesajı gönderiyoruz
        else:  # Eğer katılan kullanıcı bot sahibi değilse
            message.reply(f"Hoş geldiniz, {member.mention}! Grubumuza katıldığınız için mutluyuz.")  # genel hoş geldin mesajı gönderiyoruz



# Bir kullanıcı gruptan ayrıldığında çalışacak fonksiyon
@app.on_message(filters.left_chat_member)
def goodbye(client, message):
    member = message.left_chat_member
    if member.id == OWNER_ID:
        message.reply(f"Maalesef, {member.mention} gruptan ayrıldı. Umarız tekrar gelirsin!")
    else:
        message.reply(f"Hoşça kal, {member.mention}. Seni özleyeceğiz!")




app.run()
