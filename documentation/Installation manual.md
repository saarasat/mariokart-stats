# Installation manual

### Installing the app and working locally

1. Download the application at: https://github.com/saarasat/mariokart-stats

2. Go to the root-folder of the application (where are the files "run.py" and "README.md" and create the Python virtual environment with the command:

<pre><code>python3 -m venv venv</code></pre>

3. Acitvate the Python environment with the command:

<pre><code>source venv/bin/activate</code></pre>

4. Install the necessary dependencies with the command:

<pre><code>pip install -r requirements.txt</code></pre>

5. Launch the application with: 

<pre><code>python run.py</code><pre>

### Installing the app with Heroku 

1. Follow the steps 1-4 first

2. Make sure you have created an account at Heroku

3. On the commandline, create an app at heroku:

<pre><code>heroku create <name of your choosing></code></pre>

(4. in case you wish to modify the app and are using Github, you can add the remote for the app with:)

<pre><code>git remote add heroku https://git.heroku.com/<name-of-your-app>.git</code></pre>

