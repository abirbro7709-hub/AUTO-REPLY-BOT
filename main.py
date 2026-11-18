import os
from telethon import TelegramClient, events

# আপনার এপিআই আইডি এবং হ্যাস
API_ID = 33878694
API_HASH = "7aab68284eea919e6510b832"

# আপনার কাস্টম অটো-রিপ্লাই মেসেজ এখানে সেট করা আছে
AUTO_REPLY_MESSAGE = """🦋✨ 𝑨𝑺𝑺𝑨𝑳𝑨𝑴𝑼 𝑨𝑳𝑨𝑰𝑲𝑼𝑴 ✨🦋

🌸 আপনার মেসেজের জন্য আন্তরিক ধন্যবাদ! ❤️

╭━━━〔 💌 〕━━━╮
এই মুহূর্তে আমি অনলাইনে নেই। 🥺

আপনার মেসেজটি আমি পেয়েছি। ইনশাআল্লাহ, অনলাইনে ফিরে আসার পর যত দ্রুত সম্ভব আপনার মেসেজের উত্তর দেওয়ার চেষ্টা করব। 💫
╰━━━━━━━━━━━━╯

🤍 𝑷𝒍𝒆𝒂𝒔𝒆 𝑲𝒊𝒏𝒅𝒍𝒚 𝑾𝒂𝒊𝒕...

🌷 আপনার ধৈর্য ও ভালোবাসার জন্য অসংখ্য ধন্যবাদ।

✨ 𝑯𝒂𝒗𝒆 𝒂 𝑵𝒊𝒄𝒆 𝑫𝒂𝒚! 🦋"""

# ইউজারবট সেশন শুরু করা
client = TelegramClient('my_userbot', API_ID, API_HASH)

@client.on(events.NewMessage(incoming=True, private=True))
async def handle_incoming_message(event):
    # শুধু প্রাইভেট চ্যাটে কেউ মেসেজ দিলে অটো রিপ্লাই যাবে
    sender = await event.get_sender()
    
    # বট থেকে মেসেজ আসলে ইগনোর করবে
    if sender.bot:
        return
    
    # অটো-রিপ্লাই পাঠানো
    await event.respond(AUTO_REPLY_MESSAGE)

# মেসেজ দিয়ে অটো-রিপ্লাই টেক্সট আপডেট করার কমান্ড (নিজের চ্যাটে লিখে মেসেজ বদলাতে পারবেন)
@client.on(events.NewMessage(pattern='/setmsg (.+)', outgoing=True))
async def update_message(event):
    global AUTO_REPLY_MESSAGE
    new_msg = event.pattern_match.group(1)
    AUTO_REPLY_MESSAGE = new_msg
    await event.edit(f"✅ অটো-রিপ্লাই মেসেজ সফলভাবে আপডেট করা হয়েছে:\n\n{AUTO_REPLY_MESSAGE}")

def main():
    client.start()
    print("ইউজারবট সফলভাবে চালু হয়েছে এবং কাজ করছে...")
    client.run_until_disconnected()

if __name__ == "__main__":
    main()
  
