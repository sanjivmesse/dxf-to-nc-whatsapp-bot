# Installation Guide for Raspberry Pi Zero 2W

## Prerequisites
- Raspberry Pi Zero 2W with OS installed
- 16GB SD Card
- WiFi connectivity
- Python 3.8+

## Step 1: Update System
```bash
sudo apt-get update
sudo apt-get upgrade -y
```

## Step 2: Install Dependencies
```bash
sudo apt-get install python3-pip git -y
pip3 install --upgrade pip
```

## Step 3: Clone Repository
```bash
cd /home/pi
git clone https://github.com/sanjivmesse/dxf-to-nc-whatsapp-bot.git
cd dxf-to-nc-whatsapp-bot
```

## Step 4: Install Python Dependencies
```bash
pip3 install -r requirements.txt
```

## Step 5: Configure WhatsApp Bot
```bash
cp config.example.py config.py
# Edit config.py with your WhatsApp number and settings
nano config.py
```

## Step 6: Run Bot
```bash
python3 main.py
```

## Step 7: Auto-start Service (Optional)
```bash
sudo cp systemd/bot.service /etc/systemd/system/
sudo systemctl enable bot.service
sudo systemctl start bot.service
```

## Troubleshooting
See `TROUBLESHOOTING.md` for common issues.
