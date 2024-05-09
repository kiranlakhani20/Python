from xml.dom.minidom import parseString
from xml.parsers.xerces import XercesDOMParser, XercesDOMParserErrorHandler

class CustomErrorHandler(XercesDOMParserErrorHandler):
    def warning(self, exception):
        print(f"Warning: {exception.getMessage()}")
        return super().warning(exception)

    def error(self, exception):
        print(f"Error: {exception.getMessage()}")
        return super().error(exception)

    def fatalError(self, exception):
        print(f"Fatal Error: {exception.getMessage()}")
        return super().fatalError(exception)

def parse_xml(xml_string, create_entity_reference_nodes=True):
    # Create a XercesDOMParser instance
    parser = XercesDOMParser()
    
    # Set custom error handler
    error_handler = CustomErrorHandler()
    parser.setErrorHandler(error_handler)

    # Set option to control entity reference nodes creation
    if not create_entity_reference_nodes:
        parser.setCreateEntityReferenceNodes(false)

    try:
        # Parse the XML string
        parser.parseString(xml_string)
        dom = parser.getDocument()

        # Get the root element
        root = dom.documentElement
        print(f"Root element: {root.tagName}")

        # Process other elements as needed
        # For example, print all child nodes
        for node in root.childNodes:
            if node.nodeType == node.ELEMENT_NODE:
                print(f"Element: {node.tagName}, Value: {node.firstChild.nodeValue}")

    except Exception as e:
        print(f"Error parsing XML: {e}")

if __name__ == "__main__":
    xml_data = """
    <example>
        <item id="1">Item 1</item>
        <item id="2">Item 2</item>
        <item id="3">Item 3</item>
    </example>
    """
    parse_xml(xml_data)
