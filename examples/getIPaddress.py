import socket

def get_local_ip():
    try:
        # Opprett en socket-forbindelse for å finne den lokale IP-en
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Koble til en ekstern server (ingen data sendes)
        local_ip = s.getsockname()[0]  # Hent IP-adressen
        s.close()
        return local_ip
    except Exception as e:
        return None  # Returner None hvis det oppstår en feil

# Eksempel på bruk:
# my_ip = get_local_ip()
# print(my_ip)
