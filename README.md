# Twitter-bot for speedtest CNT ISP

Скрипт запускает из себя `speedtest` c параметром  `--simple` и
 если скорость ниже чем положено шлет пост в твиттер.

Скрипт запускается по крону раз в 20 минут.

Рядом со скриптом необходимо создать файл `.env` следующего вида:

```dotenv
TOKEN = "xxxxxxxxxxxxxxxx"
TOKEN_KEY = "xxxxxxxxxxxxxxxx"
CON_SEC = "xxxxxxxxxxxxxxxx"
CON_SEC_KEY = "xxxxxxxxxxxxxxxx"
MY_ISP_TW = "isp_twitter_account"
```

