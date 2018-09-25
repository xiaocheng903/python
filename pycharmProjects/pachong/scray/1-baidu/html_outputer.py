#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.data=[]

    def output_html(self):
        ff=open('output.html','w', encoding="utf-8")


        ff.write('<html>')
        ff.write("<html><meta charset=\"utf-8\" />")
        ff.write('<body>')
        ff.write('<table border="1">')

        for data in self.data:
            ff.write('<tr>')
            ff.write('<td>%s</td>'% data['url'])
            ff.write('<td>%s</td>' % data['title'].encode('utf-8').decode("utf-8"))
            ff.write('<td>%s</td>' % data['summary'].encode('utf-8').decode("utf-8"))
            ff.write('</tr>')

        ff.write('</table>')
        ff.write('</body>')
        ff.write('</html>')


        ff.close()
    def collect_data(self, new_data):
        if new_data is None:
            return
        self.data.append(new_data)