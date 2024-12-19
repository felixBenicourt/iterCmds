


import argparse
import os
import sys
import logging
from commands import iter_instance


"""
rez env iterCmds -- sceneRunner --lpa get_element_mysql --run Run nodes --node Echo stream attributes
rez env iterCmds -- sceneRunner --lpa python_iter --run Run nodes --node Echo stream attributes
"""


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
        logging.error("Scene file not found: %s", scene_file)
        return None
    else:
        logging.info("Opening scene: %s", scene_file)
        iter_instance.fileLoad(scene_file)
        return scene_file

def run_node(node_name):
    """Run a specific node by name."""
    isRun = iter_instance.getNodeFromCustomName(node_name)
    if isRun:
        logging.info("Running node: %s", node_name)
        isRun.evalImplementation()
    else:
        logging.warning("Node not found: %s", node_name)
        return None

def get_node_attributes(node_name):
    """Get attributes of a specific node by name."""
    node = iter_instance.getNodeFromCustomName(node_name)
    if node:
        logging.info("Node found: %s", node_name)
        attributes = node.getAttributs()
        logging.debug("Node attributes: %s", attributes)
    else:
        logging.warning("No node found with the name: %s", node_name)

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
        "--node",
        type=str,
        nargs="+",
        help="Get attributes of specific nodes by name."
    )

    args = parser.parse_args()

    try:
        if args.lpa:
            local_folder = os.path.dirname(os.path.abspath(__file__))
            scene_path = os.path.join(local_folder, f"{args.lpa}.json")
            load_scene(scene_path)

        if args.run:
            run_command = " ".join(args.run)
            logging.info("Executing run command: %s", run_command)
            run_node(run_command)

        if args.pa:
            load_scene(args.pa)

        if args.node:
            node_command = " ".join(args.node)
            logging.info("Fetching attributes for node: %s", node_command)
            get_node_attributes(node_command)

    except Exception as e:
        logging.error("An error occurred: %s", e, exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
