# fastapi-petstore

# インターフェース仕様
http://localhost:8000/docs

# 起動・停止
## ローカルで使う場合
### 起動
uvicorn app.main:app

### アクセス確認
curl http://localhost:8000/pets

* レスポンス
[{"pet_id":"1","name":"tama","type":"cat"},{"pet_id":"2","name":"kuro","type":"cat"}]

## Dockerで使う場合
### ビルド
docker build -t fastapi-petstore .

### コンテナ作成
docker run -d -p 8000:8000 --name fastapi-petstore fastapi-petstore

### コンテナ起動
docker start fastapi-petstore

### コンテナ停止
docker stop fastapi-petstore

### アクセス確認
curl http://localhost:8000/pets

* レスポンス
[{"pet_id":"1","name":"tama","type":"cat"},{"pet_id":"2","name":"kuro","type":"cat"}]

# リモートデバッグ
## ローカル
* アプリ起動

    python -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m uvicorn app.main:app --host 0.0.0.0 --port 8000

* デバッガーの接続

    VSCodeのデバッグ構成（Remote Debug for Local）を実行する


## CodeReady
* アプリ起動

    タスクの1. pip3 install、2. run application with debugpyを実行する


* デバッガーの接続

    VSCodeのデバッグ構成（Remote Debug for CodeReady）を実行する

* コード修正後のアプリ再起動

    タスクを停止すると、アプリは停止されるが、debugpyが起動したままでポートを掴んでいる
    そのため、pythonコンテナに入って、debugpyのプロセスをkillする
    ```
    [jboss@workspacesri9s5e4q37x99tv fastapi-petstore]$ ps -ef|grep debugpy
    jboss        46      1  0 12:42 ?        00:00:00 /usr/bin/python /home/jboss/.local/lib/python3.8/site-packages/debugpy/adapter --for-server 35394 --host 0.0.0.0 --port 5678 --server-access-token 41652595eb6e5b6790cae584a943fe17e8d7f644acf42984022089481b017ee0
    jboss       107     87  0 12:45 pts/1    00:00:00 grep --color=auto debugpy
    
    [jboss@workspacesri9s5e4q37x99tv fastapi-petstore]$ kill -9 46
    ```

# テスト
* プロジェクトルートから下記のように実行する
```
# pytest app
====================== test session starts ======================
platform darwin -- Python 3.8.13, pytest-7.1.2, pluggy-1.0.0
rootdir: /Users/shimac/data/2.task/2021_ITLMC_appdev/contest-phase2/projects/fastapi-petstore
plugins: anyio-3.6.1
collected 1 item                                                                                                                                                                                                            

app/tests/test_pets.py .                                                                                                                                                                                              [100%]

====================== 1 passed in 0.01s ======================
