import discord

# Kanal kimliğini almak için kullanılan fonksiyon


def kanal_kimligi_al(ismi: str, sunucu: discord.Guild) -> int:
    for kanal in sunucu.channels:
        if kanal.name == ismi:
            return kanal.id
    return None
