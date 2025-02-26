from pathlib import Path
import textwrap
import plasTeX
from plasTeX.TeX import TeX


def test_input_absolute_path(tmpdir):
  with tmpdir.as_cwd():
    Path('input.tex').write_text(textwrap.dedent(r"""
        \documentclass{article}
        \usepackage{amsthm}
        \usepackage{depgraph}

        \newtheorem{theorem}[theorem]{Theorem}

        \begin{document}
          \begin{theorem}\label{foo}
            Foo
          \end{theorem}
          \begin{theorem}\label{bar}\uses{foo}
            Bar
          \end{theorem}
          \begin{proof}\proves{bar}
            Proof of bar using foo
          \end{proof}
        \end{document}
        """))

    tex = TeX(file='input.tex')
    tex.ownerDocument.config['general'].data['plugins'].value = [
        'plastexdepgraph'
    ]
    tex.ownerDocument.userdata['jobname'] = 'test'
    doc = tex.parse()
    graph = doc.userdata['dep_graph']['graphs'][doc]
    assert len(graph.nodes) == 2
    assert len(graph.edges) == 1
