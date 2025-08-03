import discord
from discord.ext import commands, tasks
import os, random
import time
import schedule
import asyncio

TOKEN = "MTMyMjUwOTAzMzg0NzkxODY2NA.GqFfEI.wv2-_a5ahPz1Q14MANOpvMEbR7VPSsdDZqdTl0"
CHANNEL_ID = 1400048022565683200

intents = discord.Intents.default()
client = discord.Client(intents=intents)

TIPS = [
    {
        "judul": "Hemat Energi",
        "teks": "🔌 Cabut charger setelah digunakan.",
        "gambar": "images/hemat_energi.png",
        "youtube": "https://youtu.be/pb6OTxIg3lE?si=AE_7IG__mrtny9SU"
    },
    {
        "judul": "Kurangi Plastik",
        "teks": "🛍️ Gunakan tas belanja sendiri.",
        "gambar": "images/kurangi_plastik.png",
        "youtube": "https://youtu.be/4jIqNRHTg9k?si=teR4JTslY_OgpTFS"
    },
    {
        "judul": "Transportasi Hijau",
        "teks": "🚲 Gunakan sepeda untuk perjalanan dekat.",
        "gambar": "images/transportasi_hijau.png",
        "youtube": "https://youtu.be/8B-d6W-H7H8?si=xnDvfiZM5WFnsDtg"
    },
    {
        "judul": "Tanam Pohon",
        "teks": "🌱 Menanam pohon membantu menyerap karbon dioksida.",
        "gambar": "images/tanam_pohon.png",
        "youtube": "https://youtu.be/8B-d6W-H7H8?si=xnDvfiZM5WFnsDtg"
    },
    {
        "judul": "Daur Ulang",
        "teks": "♻️ Pisahkan sampah organik dan anorganik.",
        "gambar": "images/daur_ulang.png",
        "youtube": "https://youtu.be/8B-d6W-H7H8?si=xnDvfiZM5WFnsDtg"
    }
]

async def send_tip():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        tip = random.choice(TIPS)
        embed = discord.Embed(
            title=f"🌿 Eco Tip: {tip['judul']}",
            description=tip["teks"],
            color=0x00ff88
        )
        embed.set_image(url="attachment://" + os.path.basename(tip["gambar"]))
        embed.add_field(name="📺 Video Terkait", value=tip["youtube"], inline=False)

        with open(tip["gambar"], "rb") as f:
            file = discord.File(f, filename=os.path.basename(tip["gambar"]))
            await channel.send(file=file, embed=embed)

def schedule_task():
    async def wrapper():
        await send_tip()

    def job():
        asyncio.run_coroutine_threadsafe(wrapper(), client.loop)

    schedule.every(24).hours.do(job)

@client.event
async def on_ready():
    print(f"✅ Bot aktif sebagai {client.user}")
    schedule_task()

    async def scheduler():
        while True:
            schedule.run_pending()
            await asyncio.sleep(1)

    client.loop.create_task(scheduler())

client.run("MTMyMjUwOTAzMzg0NzkxODY2NA.GqFfEI.wv2-_a5ahPz1Q14MANOpvMEbR7VPSsdDZqdTl0") 



