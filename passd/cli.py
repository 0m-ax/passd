import pypass
import dmenu
import pyperclip
p = pypass.PasswordStore()
def run(args=None):

    path = dmenu.show(["Add Password"]+p.get_passwords_list())
    if path == "Add Password":
        dmenu.show(["are you kidding me like i would add that"])
        exit()

    password = p.get_decrypted_password(path,entry=pypass.EntryType.password)
    username = p.get_decrypted_password(path,entry=pypass.EntryType.username)
    hostname = p.get_decrypted_password(path,entry=pypass.EntryType.hostname)
    raw = p.get_decrypted_password(path)

    items = []
    if password:
        items.append("Password")
    if username:
        items.append("Username:"+username)
    if hostname:
        items.append( "Hostname:"+hostname)
    entry = dmenu.show(items)

    value = raw
    if entry.startswith("Password"):
        value = password
    if entry.startswith("Username"):
        value = username
    if entry.startswith("Hostname"):
        value = hostname
    pyperclip.copy(value)
