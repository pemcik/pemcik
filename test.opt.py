import os
import sys

# Faila lasīšana
def lasit_failu(faila_nosaukums):
    with open(faila_nosaukums, 'rb') as f:
        return f.read()

# Faila rakstīšana
def rakstit_failu(faila_nosaukums, dati):
    with open(faila_nosaukums, 'wb') as f:
        f.write(dati)

# OTP ģenerēšana
def generet_otp(garums):
    return os.urandom(garums)

# Baitu XOR operācija
def xor_baiti(dati1, dati2):
    return bytes(a ^ b for a, b in zip(dati1, dati2))

# Faila šifrēšana
def sifret_failu(ievades_faila, otp_faila, sifreta_faila):
    print(f"Šifrē {ievades_faila}...")
    dati = lasit_failu(ievades_faila)
    otp = generet_otp(len(dati))
    sifreti_dati = xor_baiti(dati, otp)

    rakstit_failu(otp_faila, otp)
    rakstit_failu(sifreta_faila, sifreti_dati)
    print(f"Šifrēšana pabeigta! OTP saglabāts kā {otp_faila}, šifrētais fails saglabāts kā {sifreta_faila}.")

# Faila dešifrēšana
def desifret_failu(sifreta_faila, otp_faila, desifreta_faila):
    print(f"Dešifrē {sifreta_faila}...")
    sifreti_dati = lasit_failu(sifreta_faila)
    otp = lasit_failu(otp_faila)

    desifreti_dati = xor_baiti(sifreti_dati, otp)
    rakstit_failu(desifreta_faila, desifreti_dati)
    print(f"Dešifrēšana pabeigta! Dešifrētais fails saglabāts kā {desifreta_faila}.")

# Galvenā izpildes daļa
if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Kļūda: Nepieciešami 4 argumenti - darbība, ievades fails, OTP fails, izvades fails.")
        sys.exit(1)

    darbiba = sys.argv[1]
    ievades_faila = sys.argv[2]
    otp_faila = sys.argv[3]
    izvades_faila = sys.argv[4]

    if darbiba.lower() == 'enc':
        sifret_failu(ievades_faila, otp_faila, izvades_faila)
    elif darbiba.lower() == 'dec':
        desifret_failu(ievades_faila, otp_faila, izvades_faila)
    else:
        print("Kļūda: Nederīga darbība. Lūdzu, izmantojiet 'enc' šifrēšanai vai 'dec' dešifrēšanai.")