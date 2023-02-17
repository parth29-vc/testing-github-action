import os
from app import create_app
from dotenv import load_dotenv

# It will load the environment variables from the file
load_dotenv()

env = os.getenv("FLASK_ENV") or "test"
print(f"Active environment: * {env} *")
app = create_app(env)

# if __name__ == '__main__':
app.run(host=os.getenv("SERVER_HOST"), port=int(os.getenv("SERVER_PORT")), debug=True)

