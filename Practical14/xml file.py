import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XMLParser
from xml.sax import make_parser, handler
import matplotlib.pyplot as plt
import datetime

from xml.sax import make_parser, handler
import datetime

class SaxHandler(handler.ContentHandler):
    def __init__(self):
        self.counts = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
        self.namespace_text = ""  # 用于累积<namespace>的文本内容

    def startElement(self, tag, attributes):
        # 重置namespace_text以准备接收新的<namespace>文本
        if tag == 'namespace':
            self.namespace_text = ""

    def characters(self, content):
        # 累积<namespace>元素内的字符
        self.namespace_text += content

    def endElement(self, tag):
        # 当<namespace>结束时，更新计数器
        if tag == 'namespace':
            namespace_value = self.namespace_text.strip()
            if namespace_value in self.counts:
                self.counts[namespace_value] += 1
            self.namespace_text = ""  # 重置namespace_text

    def endTerm(self, tag):
        # 假设这是自定义方法，用于处理<term>结束时的逻辑
        # 这里可能不需要做任何事情，因为计数已经在endElement中处理了
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

# main函数和其他代码保持不变...


# 使用DOM API解析XML文件
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
    # 确保data字典中有对应的键
    mf_count = data.get('molecular_function', 0)
    bp_count = data.get('biological_process', 0)
    cc_count = data.get('cellular_component', 0)
    values = [mf_count, bp_count, cc_count]
    
    plt.bar(labels, values)
    plt.title('Gene Ontology Term Frequencies')
    plt.xlabel('Ontology')
    plt.ylabel('Frequency')
    plt.show()

# 主函数
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

    plot_data(sax_counts)  # 这里使用SAX的结果来绘制图表，你也可以选择使用DOM的结果
    plot_data(dom_counts)

if __name__ == "__main__":
    main()