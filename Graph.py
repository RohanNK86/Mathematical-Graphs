import matplotlib.pyplot as pt

labels = ['Python','Java','Ruby','C++','Javascript']
values = [320,220,180,250,278]

pt.pie(values, labels=labels, autopct='%.1f%%')
pt.title("Programming Language Usage")
pt.show()
