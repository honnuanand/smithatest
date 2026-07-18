from datetime import datetime

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Hello Smitha")


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    now = datetime.now()
    date_str = now.strftime("%A, %B %d, %Y")
    time_str = now.strftime("%I:%M:%S %p")
    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello Smitha</title>
    <style>
        :root {{ color-scheme: light dark; }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #fff;
            text-align: center;
            padding: 1.5rem;
        }}
        .card {{
            background: rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.25);
            border-radius: 20px;
            padding: 3rem 3.5rem;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.25);
        }}
        h1 {{ font-size: clamp(2.5rem, 6vw, 4rem); font-weight: 700; margin-bottom: 1.25rem; }}
        .date {{ font-size: clamp(1.1rem, 3vw, 1.5rem); font-weight: 500; opacity: 0.95; }}
        .time {{ font-size: clamp(1.5rem, 4vw, 2.25rem); font-weight: 600; margin-top: 0.4rem; letter-spacing: 0.03em; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>Hello Smitha 👋</h1>
        <div class="date">{date_str}</div>
        <div class="time" id="time">{time_str}</div>
    </div>
    <script>
        // Keep the clock ticking live in the browser.
        function tick() {{
            const now = new Date();
            document.getElementById("time").textContent =
                now.toLocaleTimeString("en-US", {{ hour12: true }});
        }}
        setInterval(tick, 1000);
    </script>
</body>
</html>"""
