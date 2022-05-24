from sanic import Sanic
from sanic.response import text

from app.apis import api

app = Sanic("CustomedLink")
app.blueprint(api)

@app.get("/")
async def hello_world(request):
    return text("Customed Link")