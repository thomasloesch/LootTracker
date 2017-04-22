import requests

payload = {'fields': 'achievements%2Cchallenge', 'locale': 'en_US', 'apikey': 'k9yk5s6sn23zr4hspn5mjmngw59j9854'}
r = Requests.get('https://us.api.battle.net/wow/guild/Stormrage/Scarlet%20Crusaders', params=payload)

print(r.url)
