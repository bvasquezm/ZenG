from bot import ZenG
from settings import TOKEN, PREFIX

if __name__ == "__main__":
    client = ZenG(PREFIX)
    client.run(TOKEN)
