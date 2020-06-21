# gitkeeper

gitkeeper is a tiny microservice that let's a client side appplication authenticate with GitHub.

### Installation

```bash
# Install dependencies
pip3 install -r requirements.txt

# Export env variables
export OAUTH_CLIENT_ID=<client_id>
export OAUTH_CLIENT_SECRET=<client_secret>

# Run the app
flask run
```

### API

```bash
GET http://localhost:5000/authenticate/<code>
```

Sample success response
```json
{
  "access_token": "2e6c49c405c4e059e3ec6d7e57447a6258a53241", 
  "scope": "repo", 
  "token_type": "bearer"
}
```

Sample error response
```json
{
  "error": "bad_verification_code", 
  "error_description": "The code passed is incorrect or expired.", 
  "error_uri": "https://developer.github.com/apps/managing-oauth-apps/troubleshooting-oauth-app-access-token-request-errors/#bad-verification-code"
}
```

### Deploy to Glitch

- Clone repository
```bash
Glitch > New Project > Clone from Git Repo
```
- Set enviornment variables

```bash
OAUTH_CLIENT_SECRET=""
OAUTH_CLIENT_ID=""
```

Or Just clone the [project](https://glitch.com/~solitudenote-gitkeeper).
> Make sure that the Glitch project is private

Feel free to add deployment steps to other platforms.

[Repository](https://github.com/solitudenote/gitkeeper)

```python
import os
import oyaml as yaml

import markdown
import markdown.extensions.fenced_code
from flaskext.markdown import Markdown
from flask import Flask, render_template
from pygments.formatters import HtmlFormatter

app = Flask(__name__)
Markdown(app)

app.config['JSON_SORT_KEYS'] = False

PROJECTS_DIR_HTML = os.path.join(os.path.abspath('.'), '/sessoes/projetos/html')
PROJECTS_DIR_MARKDOWN = os.path.join(os.path.abspath('.'), 'templates/sessoes/projetos/markdown')

@app.route('/')
def index():
    website_data = yaml.load(open('_config.yaml'))
    return render_template('index.html', data=website_data)


def render_markdown(filepath):
    readme_file = open(filepath, "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code", "codehilite"]
    )
    
    # Generate Css for syntax highlighting
    formatter = HtmlFormatter(style="emacs",full=True,cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = "<style>" + css_string + "</style>"
    
    md_template = md_css_string + md_template_string
    
    return md_template

@app.route("/app-streamlit")
def app_streamlit():
    website_data = yaml.load(open('_config.yaml'))
    
    path = os.path.join(PROJECTS_DIR_MARKDOWN, 'app_streamlit.md')
    
    md_template = render_markdown(path)
    html_template = os.path.join(PROJECTS_DIR_HTML, 'app_streamlit.html')
    
    return render_template(html_template, text=md_template, data=website_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```