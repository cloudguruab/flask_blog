from app import *
from posts_bp.blueprint import *

app.register_blueprint(posts, url_prefix='/blog')    

if __name__ == "__main__":
    app.run(port=5000)