from app import create_app

# Load the appropriate configuration based on the environment
app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])
