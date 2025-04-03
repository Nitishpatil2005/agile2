from flask import Flask
from model import create_table, insert_user

app = Flask(__name__)

# Create the database table when the app starts
create_table()

@app.route('/')
def home():
    insert_user('John Doe', 'johndoe@example.com', 30)
    insert_user('Doe', 'doe@example.com', 10)
    insert_user('John ', '123johndoe@example.com', 20)
    return 'User inserted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
