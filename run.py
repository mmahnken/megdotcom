from app import app
import os

port = int(os.environ.get('PORT', 5000))
app.run(port=port)
