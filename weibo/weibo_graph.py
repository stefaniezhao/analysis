import networkx as nx
import xml.sax

class RecordHandler(xml.sax.ContentHandler):
    
    def __init__(self, g):
        self.graph=g
        self.parentflag = False
        self.src = False
        self.srcExist = False
        self.tar = False
        self.tarExist = False
        self.tar_num = 0
        self.srcPerson = ""

    def characters(self, content):
        if self.src:
            #print "source is " + content
            isAdded = self.graph.addNode(content)
            if(not isAdded):
                self.srcExist = False
            else :
                self.srcExist = True
                self.srcPerson = content
            self.src = False
        elif self.tar:
            if (not self.srcExist) and (self.tar_num > 20) : return
            else :
                #print "target is " + content
                isAdded = self.graph.addNode(content)
                if isAdded :
                    self.graph.addEage(self.srcPerson, content)
                    self.tar = False
                    self.srcPerson = ""
    
    def startElement(self, name, attr):
        if name == "RECORD":
           self.parentflag = True
           self.tar_num = 0
           return
        if self.parentflag:
           if name == "person_id":
               self.src = True
           elif name == "guanzhu_id":
                self.tar = True
                self.tar_num += 1

    def endElement(self,name):
        if name == "RECORD":
            self.parentflag = False
            self.source = ""
            
class Graph(object):
    def __init__(self, f):
        self.g = nx.Graph()
        self.f = f
        self.nodes = set([])
        
    def addNode(self, name):
        if name in self.nodes: return True
        if len(self.nodes) > 200 : return False
        else:
            self.g.add_node(name)
            self.nodes.add(name)
            #print name + " add to graph"
            
    def addEage(self, src, tar):
        self.g.add_edge(src, tar)
        self.f.write('\t' + src + ' -- ' + tar + ';\n')

BUFSIZE = 81920       
BASE_FILE = '/home/stefaniezhao/development/dataset/weibo-relation-1000w/'

filepath = BASE_FILE + 'data.xml'
result_filepath = BASE_FILE + 'relation-result.dot'

f = open(filepath, 'r', BUFSIZE)
result_f = open(result_filepath, 'w', 1)

graph = Graph(result_f)

p = xml.sax.make_parser()
p.setContentHandler(RecordHandler(graph))

print "start to parse xml to build graph"
result_f.write('strict graph  {\n')
data = f.read(BUFSIZE)
i = 0
while(data and i < 3):
    print "parse " + str(i) + " block data"
    p.feed(data)
    data = f.read(BUFSIZE)
    i+=1

result_f.write('}\n')
print graph.g.nodes()
print graph.g.edges()
    
#print "save the graph as dot file"
#OUT ="/home/stefaniezhao/development/dataset/weibo-relation-1000w/result.dot"
#nx.drawing.write_dot(graph.g, OUT)
    


