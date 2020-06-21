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

is_arrow_left = None

@app.route('/')
def index():
    website_data = yaml.load(open('_config.yaml'))

    return render_template('index.html', is_arrow_left=False, data=website_data)


def render_markdown(filepath):
    readme_file = open(filepath, "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code", "codehilite"]
    )
    
    # Generate Css for syntax highlighting
    formatter = HtmlFormatter(style="emacs", full=True, cssclass="codehilite")
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
    
    return render_template(html_template, text=md_template, is_arrow_left=True, data=website_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
