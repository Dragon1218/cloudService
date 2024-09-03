# my_pkg/app.py

from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = 'e8f7762f7a7e3f8f8df867d8b2b4d0c3'  # Replace with a strong secret key

# Step 1: Cloud Service Selection
@app.route('/hello')
def hello_world():
    return "Hello, World!"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['cloud_service'] = request.form['cloud_service']
        return redirect(url_for('select_integration'))
    return render_template('serviceSelection.html')

# Step 2: Integration Type Selection
@app.route('/select_integration', methods=['GET', 'POST'])
def select_integration():
    if request.method == 'POST':
        session['integration_type'] = request.form['integration_type']
        return redirect(url_for('select_middleware'))
    return render_template('integrationType.html')

# Step 3: Middleware Selection
@app.route('/select_middleware', methods=['GET', 'POST'])
def select_middleware():
    if request.method == 'POST':
        session['middleware'] = request.form['middleware']
        return redirect(url_for('summary'))
    return render_template('middlewareType.html')

# Final Summary and Integration
@app.route('/summary', methods=['GET', 'POST'])
def summary():
    if request.method == 'POST':
        integration_type = session.get('integration_type')
        if integration_type == 'github':
            return redirect(url_for('github_integration'))
        elif integration_type == 'gitlab':
            return redirect(url_for('gitlab_integration'))
    return render_template('summary.html', session=session)

# GitHub Integration (Example)
@app.route('/github_integration')
def github_integration():
    # Example of redirecting to GitHub OAuth for authentication
    github_client_id = 'Dragon1218'
    redirect_uri = url_for('github_callback', _external=True)
    return redirect(f'https://github.com/login/oauth/authorize?client_id={github_client_id}&redirect_uri={redirect_uri}')

@app.route('/github_callback')
def github_callback():
    code = request.args.get('code')
    github_client_id = 'Dragon1218'
    github_client_secret = 'your_github_client_secret'
    
    token_url = 'https://github.com/login/oauth/access_token'
    headers = {'Accept': 'application/json'}
    payload = {
        'client_id': github_client_id,
        'client_secret': github_client_secret,
        'code': code,
    }
    
    response = requests.post(token_url, headers=headers, data=payload)
    response_data = response.json()
    access_token = response_data.get('access_token')
    
    if access_token:
        # You can now use the access token to interact with the GitHub API
        return f"Successfully authenticated with GitHub! Access Token: {access_token}"
    else:
        return "Failed to authenticate with GitHub."

# GitLab Integration (Example)
@app.route('/gitlab_integration')
def gitlab_integration():
    # Similar logic for GitLab OAuth can be implemented here
    return "GitLab integration is under construction."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
