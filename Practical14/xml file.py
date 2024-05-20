import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XMLParser
from xml.sax import make_parser, handler
import matplotlib.pyplot as plt
import datetime
# Using SAX API to parse the file
class SaxHandler(handler.ContentHandler):
    def __init__(self): # Initialise
        # Create a dictionary
        self.counts = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
        self.namespace_text = ""  
    def startElement(self, tag, attributes):
        # Reset namespace text
        if tag == 'namespace':
            self.namespace_text = ""
    def characters(self, content):
        self.namespace_text += content
    def endElement(self, tag):
        if tag == 'namespace':
            namespace_value = self.namespace_text.strip()
            if namespace_value in self.counts:
                self.counts[namespace_value] += 1
            self.namespace_text = ""  # Reset namespace text
    def endTerm(self, tag):
        pass

def parse_xml_sax(xml_file):
    handler = SaxHandler()
    parser = make_parser()
    parser.setContentHandler(handler)
    start_time = datetime.datetime.now()
    with open(xml_file, 'rb') as f:
        parser.parse(f)
    end_time = datetime.datetime.now()
    return handler.counts, (end_time - start_time).total_seconds()

# Using DOM API to parse the file
def parse_xml_dom(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    counts = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
    start_time = datetime.datetime.now()
    for term in root.findall('term'):
        namespace = term.find('namespace').text
        if namespace in counts:
            counts[namespace] += 1
    end_time = datetime.datetime.now()
    return counts, (end_time - start_time).total_seconds()

def plot_data(data):
    labels = ['Molecular Function', 'Biological Process', 'Cellular Component']
    # Make sure there are corresponding keys in dictionary
    mf_count = data.get('molecular_function', 0)
    bp_count = data.get('biological_process', 0)
    cc_count = data.get('cellular_component', 0)
    values = [mf_count, bp_count, cc_count]
    # Set the plot
    plt.bar(labels, values)
    plt.title('Gene Ontology Term Frequencies')
    plt.xlabel('Ontology')
    plt.ylabel('Frequency')
    plt.show()

def main():
    file_path ="C:\\Users\\wangj\\Desktop\\data\\go_obo.xml"
    sax_counts, sax_time = parse_xml_sax(file_path)
    dom_counts, dom_time = parse_xml_dom(file_path)

    print(f"SAX API counts: {sax_counts}")
    print(f"DOM API counts: {dom_counts}")
    print(f"Time taken by SAX API: {sax_time} seconds")
    print(f"Time taken by DOM API: {dom_time} seconds")
    if sax_time < dom_time:
        print("SAX API was faster.")
    else:
        print("DOM API was faster.")

    plot_data(sax_counts)  # Draw the plot of SAX
    plot_data(dom_counts)  # Draw the plot of DOM

if __name__ == "__main__":
    main()