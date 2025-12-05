# lib/tree.py

class Tree:
    def __init__(self, data):
        """
        Initialize a Tree node from a dictionary.
        Expected keys: 'tag_name', 'id', 'text_content' (optional), 'children' (optional)
        """
        self.tag_name = data.get('tag_name')
        self.id = data.get('id')
        self.text_content = data.get('text_content', '')
        self.children = []
        for child_data in data.get('children', []):
            self.children.append(Tree(child_data))

    def get_element_by_id(self, element_id):
        """
        Recursively search for a node with a given id and return it as a dictionary.
        """
        if self.id == element_id:
            return {
                'tag_name': self.tag_name,
                'id': self.id,
                'text_content': self.text_content,
                'children': [child.to_dict() for child in self.children]
            }

        for child in self.children:
            result = child.get_element_by_id(element_id)
            if result:
                return result

        return None

    def to_dict(self):
        """
        Convert Tree node to a dictionary.
        """
        return {
            'tag_name': self.tag_name,
            'id': self.id,
            'text_content': self.text_content,
            'children': [child.to_dict() for child in self.children]
        }
