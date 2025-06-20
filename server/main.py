from fastapi import FastAPI

from server.endpoints import router

app = FastAPI(title="MCP Server for Hercules")

app.include_router(router)