TOOL_DEFINITION = {
    "type": "function",
    "function": {
        "name": "count_words",
        "description": "Verilen metindeki kelime sayısını sayar ve sonucu döner.",
        "parameters": {
            "type": "object",
            "properties": {
                "metin": {
                    "type": "string",
                    "description": "Kelime sayısı hesaplanacak metin",
                },
            },
            "required": ["metin"],
        },
    },
}


def count_words(metin: str) -> str:
    kelime_sayisi = len(metin.split())
    return f"Metindeki kelime sayısı: {kelime_sayisi}"
