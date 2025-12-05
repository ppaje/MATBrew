"""
Веб-сервер дашборда аналитики
"""

from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import json
from pathlib import Path
from datetime import datetime

app = FastAPI(title="Telegram Insights Dashboard")

# Настройка статических файлов и шаблонов
BASE_DIR = Path(__file__).resolve().parent.parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Глобальные данные (в реальной системе будет БД)
user_stats = {}

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Главная страница дашборда"""
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "title": "Telegram Insights Pro"}
    )

@app.get("/api/stats/{user_id}")
async def get_user_stats(user_id: int):
    """Получение статистики пользователя"""
    # В реальной системе загрузка из БД
    report_path = Path(f"data/analytics_reports/{user_id}_{datetime.now().date()}.json")
    
    if report_path.exists():
        with open(report_path, 'r', encoding='utf-8') as f:
            report = json.load(f)
        return report
    else:
        return {"error": "Report not found", "user_id": user_id}

@app.get("/api/reports")
async def get_all_reports():
    """Получение списка всех отчетов"""
    reports_dir = Path("data/analytics_reports")
    
    if not reports_dir.exists():
        return []
    
    reports = []
    for report_file in reports_dir.glob("*.json"):
        with open(report_file, 'r', encoding='utf-8') as f:
            report_data = json.load(f)
            reports.append({
                "user_id": report_data.get("user_id"),
                "date": report_data.get("generated_at"),
                "stats": report_data.get("statistics", {})
            })
    
    return reports

@app.websocket("/ws/updates")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket для обновлений в реальном времени"""
    await websocket.accept()
    
    try:
        while True:
            # Отправляем обновления статистики
            # В реальной системе здесь будут реальные данные
            import asyncio
            await asyncio.sleep(10)
            
            update_data = {
                "timestamp": datetime.now().isoformat(),
                "active_users": len(user_stats),
                "messages_processed": sum(stats.get("total_messages", 0) for stats in user_stats.values())
            }
            
            await websocket.send_json(update_data)
    except:
        pass

def run_dashboard_server():
    """Запуск сервера дашборда"""
    config = uvicorn.Config(
        app,
        host="0.0.0.0",
        port=8081,
        log_level="info"
    )
    server = uvicorn.Server(config)
    
    import asyncio
    asyncio.run(server.serve())

if __name__ == "__main__":
    run_dashboard_server()
