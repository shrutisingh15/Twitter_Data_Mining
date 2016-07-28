import pandas
from bokeh.charts import Bar, Scatter, output_file, show
from flask import Flask,render_template
from bokeh.embed import file_html,components



app = Flask(__name__)
@app.route('/')
def Diversity_Chart():
    datacsv = pandas.read_csv("datacsv.csv")
    p=Bar(datacsv, 'Newspaper', values='Lexical Diversity',xlabel='Newspaper',ylabel='Lexical Diversity',
          legend='top_left',bar_width = 0.1,group='Type')
             
    ##output_file("bar.html")
    script1, div1 = components(p)
    ##show(p)  
    return render_template('graph.html', script1=script1, div1=div1)   
     
@app.route('/relation')
def Relation_Chart():
    dataset = pandas.read_csv("dataset1.csv")
    s = Scatter(dataset, x= "Retweet_Count", y= "Favorite_Count",xlabel='Retweet_Count',ylabel='Favorite_Count',marker='diamond',color='green')
    script2, div2 = components(s)
    return render_template('compare.html', script2=script2, div2=div2)
    
if __name__ == '__main__':
        
    app.debug = True
    app.run(port=33507)