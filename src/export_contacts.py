from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty


api_id = '25404166'
api_hash = 'b0716cb3781fb970b2c13814be1e4472'
phone_number = '+237681297063'

client = TelegramClient(phone_number, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Entrez le code reçu : '))

dialogs = client(GetDialogsRequest(
    offset_date=None,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=200,
    hash=0
)).chats

print("Groupes disponibles :")
for i, chat in enumerate(dialogs):
    print(f'{i} - {chat.title}')

group_index = int(input("Sélectionnez le numéro du groupe : "))
target_group = dialogs[group_index]


members = client.get_participants(target_group)

# Sauvegarder les contacts dans un fichier
with open(f'contacts.csv', 'w', encoding='utf-8') as f:
    f.write('Nom,Username,ID\n')
    for user in members:
        name = f"{user.first_name or ''} {user.last_name or ''}".strip()
        username = user.username or ''
        user_id = user.id
        f.write(f'{name},{username},{user_id}\n')

print("Contacts sauvegardés dans 'contacts.csv'")
client.disconnect()
