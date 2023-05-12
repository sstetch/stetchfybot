##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
get_queue = {}
SESSION_NAME = getenv('SESSION_NAME', 'BABeoPb8_V9H6tvmz3bdDuWQJ_eHVWjOL1Fnpiaioua8xW4kVgt4GW3f4IP8wLtPgyrZMXhHZRpCg8dKb8daR5U2o9iKX_olDr4Jj9K29LhUdr7WXu-WyNEQAv95TQj_V89NULLqcgzOe43TE-65-MuQrWV4VZD_9u7n_G_rNjwFjE1RSQeQhkssAYc3hTIoF5tkwehRPzPfnXpu1DxkMjtrzVQ7nbhzOgKzkCSO9GXLRSLDA2l1gURoU1TPjV2qyAkiFdLWOO-xcb7Tp--Ae_S6a8-oURC1VgfeJ6EathAUYS_SjZqdcty3laSAyOM7jTP0lf42ekvcTDaJAYF6Y42mAAAAAW3f2RcA')
BOT_TOKEN = getenv('BOT_TOKEN', '6208176104:AAFfhRHFpIvb0h_Jc8Mum-yz-ZH0RgMFPJU')
API_ID = int(getenv('API_ID', '14837825'))
API_HASH = getenv('API_HASH', '0ed849f5e7ab2df61d969317de2ca64c'))
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '540000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ ! _ ').split())
MONGO_DB_URI = getenv("MONGO_DB_URI", 'mongodb+srv://joepsychoo:<password>@cluster0.q0ox4m3.mongodb.net/?retryWrites=true&w=majority')
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '1404114574').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001596581219'))
ASS_ID = int(getenv("ASS_ID", '6138353943'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '1404114574').split()))
GROUP = getenv("GROUP", 'TXNX5')
CHANNEL = getenv("CHANNEL", 'its_stetch')
CHANNEL = getenv("CHANNEL", 'TXNX3')
MUST_JOIN = getenv("MUST_JOIN", 'TXNX5')
if MUST_JOIN.startswith("@"):
    MUST_JOIN = MUST_JOIN.replace("@", "")
