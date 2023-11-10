import os
import sys

# Priekš vizuālām lietām
from PyQt6.QtCore import Qt
# Priekš ikonas
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout


# Funkcija faila šifrēšanai
def encrypt_file():
    input_filename, _ = QFileDialog.getOpenFileName(caption="🔒 Izvēlēties failu šifrēšanai")
    otp_filename, _ = QFileDialog.getSaveFileName(caption="🔑 Saglabāt OTP failu kā...")
    encrypted_filename, _ = QFileDialog.getSaveFileName(caption="🔒 Saglabāt šifrēto failu kā...")

    # OTP (One-Time Pad) piedzīvojumi
    # Atver ievadfailu binārajā režīmā ('rb') lasīšanai
    with open(input_filename, 'rb') as f_input:
        # Nolasa visu faila saturu un saglabā to mainīgajā 'input_data'
        input_data = f_input.read()

    # Ģenerē OTP, izmantojot os.urandom funkciju.
    # OTP garums ir vienāds ar ievadfaila garumu - len(input_data)
    otp_data = os.urandom(len(input_data))

    # Atver OTP failu binārajā režīmā ('wb') rakstīšanai
    with open(otp_filename, 'wb') as f_otp:
        # Raksta OTP datus failā
        f_otp.write(otp_data)

    # Sapāro ievadfaila datus ar OTP datus
    paired_data = zip(input_data, otp_data)
    # Varēja iet cauri bitiem un tad ņemt pa vienam burtam no viena un otrā, bet ZIP ir īsāk
    # for i in range(len(input_data)):

    # Izveido tukšu sarakstu, kurā glabāt XOR rezultātus
    xor_result_list = []

    # Iterē caur katru baitu pāri
    for a, b in paired_data:
        # Veic XOR operāciju un saglabā rezultātu
        xor_result = a ^ b

        # Pievieno rezultātu sarakstam
        xor_result_list.append(xor_result)

    # Pārveido sarakstu par baitu masīvu
    encrypted_data = bytearray(xor_result_list)

    # Var visu aizvietot ar vienas līnijas rindu
    # encrypted_data = bytearray([a ^ b for a, b in zip(input_data, otp_data)])

    # Atver šifrēto failu binārajā režīmā ('wb') rakstīšanai
    with open(encrypted_filename, 'wb') as f_encrypted:
        # Raksta šifrētos datus failā
        f_encrypted.write(encrypted_data)


# Funkcija faila dešifrēšanai
def decrypt_file():
    encrypted_filename, _ = QFileDialog.getOpenFileName(caption="🔒 Izvēlēties šifrēto failu")
    otp_filename, _ = QFileDialog.getOpenFileName(caption="🔑 Izvēlēties OTP failu")
    decrypted_filename, _ = QFileDialog.getSaveFileName(caption="🔓 Saglabāt dešifrēto failu kā...")

    # Atver šifrēto failu binārajā režīmā ('rb') lasīšanai
    with open(encrypted_filename, 'rb') as f_encrypted:
        # Nolasa visu šifrētā faila saturu
        encrypted_data = f_encrypted.read()

    # Atver OTP failu binārajā režīmā ('rb') lasīšanai
    with open(otp_filename, 'rb') as f_otp:
        # Nolasa visu OTP faila saturu
        otp_data = f_otp.read()

    # Pārbauda, vai šifrētā faila un OTP faila garums ir vienāds
    if len(encrypted_data) != len(otp_data):
        print("OTP faila un šifrētā faila garumam jābūt vienādam.")
        return

    # Atkal izmantojam ZIP - Sapārojam šifrētā faila datus ar OTP datus
    paired_data_decryption = zip(encrypted_data, otp_data)

    # Izveido tukšu sarakstu, kurā glabāt XOR rezultātus
    xor_result_list_decryption = []

    # Iterē caur katru baitu pāri
    for a, b in paired_data_decryption:
        # Veic XOR operāciju un saglabā rezultātu
        xor_result = a ^ b

        # Pievieno rezultātu sarakstam
        xor_result_list_decryption.append(xor_result)

    # Pārveido sarakstu par baitu masīvu
    decrypted_data = bytearray(xor_result_list_decryption)

    # Īsākais pieraksts
    # decrypted_data = bytearray([a ^ b for a, b in zip(encrypted_data, otp_data)])

    # Atver dešifrēto failu binārajā režīmā ('wb') rakstīšanai
    with open(decrypted_filename, 'wb') as f_decrypted:
        # Raksta dešifrētos datus failā
        f_decrypted.write(decrypted_data)


