from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError
from pathlib import Path
from dotenv import load_dotenv

# 開発モジュール
from app.routers import pets_router, health_router

# 環境変数のロード
env_path = Path('./app/configs') / '.env.default'
load_dotenv(dotenv_path=env_path, override=False, encoding='utf-8')

description = """
## ベースURL、ポート番号
* ・・・

## 認証
* ・・・

## エラーレスポンス
* ・・・

## 特記事項
* ・・・

"""

tags_metadata = [{
    'name': 'pets',
    'description': 'ペット'
},{
    'name': 'health',
    'description': 'ヘルスチェック'
}] 

app = FastAPI(title='ペットストア', version='0.2.0', description=description, openapi_tags=tags_metadata)
# DevSpacesではプロキシされる関係で、fqdnの後にパスが設定される。docsアクセス時に設定されたパスをつけてopenapi.jsonをとれるように、FastAPIアプリにopenapi_prefixをセットする必要がある
# app = FastAPI(title='ペットストア', version='0.2.0', description=description, openapi_tags=tags_metadata, openapi_prefix="/workspacef5f6ac0990884648/theia-ide/13133")



@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

app.include_router(pets_router.router, tags=["pets"])
app.include_router(health_router.router, tags=["health"])
