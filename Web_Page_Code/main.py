from flask import Flask, render_template, request, redirect, url_for, session, send_file
from otp import load_user_data, validate_user, validate_otp
import os

app = Flask(__name__)
app.secret_key = '1234' 

    
@app.route('/')
@app.route("/DeathStarWeaknesses")
def death_star_weaknesses_render():\
    # Retrieve image filenames from the static/img directory
    image_dir = os.path.join(app.static_folder, 'img/death_star_images')
    images = [f'img/death_star_images/{filename}' for filename in os.listdir(image_dir) if filename.endswith(('.jpg', '.png', '.jpeg'))]

    return render_template('death_star_weaknesses.html', images=images) 

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_file(os.path.join('static', filename), as_attachment=True)

@app.route('/login')
def login():
    return render_template('login.html')

# Route to handle form submission
@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    file_path = "data/users.xlsx"
    df = load_user_data(file_path)

    if df is None:
        print("Failed to load user data.")
        return
    
    isObiwan, secret_key = validate_user(username, password, df)

    if(isObiwan):
        session['username'] = username
        session['secret_key'] = secret_key
        return redirect(url_for('otp'))  # Redirect to OTP page

    else:
        print("Not obiwan")
        return('Invalid username or password. Please try again.')

# Route to display OTP input form
@app.route('/otp', methods=['GET'])
def otp():
    # Ensure user is coming from a valid login
    print(session)
    if 'username' not in session:
        print("Not in sesh")
        return redirect(url_for('login'))  # Redirect to login if no valid session

    return render_template('otp.html')


# Route to handle OTP submission
@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    user_otp = request.form['otp']

    if validate_otp(session['secret_key'], user_otp):
        print("Login successful!")
        # return f'Login successful! Welcome, {session["username"]}!'
        return(render_template('obiwan.html'))
    
    else:
        print("Invalid OTP. Login failed.")
        return(render_template('galaxy.html'))

@app.route("/GalaxyVideo")
def galaxy_render():
    return render_template('galaxy.html') 

if __name__ == '__main__':
    app.run(debug=True)