from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    from application import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    print("Returning app from create_app method")
    return app


#if __name__ == "__main__":
print("creating app object...")
app = create_app("config")
# We run on debug only when launching through Python command line
# for production we are launching this REST API app through gunicorn
# app.run(debug=True)
