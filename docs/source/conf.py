import sphinx_rtd_theme
import sphinx_rtd_dark_mode

project = "vmpheus Docs"
author = "Arun George Saji"

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_rtd_dark_mode',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]
html_static_path = ["_static"]

html_show_sourcelink = False

html_logo = "_static/vortexlinux-favicon.png" 
html_favicon = "_static/vortexlinux-favicon.png" 

html_theme = "sphinx_rtd_theme"
default_dark_mode = True

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'black',
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

html_context = {
}

html_css_files = [
    'css/custom.css',
]
