import uvicorn

from .app import create_production_app

if __name__ == '__main__':
    uvicorn.run(create_production_app, host='0.0.0.0', port=8000, factory=True)
