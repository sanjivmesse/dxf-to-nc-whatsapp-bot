#!/usr/bin/env python3
"""
DXF to NC WhatsApp Bot - Main Entry Point
Optimized for Raspberry Pi Zero 2W
"""

import os
import sys
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import modules
try:
    from bot.whatsapp_bot import WhatsAppBot
    from bot.dxf_processor import DXFProcessor
    from bot.gcode_generator import GCodeGenerator
    from config import WHATSAPP_NUMBER, STORAGE_PATH
except ImportError as e:
    logger.error(f"Import error: {e}")
    logger.error("Please run: pip3 install -r requirements.txt")
    sys.exit(1)

def main():
    """
    Main function to start the bot
    """
    logger.info("="*50)
    logger.info("DXF to NC WhatsApp Bot Starting...")
    logger.info("="*50)
    
    # Create necessary directories
    Path(STORAGE_PATH).mkdir(parents=True, exist_ok=True)
    Path(STORAGE_PATH + '/dxf').mkdir(parents=True, exist_ok=True)
    Path(STORAGE_PATH + '/nc').mkdir(parents=True, exist_ok=True)
    
    logger.info(f"Storage path: {STORAGE_PATH}")
    logger.info(f"WhatsApp number: {WHATSAPP_NUMBER}")
    
    # Initialize bot components
    try:
        bot = WhatsAppBot()
        dxf_processor = DXFProcessor()
        gcode_gen = GCodeGenerator()
        
        logger.info("All components initialized successfully")
        
        # Start bot
        logger.info("Starting WhatsApp bot listener...")
        bot.start()
        
    except Exception as e:
        logger.error(f"Error starting bot: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
        sys.exit(0)