# GUI izveide ar PyQt6
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("🔒 OTP File Encryptor/Decryptor 🔓")
window.setWindowIcon(QIcon('icon.png'))
layout = QVBoxLayout()

# Izveidojam horizontālo layoutu pogām
button_layout = QHBoxLayout()
# Izveidojam horizontālo layoutu aprakstiem
info_button_layout = QHBoxLayout()

encrypt_button = QPushButton("🔒 Šifrēt failu")
encrypt_button.clicked.connect(encrypt_file)
decrypt_button = QPushButton("🔓 Dešifrēt failu")
decrypt_button.clicked.connect(decrypt_file)

# Pievienojam pogas un aprakstus horizontālajiem layoutiem
button_layout.addWidget(encrypt_button)
button_layout.addWidget(decrypt_button)

info_button_layout.addWidget(QLabel('''
<b>Poga "🔒 Šifrēt failu"</b><br>
- Faila izvēle: Izvēlas failu.<br>
- OTP ģenerēšana: Izveido OTP.<br>
- XOR: Veic XOR ar OTP.<br>
- Saglabāšana: Saglabā OTP un šifrēto failu.<br>
<i>Piemērs:</i> 01010101 XOR 11001100 = 10011001
'''))
info_button_layout.addWidget(QLabel('''
<b>Poga "🔓 Dešifrēt failu"</b><br>
- Failu izvēle: Izvēlas šifrēto failu un OTP.<br>
- XOR: Atjauno oriģinālo failu.<br>
- Saglabāšana: Saglabā atšifrēto failu.<br>
<i>Piemērs:</i> 10011001 XOR 11001100 = 01010101
'''))

# Pievienojam horizontālos layoutus vertikālajam layoutam
layout.addLayout(button_layout)
layout.addLayout(info_button_layout)

info_label = QLabel('''
<i><br>
<b>Par XOR (Eksklusīvais OR)</b><br><br>
- <b>Izmanto Baitu Operācijas:</b> XOR (Eksklusīvais OR) darbība, kas parasti ir bitu operācija, šajā gadījumā tiek piemērota baitiem. Tas nozīmē, ka katrs baits no ievaddatu masīva tiek paņemts un XOR'ots ar atbilstošo baitu no OTP (One-Time Pad) masīva.<br>
<br>
<b>Darbības Principi:</b>
  <ul>
    <li>Katrs baits ir 8 bitu virkne. Piemēram, baits A varētu būt reprezentēts kā 01000001 un baits X kā 11001000.</li>
    <li>XOR operācija tiek veikta katram bitam atsevišķi vienā baitā.</li>
    <li>Rezultātā iegūstam jaunu 8 bitu virkni, kas pārstāv jaunu baitu.</li>
  </ul><br>

<b>Kā Tas Notiek:</b>
  <ol>
    <li>Ņemam pirmo baitu no ievaddatu masīva un pirmo baitu no OTP.</li>
    <li>Veicam XOR operāciju starp šiem diviem baitiem.</li>
    <li>Saglabājam rezultātu jaunā masīvā.</li>
    <li>Atkārtojam šo procesu katram baitam.</li>
  </ol><br>

<b>Piemērs:</b>
<ul>
<li>Apskatīsim piemēru ar trīs baitiem. Pieņemsim, ka ievaddatu masīvs ir [A, B, C] un OTP ir [X, Y, Z].</li>
<li>XOR operācija starp A un X varētu būt kaut kas līdzīgs 01000001 XOR 11001000 = 10001001.</li>
<li>Līdzīgi, B XOR Y un C XOR Z iegūs jaunus baitus.</li>
<li>Tātad, rezultāts būs jauns masīvs ar šiem jaunajiem baitiem, piemēram, [A^X, B^Y, C^Z].</li>
 </ul>
''')
info_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
info_label.setWordWrap(True)
layout.addWidget(info_label)

signature_label = QLabel("Applied Cryptography, 2023")
signature_label.setAlignment(Qt.AlignmentFlag.AlignRight)

layout.addWidget(signature_label)

window.setLayout(layout)
window.show()

sys.exit(app.exec())