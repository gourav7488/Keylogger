from cryptography.fernet import Fernet

key = "PaYV2YqxlQ_0Evhu1qJuJofJe4P2C0UfESme9OEvifc="

system_information_e = 'e_systeminfo.txt'
clipboard_information_e = 'e_clipboard.txt'
keys_information_e = 'e_key_log.txt'



encrypted_files = [keys_information_e, clipboard_information_e, system_information_e]
count = 0


for decrypting_files in encrypted_files:

    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open("decryption.txt", 'wb') as f:
        f.write(decrypted)

    count += 1