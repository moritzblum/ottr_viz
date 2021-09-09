# OTTR Viz: Reasonable Ontology Template Visulaization

## Installation
Requires Python >= 3.6

1. clone
2. navigate into the main directory by `cd ottr_viz/`
3. install all python requirements with `pip install .`
4. install the additional requirements depending on the tools you use


## Viz OTTR Library

    python ottr_library.stottr

### Additional dependencies
* [Graphviz](https://graphviz.org/), install with `sudo apt-get install graphviz graphviz-dev` if not already installed

### Parameters
    -format, --format:  output file format, e.g. png, pdf (all types supported by graphviz), default='png'

### Example:
With `python viz_ottr_library.py -format png data/pattern_library.stottr` you can generate the following visualization:

![Viz OTTR Library example](./data/pattern_library_viz.png)


## Viz OTTR Instances

    python ottr_instances.stottr ottr_library.stottr

### Additional dependencies
* [Lutra](https://gitlab.com/ottr/lutra/lutra)
* [Raptor RDF Syntax Library](https://librdf.org/raptor/)

### Parameters
    -format, --format:      output file format, e.g. png, pdf, default='png'
    -rdf_dir, --rdf_dir:    if specified: directory for storing the RDF instances
    -viz_dir, --viz_dir:    if specified: directory for outputting the visualizations

### Example:
With `python viz_ottr_instances.py ./data/ottr_instances/ ./data/pattern_library.stottr` you can generate the following visualization:

![Viz OTTR Instances example](./data/ottr_instances/pattern_instance.png)


