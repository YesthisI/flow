# decode.py
import base64

with open('flowgo-full.zip.base64', 'r') as f:
    content = f.read()

# Очищаем от лишних символов
content = ''.join(c for c in content if c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=')

# Декодируем
data = base64.b64decode(content)

# Сохраняем как ZIP
with open('flowgo-full.zip', 'wb') as f:
    f.write(data)

print("✅ Успешно декодировано: flowgo-full.zip")
