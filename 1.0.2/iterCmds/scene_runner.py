

import argparse
import os
import sys
import logging
from commands import iter_instance


"""
rez env iterCmds -- sceneRunner --lpa get_element_mysql --run Run nodes --echo Echo stream attributes
rez env iterCmds -- sceneRunner --lpa python_iter --run Run nodes --echo Echo stream attributes
rez env iterCmds -- sceneRunner --lpa CONSTANTS --echo Echo stream attributes
rez env iterCmds -- sceneRunner --lpa CONSTANTS --set "root:editAttributeName:value" --set "project:editAttributeName:value" --echo Echo stream attributes
"""

# this is a test

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("scene_runner.log"),
        logging.StreamHandler(sys.stdout)
    ]
)


def load_scene(scene_file):
    """Load a scene or JSON configuration."""
    if not os.path.exists(scene_file):
        logging.error(f"Scene file not found: {scene_file}")
        return None
    else:
        logging.info(f"Opening scene: {scene_file}")
        iter_instance.fileLoad(scene_file)
        return scene_file


def run_node(node_name):
    """Run a specific node by name."""
    isRun = iter_instance.getNodeFromCustomName(node_name)
    if isRun:
        logging.info(f"Running node: {node_name}")
        isRun.evalImplementation()
    else:
        logging.warning(f"Node not found: {node_name}")
        return None


def get_node_attributes(node_name):
    """Get attributes of a specific node by name."""
    node = iter_instance.getNodeFromCustomName(node_name)
    if node:
        logging.info(f"Node found: {node_name}")
        attributes = node.getAttributs()
        logging.debug(f"Node attributes: {attributes[node.id]}")
    else:
        logging.warning(f"No node found with the name: {node_name}")


def set_node_values(set_commands):
    for command in set_commands:
        try:
            parts = command.split(":")
            if len(parts) != 3:
                raise ValueError(f"Invalid format: {command}")
            node_name, attribute, value = parts
            node = iter_instance.getNodeFromCustomName(node_name.strip())
            if node:
                logging.info(f"Setting value for node '{node_name}', attribute '{attribute}' to '{value}'")
                node.evalImplementation()
                node.value[attribute] = value
                logging.debug(f"Updated value for '{node_name}': {node.evalValue[node.id]}")
            else:
                logging.warning(f"Node not found: {node_name}")
        except Exception as e:
            logging.error(f"Error processing set command '{command}': {e}")


def main():
    parser = argparse.ArgumentParser(description="scene_runner - A script to open scenes and run nodes.")
    parser.add_argument(
        "--lpa",
        type=str,
        help="Local path to the ITER scene."
    )
    parser.add_argument(
        "--pa",
        type=str,
        help="Path to the ITER scene."
    )
    parser.add_argument(
        "--run",
        type=str,
        nargs="+",
        help="Run specific nodes by name."
    )
    parser.add_argument(
        "--echo",
        type=str,
        nargs="+",
        help="Get attributes of specific nodes by name."
    )
    parser.add_argument(
        "--set",
        type=str,
        action="extend",
        nargs="+",
        help="Set attributes for nodes in the format 'node_name:attribute_name:value'."
    )

    args = parser.parse_args()

    try:
        if args.lpa:
            local_folder = os.path.dirname(os.path.abspath(__file__))
            scene_path = os.path.join(local_folder, f"{args.lpa}.json")
            load_scene(scene_path)

        if args.pa:
            load_scene(args.pa)

        if args.set:
            logging.info("Setting node attributes.")
            set_node_values(args.set)

        if args.run:
            run_command = " ".join(args.run)
            logging.info(f"Executing run command: {run_command}")
            run_node(run_command)

        if args.echo:
            node_command = " ".join(args.echo)
            logging.info(f"Fetching attributes for node: {node_command}")
            get_node_attributes(node_command)


    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()

