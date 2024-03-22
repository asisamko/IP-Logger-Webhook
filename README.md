
# Simple IP Address Logger

A simple IP Address Logger for Discord Webhook written in Python. 📡

# 👀 Features
- ✅ Customizable Webhook address and name
- ✅ Shows IP deatails directly in the webhook
- ✅ Completly undetected
- ✅ Simple to use
- ⌚ I`m releasing .EXE builder very soon (I have some problems)


1. After you open the file it will grab your IP Address and send it to a Discord Webhook
2. You can send the Python script to the victim or convert to the .EXE file with `pyinstaller` [(Tutorial below)](/README.md#how-to-convert)
## 📸 Webhook preview

![App Screenshot](https://i.ibb.co/4t2pvHV/image.png)


## Download and Usage

- Create a Discord Webhook on your server and copy the address

- Download the script

```bash
  git clone https://link-to-project
```

- Install dependencies

```bash
  pip install -r requirements.txt
```
- Edit the webhook address and name in the `main.py`


- Run the code (CMD / Terminal)

```bash
  python main.py
```



## 💾 How to convert
- Install `pyinstaller` with pip

```bash
  pip install pyinstaller
```

- Build the executable file

```bash
  pyinstaller --noconfirm --onefile --windowed --name "exe-file-name"  "this-python-script-path"
```
- You should get an **executable file** that you can send to the victim
