from HTMLParser import HTMLParser
import os.path

save_path = '/Users/sur000e/workspace-mallet/walmart/output'
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    startTag = "abc"
    number = 210

    def handle_starttag(self, tag, attrs):
        if self.startTag == "div":
            self.startTag+=tag
        else:
            self.startTag = tag
        # print "Encountered a start tag:", tag

    # def handle_endtag(self, tag):
    #     print "Encountered an end tag :", tag

    def handle_data(self, data):
        if self.startTag == "divp":
            filename = "comment" + str(self.number) + ".txt"
            fullname = os.path.join(save_path,filename)
            file = open(fullname,'w')
            self.number+=1
            file.write(data)
            file.close()


parser = MyHTMLParser()
with open('input/6.html', 'r') as file:
    data=file.read()
parser.feed(data)
