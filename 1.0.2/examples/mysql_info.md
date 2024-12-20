# iterCmds

A sandbox repository for development purposes with Iter and other tools.  
Additional documentation and specific examples will be provided in the future.

## Pages

1. [README](../../README.md)
2. [Load Constants Example](./load_constants.md)
3. [MySQL Manipulation](./mysql_info.md)

---

## Example: Creating a Scene and Accessing Node Variables

This example demonstrates how **IterCmds** interacts with scenes using commands and arguments. The twist now is that we can use the **k_mysql** package to manipulate the database directly.

---

### Step 1: Create and Configure Nodes in the Scene

In this step, we will create a scene named **insert_element_mysql**.

![Step 1](https://i.imgur.com/rpbdtBE.png)

In the **get asset** Python Iter Node script:

```python
from k_mysql.mysql_wrapper import MySQLDatabase

db_class = MySQLDatabase(
    "localhost", 
    "root", 
    "", 
    input_data['db_name']
)

assets = db_class.get_elements_by_name(
    table_name = input_data['table_name'],
    name_column = "name",
    name_value = input_data["asset_name"]
)

filtered = db_class.filter_dicts(
    assets,
    "task",
    input_data["task_name"]
)

latest = db_class.get_highest_value(
    filtered,
    "version"
)

print({"asset": latest})

db_class.disconnect()
```

The variable **input_data** is the dictionary derived from the **stream attributes list**.

The command line to execute the scene:
```bash
rez env iterCmds -- sceneRunner --lpa insert_element_mysql --run Run nodes --echo Echo stream attributes
```

To change the parameter of a node, use the following command:

```bash
rez env iterCmds -- sceneRunner --lpa insert_element_mysql --set "asset name:editAttributeValue:name of the asset" --run Run nodes --echo Echo stream attributes
```

Here’s the result at the end:

```bash
2024-12-19 22:36:21,232 - DEBUG - Node attributes: {'db_name': 'home_db', 'project name': 'template', 'project': {'id': 1, 'name': 'template'}, 'asset_name': 'thanos', 'type_name': 'chr', 'task_name': 'rig', 'variation_name': 'main'}
```

---

### Step 2: Create a Scene that Can Get the Data

In this step, we create a scene named **get_element_mysql**.

![Step 2](https://i.imgur.com/oaaGYqc.png)

in the **get project** Python Iter Node script :

```python
from k_mysql.mysql_wrapper import MySQLDatabase


db_class = MySQLDatabase("localhost", "root", "", "home_db")

project = db_class.get_elements_by_name(
    table_name = "project",
    name_column = "name",
    name_value = "template"
)

print({'project':project[0]})

db_class.disconnect()
```

in the **insert asset** Python Iter Node script :

```python
from k_mysql.mysql_wrapper import MySQLDatabase

db_class = MySQLDatabase(
    "localhost", 
    "root", 
    "", 
    input_data["db_name"]
)

db_class.insert_element(
    "asset",
    {"projectId":input_data["project"]["id"],
    "name":input_data["asset_name"], 
    "type":input_data["type_name"],
    "task":input_data["task_name"],
    "variation":input_data["variation_name"],
    "version":1,
    "status":"Approved"}
)

print({'asset_done':True})

db_class.disconnect()
```
The idea is to retrieve the project ID from the database using the project name and insert it into the **input_data["project"]["id"]**

The command line to execute the scene:
```bash
rez env iterCmds -- sceneRunner --lpa get_element_mysql --run Run nodes --echo Echo stream attributes
```

To change the parameter of a node:

```bash
rez env iterCmds -- sceneRunner --lpa get_element_mysql --set "asset name:editAttributeValue:name of the asset" --run Run nodes --echo Echo stream attributes
```

## Pages
- **k_mysql** is used here to interact with the MySQL database. It provides methods like **get_elements_by_name**, **filter_dicts**, **get_highest_value**, and **insert_element** for fetching and inserting data into the database.
- The **input_data** dictionary contains all the necessary attributes for the scene, such as the database name, asset name, task name, and more.
- The scene configuration and script examples demonstrate how to use **IterCmds** to manipulate nodes and perform database operations with the **k_mysql** package.


