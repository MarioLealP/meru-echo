"""The echo app."""

import sentry_sdk
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

# Crash reports to GlitchTip (D125): SENTRY_DSN comes from nuwa-app's glitchtip.dsn; unset, the SDK stays off.
# No local variables or request bodies in a report - either can hold a secret.
sentry_sdk.init(include_local_variables=False, max_request_body_size="never")


app = FastAPI(title="echo", docs_url=None, redoc_url=None, openapi_url=None)


@app.get("/heartbeat", response_class=PlainTextResponse)
async def heartbeat() -> str:
    """Meru's liveness and readiness probes (nuwa-app's heartbeat.path) - add a /ready once there are dependencies."""
    return "ok"
