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
## ローカルでアプリ起動
python -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m uvicorn app.main:app --host 0.0.0.0 --port 8000

## デバッガーの接続
VSCodeのデバッグ構成（Remote Debug for Local Process）を実行する