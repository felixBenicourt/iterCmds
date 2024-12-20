# iterCmds

A sandbox repository for development purposes with Iter and other tools.  
Additional documentation and specific examples will be provided in the future.

## Pages

1. [README](./README.md)
2. [load constants example](./1.0.2/examples/load_constants.md)

## Table of Contents

- [Runner](#Runner)
- [Features](#Features)
- [Prerequisites](#Prerequisites)
- [Installation](#Installation)
- [Usage](#Usage)
- [Examples](#Examples)
- [License](#license)


# Runner

`scene_runner` is a command-line tool to load scenes, run specific nodes, and fetch attributes of nodes in the ITER API.

## Features

- Load scenes from a local or specified path.
- Execute nodes by name.
- Retrieve and display attributes of specific nodes.
- Log all operations to a file and the console.

## Prerequisites

- Python 3.x
- ITER package installed and configured.

## Installation

Clone this repository and ensure that the required dependencies and ITER framework are properly set up in your environment.

```bash
# Clone the repository
git clone <repository-url>
cd <repository-folder>
```

## Usage

Run the script using the following commands:

### Load Scene from Local Path
```bash
rez env iterCmds -- sceneRunner --lpa <local_path_to_scene>
```
- **`<local_path_to_scene>`**: The relative path to the scene (without `.json` extension).

### Load Scene from Specified Path
```bash
rez env iterCmds -- sceneRunner --pa <path_to_scene>
```
- **`<path_to_scene>`**: The full path to the scene file.

### Run Specific Nodes
```bash
rez env iterCmds -- sceneRunner --run <node_name>
```
- **`<node_name>`**: The name of the node to be executed.

### Fetch Node Attributes
```bash
rez env iterCmds -- sceneRunner --node <node_name>
```
- **`<node_name>`**: The name of the node whose attributes are to be displayed.

## Examples

### Example 1: Load a Scene from Local Path
```bash
rez env iterCmds -- sceneRunner --lpa get_element_mysql
```

### Example 2: Run a Node
```bash
rez env iterCmds -- sceneRunner --lpa get_element_mysql --run Run nodes
```

### Example 3: Fetch Attributes of a Node
```bash
rez env iterCmds -- sceneRunner --lpa get_element_mysql --node Echo stream attributes
```

### Example 4: Set Attributes node value
```bash
rez env iterCmds -- sceneRunner --lpa CONSTANTS --set "root:editAttributeName:value" --set "project:editAttributeName:value"
```

For further questions, feel free to contact the repository maintainer.

---

## License

```text
Custom License Agreement

Copyright (c) 2024 Felix Benicourt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to use,
study, and modify the Software for personal, educational, or internal purposes,
subject to the following conditions:

1. Redistribution and Resale:
   - Redistribution, sublicensing, or resale of the Software, in whole or in part, 
     is strictly prohibited without prior written consent from the author.

2. Attribution:
   - This copyright notice and permission notice shall be included in all copies 
     or substantial portions of the Software.

3. No Warranty:
   - THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
     IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
     FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL 
     THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER 
     LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING 
     FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
     IN THE SOFTWARE.
```
