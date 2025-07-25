from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio
from .model import chunk_and_denoise, transcribe_chunks, cleanup

class TranscribeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        audio_path = data.get("audio_path")  # مثل: "media/recording.wav"

        if not audio_path:
            await self.send(text_data=json.dumps({"error": "Audio path not provided"}))
            return

        chunks = chunk_and_denoise(audio_path, chunk_duration=2)

        for i, chunk in enumerate(chunks):
            result = transcribe_chunks([chunk])
            print(result)
            await self.send(text_data=json.dumps({
                "chunk": i,
                "text": result
            }))
            await asyncio.sleep(0.1)  # تمنح الوقت للـ frontend لتحديث نفسه

        cleanup(chunks)
        await self.send(text_data=json.dumps({"done": True}))
