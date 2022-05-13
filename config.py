from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "12787577"))
API_HASH = getenv("API_HASH", "d30cef43991a144be80615919bfcfc6c")
BOT_TOKEN = getenv("BOT_TOKEN","5384359690:AAF9eXm2jZbSqHLq8ZVIs8g1rGXso-pM980")
BOT_NAME = getenv("BOT_NAME","AGORA ROBOT")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "AQCO7KQ-oyGgMD8FRaGUUbHz43j3-SMfiIF6gmct-xb9HZyAmNJuGEMSwjJOCZr-hfqIFGYSJ8dhZEfo8DcEQHydPFNNPTr72CUYVk31ymHwNewUX90DYjVUlF06IdxPPTfNJHqlBDtFF03DSKW0OhPq4PtknZ0WmxwXhDB8yC42yiefcKFdxWVfz6ap7uNVkSMuLykw4snTkQtc5OIrFru6bx9kLbD8VGU32JiSZobd0C-zPNKVE0U4o6LjvdvYaYlpNu1L9z3ZbjcsEDvxKptpQSUaRa0RetqqAzVaXI3GXaFpYwPhdQUZXIcnhPoATht8ByeR2bqHMALPNBkOoJfvAAAAATe3gk0A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5272015055 5122474448").split()))
