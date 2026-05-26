import datetime
from zoneinfo import ZoneInfo

fuso_BR = ZoneInfo("America/Sao_Paulo")
x = datetime.datetime.now(fuso_BR)
print(x)
