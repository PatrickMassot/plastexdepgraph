# plasTeX dependency graphs

This is a [plasTeX](https://github.com/plastex/plastex/) plugin allowing
to build dependency graphs.

Needs graphviz and its dev libraries. If you have a user-friendly OS, it is
as simple as `sudo apt install graphviz libgraphviz-dev`. See https://pygraphviz.github.io/documentation/stable/install.html otherwise.

You can use this package with plasTeX using `\usepackage{depgraph}`.
Do not forget to tell plasTeX to use this plugin. From the command line, this
would mean running `plastex --plugins=plastexdepgraph test.tex` for instance.
Note that the
[Lean blueprint package](https://github.com/PatrickMassot/leanblueprint)
automatically loads this packages and transmit options.

## Options

When loading the package inside the tex file, you can give the following
arguments:
* title: the title of the dependency graph.
        The default value is Dependencies.
* dep_by: optional level for dependency graph generation, for instance chapter
        or part.
        The default value is to generate one graph for the whole document
* thms: optional list of theorem types to include into the report,
        separated by +.
        The default value is: definition+lemma+proposition+theorem+corollary
* nonreducedgraph: keep all edges in the dependency, even transitively
        redundant ones.
* tpl: template file for dependency graph, relative to the current
  directory

For instance you could write 
```latex
\usepackage[thms=dfn+lem+prop+thm+cor]{depgraph}
```
if you like short environment names.

This package will also consider optional information contained in the document
userdata dictionary. Such information could be added by other packages who
want to influence the dependency graph. For instance the 
[Lean blueprint plugin](https://github.com/PatrickMassot/leanblueprint)
does that.

* `document.userdata['dep_graph']['shapes']` can be a dictionary whose keys are node
  kinds as strings and whose values are strings descripting graphviz shapes
  (see https://graphviz.org/doc/info/shapes.html).
  By default, everything uses an ellipse except definition which uses a box.

* `document.userdata['dep_graph']['colorizer']` can be a function taking as input
  a plasTeX node and outputting a CSS color for the boundary of graph nodes.

* `document.userdata['dep_graph']['fillcolorizer']` can be a function taking as
  input a plasTeX node and outputting a CSS color for the interior of graph
  nodes.

* `document.userdata['dep_graph']['stylerizer']` can be a function taking as input
  a plasTeX node and outputting a graphviz style
  (see https://graphviz.org/docs/attr-types/style/).

* `document.userdata['dep_graph']['legend']` can be a list whose entries are pairs
  made of a visual description and an explanation.
  The default value is:
  [('Boxes', 'definitions'), ('Ellipses', 'theorems and lemmas')]
  Additional entries can also refer to colors.

* `document.userdata['dep_graph']['extra_modal_links']` can be a list of Jinja2
  templates used to render extra links at the bottom of the modal appearing
  when clicking on graph nodes.
  The default value is an empty list.

## Minimal example

The procedure to create a minimal example of using this plugin is:

* Install the required graphviz packages (say using  `sudo apt install graphviz libgraphviz-dev`)
* Install this python package (say using `pip install plastexdepgraph` which
will also install the main platex program).
* Create a TeX file `test.tex` with content

  ```latex
  \documentclass{article}
  \usepackage{depgraph}

  \newtheorem{definition}{Definition}

  \begin{document}
  \section{Test}
    
  \begin{definition}
    \label{def:one} My first definition.
  \end{definition}

  \begin{definition}
    \uses{def:one}
    \label{def:two} My second definition.
  \end{definition}
  \end{document}
  ```
* Run `plastex --plugins=plastexdepgraph test.tex`
* Serve the content of the newly created `test` folder, say with `python -m
http.server` ran from that folder (simply opening the html files as local files without going through a web server won’t work).

Note the `\section` is here to ensure there will be some table of contents. Otherwise the dependency graph will be generated but you won’t see any link.