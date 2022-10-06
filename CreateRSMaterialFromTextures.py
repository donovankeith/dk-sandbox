"""Name-en-US: Create RS Material from Textures...
Description-en-US: Select a texture file to auto-create a Redshift Standard material.
"""

import c4d
import maxon

def create_material():
    mat = c4d.BaseMaterial(c4d.Mmaterial)
    if mat is None:
        raise ValueError("Unable to create material.")

    return mat

def create_node_material(node_space_id=None):
    if node_space_id is None:
        node_space_id = c4d.GetActiveNodeSpaceId()
        if node_space_id is None:
            raise ValueError("Unable to get active node space.")

    mat = create_material()
    if mat is None:
        raise ValueError("Unable to create material.")

    node_material = mat.GetNodeMaterialReference()
    if node_material is None:
        raise ValueError("Unable to get mat as node material.")

    return node_material

def create_redshift_node_material():
    NODE_SPACE_REDSHIFT = "com.redshift3d.redshift4c4d.class.nodespace"
    mat = create_node_material(node_space_id=NODE_SPACE_REDSHIFT)
    if mat is None:
        raise ValueError("Unable to create redshift node material.")

    return mat

def main():
    node_material = create_redshift_node_material()
    if node_material is None:
        raise ValueError("Unable to create Redshift Material.")

    print(node_material)

if __name__ == "__main__":
    main()