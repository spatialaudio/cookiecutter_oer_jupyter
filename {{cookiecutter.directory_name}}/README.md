# {{cookiecutter.project_name}}
{%- if cookiecutter.include_ci == "Yes" -%}
[![Linting]({{cookiecutter.git_remote}}/actions/workflows/lint_nb.yml/badge.svg?branch=master)]({{cookiecutter.git_remote}}/actions/workflows/lint_nb.yml) 
[![Run Notebooks]({{cookiecutter.git_remote}}/actions/workflows/run_nb.yml/badge.svg?branch=master)]({{cookiecutter.git_remote}}/actions/workflows/run_nb.yml) 
[![Sphinx Built]({{cookiecutter.git_remote}}/actions/workflows/notebook_ci.yml/badge.svg?branch=master)]({{cookiecutter.git_remote}}/actions/workflows/notebook_ci.yml)
{% endif %}

This repository collects didactically edited [Jupyter](https://jupyter.org/) notebooks that introduce basic concepts of [{{cookiecutter.project_name}}]({{cookiecutter.git_remote}}). Please take a look at the [static version](http://nbviewer.ipython.org/github/{{cookiecutter.git_remote}}/blob/master/index.ipynb)
at first glance. 

_Insert overview of contents_

The contents are provided as [Open Educational Resource](https://de.wikipedia.org/wiki/Open_Educational_Resources), so feel free to fork, share, teach and learn.
You can give the project a [Star]({{cookiecutter.git_remote}}/stargazers) if you like it.


## Getting Started

The Jupyter notebooks are accessible in various ways

* Online as [static web pages](http://nbviewer.ipython.org/github/{{cookiecutter.git_remote}}/blob/master/index.ipynb)
* Online for [interactive usage](https://mybinder.org/v2/gh/{{cookiecutter.git_remote}}/master?filepath=index.ipynb) with [binder](https://mybinder.org/)
* Local for interactive usage on your computer

Other online services (e.g. [Google Colaboratory](https://colab.research.google.com),
[Microsoft Azure](https://azure.microsoft.com/), ...) also provide environments for the 
interactive execution of Jupyter notebooks.
Local execution on your computer requires a local Jupyter/IPython installation.
The [Anaconda distribution](https://www.continuum.io/downloads)  is considered a convenient starting point.
Then, you would have to [clone/download the notebooks from Github]({{cookiecutter.git_remote}}).
Use a [Git](http://git-scm.org/) client to clone the notebooks and start
your local Jupyter server. For manual installation under OS X/Linux please
refer to your packet manager.

## Concept and Contents



The material covers the following topics 

* topic 1
* topic 2
* ...


## Usage and Contributing

The contents are provided as [Open Educational Resource](https://de.wikipedia.org/wiki/Open_Educational_Resources).
**!TBD: license!**
Feel free to use the entire collection, parts, or even single notebooks for your purposes.
I am curious on the usage of the provided resources, so feel free to drop a
line or report to [{{cookiecutter.contact_mail}}](mailto:{{cookiecutter.contact_mail}}).

You are invited to contribute on different levels.
The lowest level is to provide feedback in terms of a
[Star]({{cookiecutter.git_remote}}/stargazers)
if you like the content.
Please consider reporting errors or suggestions for improvements as
[issues]({{cookiecutter.git_remote}}/issues).
We are always looking forward to new examples and exercises, and reformulated existing and novel sub-sections or sections.
Authorship of each considerable contribution is clearly stated.
One way of introducing reformulated and new material is to handle them as
a tracked [pull request]({{cookiecutter.git_remote}}/pulls).

{%- if cookiecutter.include_ci == "Yes" -%}
## Build Status

The notebooks' computational examples are automatically built and checked for errors by continuous integration using github actions.

[![Linting]({{cookiecutter.git_remote}}/actions/workflows/lint_nb.yml/badge.svg?branch=master)]({{cookiecutter.git_remote}}/actions/workflows/lint_nb.yml) 
[![Run Notebooks]({{cookiecutter.git_remote}}/actions/workflows/run_nb.yml/badge.svg?branch=master)]({{cookiecutter.git_remote}}/actions/workflows/run_nb.yml) 
[![Sphinx Built]({{cookiecutter.git_remote}}/actions/workflows/notebook_ci.yml/badge.svg?branch=master)]({{cookiecutter.git_remote}}/actions/workflows/notebook_ci.yml)

{% endif %}

{#
The general structure of this repository including this readme and the continuous integration workflows through GitHub actions were created by a [cookiecutter](https://www.cookiecutter.io) template. The template is heavily based on the a collection of repositories created by [Sascha Spors](http://www.int.uni-rostock.de/Staff-Info.23+B6JmNIYXNoPWUxOTliMTNjY2U2MDcyZjJiZTI0YTc4MmFkYTE5NjQzJnR4X2pwc3RhZmZfcGkxJTVCYmFja0lkJTVEPTMmdHhfanBzdGFmZl9waTElNUJzaG93VWlkJTVEPTExMQ__.0.html) at the University of Rostock, Germany. The contents are provided as [Open Educational Resource](https://de.wikipedia.org/wiki/Open_Educational_Resources)
#}