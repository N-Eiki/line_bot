# line_bot
今の所は投稿をそのまま返す
#
後々にキャラクターの画像を送ったらそのキャラ名を返すみたいなのにしたい
#
https://developers.line.biz/console/channel/1654298344/messaging-api

#
$ python manage.py runserver
$ ngrok http 8000

#
ngrok http 8000の結果出力されたurlで https://developers.line.biz/console/channel/1654298344/messaging-api のwebhookの部分を更新する。
#
settings.pyのALLOWED_HOSTSを〇〇.ngrok.ioにする。
