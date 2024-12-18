from flask import Flask, make_response
import invoice_api
import file_api
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config.from_object("setting.DevelopmentConfig")
    # 将对应模块下的蓝图对象注册到app中
    with app.app_context():
        app.register_blueprint(invoice_api.new_list)
        app.register_blueprint(file_api.new_list)

    return app

if __name__ == '__main__':
    app_s = create_app()
    app_s.run()