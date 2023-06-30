# https://stackoverflow.com/questions/49157098/using-custom-preprocessor-with-jupyter-nbconvert-v5-3-1-on-the-command-line
# https://nbconvert.readthedocs.io/en/latest/nbconvert_library.html#Custom-Preprocessors


from nbconvert.preprocessors import Preprocessor
from traitlets import Set, Unicode


class IncludeCellsWithTags(Preprocessor):
    """
    Removes inputs, outputs, or cells from a notebook that
    unless they have designated tabs prior to exporting
    the notebook.

    inlcude_cell_tags
        includes cells tagged with these values
    """
    include_cell_tags = Set(
        Unicode(),
        default_value=[],
        help=(
            "Tags indicating which cells are to be maintained,"
            "matches tags in ``cell.metadata.tags``."
        ),
    ).tag(config=True)

    
    def _items_in_both_lists(self,a,b):
        """Returns true if there are item(s) common to both list like objects
        a and b"""
        return(len(set(a) & set(b)) > 0)

    
    def preprocess(self, notebook, resources):
        """
        Preprocessing to apply to each notebook. See base.py of nbconvert
        for details.
        """        
        executable_cells = []
        for cell in notebook.cells:
            if self._items_in_both_lists(
                cell.metadata.get('tags'), self.include_cell_tags):
                executable_cells.append(cell)
        notebook.cells = executable_cells
        return notebook, resources