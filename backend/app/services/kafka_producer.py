from aiokafka import AIOKafkaProducer
import json


async def send_log_to_kafka(user_id: int, action: str, timestamp: str):
    producer = AIOKafkaProducer(bootstrap_servers='kafka:9092')
    await producer.start()
    try:
        message = {
            'user_id': user_id,
            'action': action,
            'timestamp': timestamp
        }
        await producer.send_and_wait('logs_topic', value=json.dumps(message).encode('utf-8'))
        print(f"Message sent: {message}")
    except Exception as e:
        print(f"Error sending message: {e}")
    finally:
        await producer.stop()
