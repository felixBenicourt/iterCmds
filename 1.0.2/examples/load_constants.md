
# Using IterCmds to Load a Scene and Print Node Attributes

## Pages

1. [README](../../README.md)
2. [load constants example](./load_constants.md)

---

## Example: Creating a Scene and Accessing Node Variables

This example demonstrates how IterCmds is designed to interact with scenes using commands with arguments.

---

### Step 1: Create and Configure Nodes Scene

Create a scene named **CONSTANTS**.

1. Add multiple **Constant Nodes** and define their key-value pairs.
2. Merge these nodes and manipulate their data as needed.
3. Include an **Echo Stream Attribute Node**, and rename it for clarity (e.g., "Echo var").

![Step 1](https://i.imgur.com/9Oy0txQ.png)

---

### Step 2: Create a Scene that Can Get the Data

Create a scene named **python_iter**.

1. Add a read file node and get the **CONSTANTS** scene path.
2. Create a Python Iter node with the following code:

```python
from commands import iter_instance

iter_instance.fileLoad(input_data['path'])

echoNode = iter_instance.getNodeFromCustomName("Echo stream attributes")

if echoNode:
    print({'test': echoNode.calcAttributes()})
else:
    print({'test': None})
```

3. Include an **Echo Stream Attribute Node** and a **Run nodes** node.
4. Save the scene as **python_iter**.

![Step 2](https://i.imgur.com/CG3swTC.png)

---

### Step 3: Running the Scene

Use the following command to run the scene and fetch the attributes:

```bash
rez env iterCmds -- sceneRunner --lpa python_iter --run Run nodes --node Echo stream attributes
```

---

### Output

After running the above command, you should see the following output:

```bash
C:\Windows\System32>rez env iterCmds -- sceneRunner --lpa python_iter --run Run nodes --node Echo stream attributes
2024-12-19 17:08:31,599 - INFO - Opening scene: c:\pipeline\prod\iterCmds.0.2\iterCmds\python_iter.json
2024-12-19 17:08:31,688 - DEBUG - Input is not connected on node Run nodes
2024-12-19 17:08:31,704 - INFO - Executing run command: Run nodes
2024-12-19 17:08:31,704 - INFO - Running node: Run nodes
2024-12-19 17:08:31,705 - DEBUG - List of nodes: ['Read file'] is going to be evaluated
2024-12-19 17:08:31,705 - DEBUG - Connected node: Read file named Read file is going to be evaluated
2024-12-19 17:08:31,707 - DEBUG - Input reference node info: {'path': 'C:/pipeline/PROD/iterCmds/1.0.2/iterCmds/CONSTANTS.json'}
2024-12-19 17:08:32,467 - DEBUG - Received output from subprocess: {"output": "{'test': {'path_constants': 'C:\\HOME\\proj\\template', 'root_constants': 'C:\\HOME\\proj', 'name_constants': 'template'}}
"}
2024-12-19 17:08:32,468 - DEBUG - Parsed nested dictionary successfully: {'test': {'path_constants': 'C:\HOME\proj\template', 'root_constants': 'C:\HOME\proj', 'name_constants': 'template'}}
2024-12-19 17:08:32,468 - DEBUG - Run Node has been executed
2024-12-19 17:08:32,469 - INFO - Fetching attributes for node: Echo stream attributes
2024-12-19 17:08:32,469 - INFO - Node found: Echo stream attributes
2024-12-19 17:08:32,470 - DEBUG - Node attributes: {2236866897584: {'path': 'C:/pipeline/PROD/iterCmds/1.0.2/iterCmds/CONSTANTS.json', 'test': {'path_constants': 'C:\HOME\proj\template', 'root_constants': 'C:\HOME\proj', 'name_constants': 'template'}}}
```

This output shows the parsed attributes from the **Echo Stream Attribute Node** along with the corresponding path and key-value pairs.

What's particularly interesting about this process is the following line from the output:

```bash
2024-12-19 17:08:32,470 - DEBUG - Node attributes: {2236866897584: {'path': 'C:/pipeline/PROD/iterCmds/1.0.2/iterCmds/CONSTANTS.json', 'test': {'path_constants': 'C:\HOME\proj\template', 'root_constants': 'C:\HOME\proj', 'name_constants': 'template'}}}
```

In this case, we opened the **python_iter** scene, which contains a node graph that uses a Python script with the Iter API. This script loads the **CONSTANTS** scene, retrieves the variables, and then echoes them. The key point here is how the IterCmds API is leveraged to access the scene data, and how the attributes of the nodes, including their key-value pairs, are fetched and printed in the debug output. The Echo Stream Attribute Node provides a convenient way to view the parsed node attributes, which include paths and key-value pairs—critical pieces of data for further processing or manipulation.




