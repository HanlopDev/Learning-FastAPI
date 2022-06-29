from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/twoforms", response_class=HTMLResponse)
async def twoform_home(request: Request):
    return templates.TemplateResponse("twoforms.html", {'request': request})

