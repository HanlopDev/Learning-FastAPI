from turtle import st
from unittest import result
from fastapi import Request, APIRouter, FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/accordion", response_class=HTMLResponse)
async def get_accordion(request: Request):
    tag = "flower"
    result = "Type a Number"
    return templates.TemplateResponse("accordion.html", context={'request': request, 'result':result, 'tag':tag})

@router.post("/accordion", response_class=HTMLResponse)
def post_accordion(request: Request, tag: str = Form(...)):
    return templates.TemplateResponse('accordion.html', context={'request':request, 'tag':tag})
