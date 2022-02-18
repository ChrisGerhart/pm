from flask import Flask, redirect, url_for, render_template, request
from json import load

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def get_user():
    return redirect(url_for("user", username=f"{request.form['username']}"))

@app.route("/user/<username>")
def user(username):
    if username in data:
        return render_template("user_tasks.html", username=username, rows = make_table_rows(data[username]))
    return f"Hello @{username}, we couldn't find your tasks :("

def make_table_rows(tasks):
    all_keys = []
    for task in tasks:
        for key in task.keys():
            all_keys.append(key)
    keys = sorted(set(all_keys), key=all_keys.index)
    rows = [keys]
    for task in tasks:
        new_row = []
        for key in keys:
            new_row.append(task.get(key, ""))
        rows.append(new_row)
    return rows

if __name__ == "__main__":
    with open("tasks.json") as f:
        data = load(f)
    app.run(debug = True)

def passwordRegister():
  password = input("Enter a password")
  passwordConfirm = input("Re-Enter your password")

  if password != passwordConfirm:
    print("Passwords are not the same")
  else:
    if len(password) < 5:
      print("Password is too short")
      UserRegister()
    elif not any(char.isalpha() for char in password):
      print("Password must contain a letter")
      UserRegister()
    elif not any(char.isupper() for char in password):
      print("Password must contain an uppercase")
      UserRegister()
    elif not any(char.islower() for char in password):
      print("Password must contain a lowercase")
      UserRegister()
    elif not any(char.isdigit() for char in password):
      print("Password must contain a number")
      UserRegister()
    elif any(char.isalnum() for char in password):
      print("Password must contain a special character")
      UserRegister()
      '''Not working, password is accpeted with or without special characters'''
    else:
      print("Your account has been created")
UserRegister()
