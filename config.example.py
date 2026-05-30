# Configuration File for DXF to NC Bot
# Copy this to config.py and update values

# WhatsApp Settings
WHATSAPP_NUMBER = "+508676482"  # Your WhatsApp number
WHATSAPP_API_KEY = "your_api_key_here"

# End Mill Sizes (mm)
END_MILL_SIZES = [3, 4, 5, 6, 8, 10, 12, 28]

# Materials & Feed Rates
MATERIALS = {
    'wood': {
        'feed_rate': 1200,
        'spindle_speed': 8000,
        'depth_per_pass': 5
    },
    'acrylic': {
        'feed_rate': 1000,
        'spindle_speed': 10000,
        'depth_per_pass': 3
    }
}

# Machine Settings
MAX_RPM = 12000
DEFAULT_SAFETY_MARGIN = 2  # mm

# Raspberry Pi Settings
USB_GADGET_PORT = '/dev/ttyACM0'
STORAGE_PATH = '/home/pi/dxf_files'
LOG_PATH = '/home/pi/logs'

# Web Dashboard
WEB_PORT = 5000
WEB_HOST = '0.0.0.0'

# Database
DATABASE_PATH = '/home/pi/bot_database.db'
