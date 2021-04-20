import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import seedbank

project = 'SeedBank'
copyright = '2021 Boise State University'
author = 'Michael D. Ekstrand'

release = seedbank.__version__

extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

source_suffix = '.rst'

pygments_style = 'sphinx'
highlight_language = 'python3'

html_theme = 'furo'
html_theme_options = {
    # 'github_user': 'lenskit',
    # 'github_repo': 'seedbank',
}
templates_path = ['_templates']

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'numba': ('https://numba.readthedocs.io/en/stable/', None),
    'sklearn': ('https://scikit-learn.org/stable/', None),
    'torch': ('https://pytorch.org/docs/stable/', None),
}

autodoc_default_options = {
    'members': True,
    'member-order': 'bysource'
}

napoleon_type_aliases = {
    'seed-like': ':term:`seed-like`'
}
