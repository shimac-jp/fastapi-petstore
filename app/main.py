from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError

# 開発モジュール
from app.routers import pets_router, health_router


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
    'description': 'api状態確認'
}] 

app = FastAPI(title='ペットストア', version='0.1.0', description=description, openapi_tags=tags_metadata)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

app.include_router(pets_router.router, tags=["pets"])
app.include_router(health_router.router, tags=["health"])
