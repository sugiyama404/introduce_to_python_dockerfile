from flask import Flask
from flask_cors import CORS
import sys
sys.path.append("/app")
from opt.interface.router.index_controller import index_bp
from opt.interface.router.user_controller import user_bp
import opt.settings as settings

app = Flask(__name__)
CORS(app)

app.register_blueprint(index_bp, url_prefix='/')
app.register_blueprint(user_bp, url_prefix='/user')

if __name__ == "__main__":
    app.run(debug=settings.debug_mode, host='0.0.0.0', port=8000)
