from flask import Flask, render_template, request
import pandas as pd

# 模块
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go
import pyecharts
import warnings
import numpy as np 
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.globals import ChartType, SymbolType,CurrentConfig
from jinja2 import Markup, Environment, FileSystemLoader
#from map import map_world
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))
warnings.filterwarnings("ignore")

data = pd.read_csv('Potentially_Excess_Deaths_from_the_Five_Leading_Causes_of_Death_2005_Fixed.csv')
app = Flask(__name__, static_folder="templates")
#配置缓存最大时间  
a=[]
for i in np.arange(2005,2016):
    a.append(str(i))


@app.route('/Cancer',methods=['GET'])
def Cancer():
    return render_template('Cancer.html') 
  
@app.route('/2005-Cancer')
def Cancer_2005():
    return render_template('2005/2005-Cancer.html',)

@app.route('/2006-Cancer')
def Cancer_2006():
    return render_template('2006/2006-Cancer.html',) 

@app.route('/2007-Cancer')
def Cancer_2007():
    return render_template('2007/2007-Cancer.html',) 

@app.route('/2008-Cancer')
def Cancer_2008():
    return render_template('2008/2008-Cancer.html',) 

@app.route('/2009-Cancer')
def Cancer_2009():
    return render_template('2009/2009-Cancer.html',) 

@app.route('/2010-Cancer')
def Cancer_2010():
    return render_template('2010/2010-Cancer.html',) 

@app.route('/2011-Cancer')
def Cancer_2011():
    return render_template('2011/2011-Cancer.html',) 

@app.route('/2012-Cancer')
def Cancer_2012():
    return render_template('2012/2012-Cancer.html',) 

@app.route('/2013-Cancer')
def Cancer_2013():
    return render_template('2013/2013-Cancer.html',) 

@app.route('/2014-Cancer')
def Cancer_2014():
    return render_template('2014/2014-Cancer.html',) 

@app.route('/2015-Cancer')
def Cancer_2015():
    return render_template('2015/2015-Cancer.html',) 
 


@app.route('/Chronic',methods=['GET'])
def Chronic():
    return render_template('Chronic.html')  

@app.route('/2005-Chronic')
def Chronic_2005():
    return render_template('2005/2005-Chronic Lower Respiratory Disease.html',)

@app.route('/2006-Chronic')
def Chronic_2006():
    return render_template('2006/2006-Chronic Lower Respiratory Disease.html',) 

@app.route('/2007-Chronic')
def Chronic_2007():
    return render_template('2007/2007-Chronic Lower Respiratory Disease.html',) 

@app.route('/2008-Chronic')
def Chronic_2008():
    return render_template('2008/2008-Chronic Lower Respiratory Disease.html',) 

@app.route('/2009-Chronic')
def Chronic_2009():
    return render_template('2009/2009-Chronic Lower Respiratory Disease.html',) 

@app.route('/2010-Chronic')
def Chronic_2010():
    return render_template('2010/2010-Chronic Lower Respiratory Disease.html',) 

@app.route('/2011-Chronic')
def Chronic_2011():
    return render_template('2011/2011-Chronic Lower Respiratory Disease.html',) 

@app.route('/2012-Chronic')
def Chronic_2012():
    return render_template('2012/2012-Chronic Lower Respiratory Disease.html',) 

@app.route('/2013-Chronic')
def Chronic_2013():
    return render_template('2013/2013-Chronic Lower Respiratory Disease.html',) 

@app.route('/2014-Chronic')
def Chronic_2014():
    return render_template('2014/2014-Chronic Lower Respiratory Disease.html',) 

@app.route('/2015-Chronic')
def Chronic_2015():
    return render_template('2015/2015-Chronic Lower Respiratory Disease.html',) 


@app.route('/Heart',methods=['GET'])
def Heart():
    return render_template('Heart.html')  


@app.route('/2005-Heart')
def Heart_2005():
    return render_template('2005/2005-Heart Disease.html',)

@app.route('/2006-Heart')
def Heart_2006():
    return render_template('2006/2006-Heart Disease.html',) 

@app.route('/2007-Heart')
def Heart_2007():
    return render_template('2007/2007-Heart Disease.html',) 

@app.route('/2008-Heart')
def Heart_2008():
    return render_template('2008/2008-Heart Disease.html',) 

@app.route('/2009-Heart')
def Heart_2009():
    return render_template('2009/2009-Heart Disease.html',) 

@app.route('/2010-Heart')
def Heart_2010():
    return render_template('2010/2010-Heart Disease.html',) 

@app.route('/2011-Heart')
def Heart_2011():
    return render_template('2011/2011-Heart Disease.html',) 

@app.route('/2012-Heart')
def Heart_2012():
    return render_template('2012/2012-Heart Disease.html',) 

@app.route('/2013-Heart')
def Heart_2013():
    return render_template('2013/2013-Heart Disease.html',) 

@app.route('/2014-Heart')
def Heart_2014():
    return render_template('2014/2014-Heart Disease.html',) 

@app.route('/2015-Heart')
def Heart_2015():
    return render_template('2015/2015-Heart Disease.html',)



@app.route('/Stroke',methods=['GET'])
def Stroke():
    return render_template('Stroke.html') 

@app.route('/2005-Stroke')
def Stroke_2005():
    return render_template('2005/2005-Stroke.html',)

@app.route('/2006-Stroke')
def Stroke_2006():
    return render_template('2006/2006-Stroke.html',) 

@app.route('/2007-Stroke')
def Stroke_2007():
    return render_template('2007/2007-Stroke.html',) 

@app.route('/2008-Stroke')
def Stroke_2008():
    return render_template('2008/2008-Stroke.html',) 

@app.route('/2009-Stroke')
def Stroke_2009():
    return render_template('2009/2009-Stroke.html',) 

@app.route('/2010-Stroke')
def Stroke_2010():
    return render_template('2010/2010-Stroke.html',) 

@app.route('/2011-Stroke')
def Stroke_2011():
    return render_template('2011/2011-Stroke.html',) 

@app.route('/2012-Stroke')
def Stroke_2012():
    return render_template('2012/2012-Stroke.html',) 

@app.route('/2013-Stroke')
def Stroke_2013():
    return render_template('2013/2013-Stroke.html',) 

@app.route('/2014-Stroke')
def Stroke_2014():
    return render_template('2014/2014-Stroke.html',) 

@app.route('/2015-Stroke')
def Stroke_2015():
    return render_template('2015/2015-Stroke.html',) 


    
    

    
@app.route('/Unintentional',methods=['GET'])
def Unintentional():
    return render_template('Unintentional.html') 

@app.route('/2005-Unintentional')
def Unintentional_2005():
    return render_template('2005/2005-Unintentional Injury.html',)

@app.route('/2006-Unintentional')
def Unintentional_2006():
    return render_template('2006/2006-Unintentional Injury.html',) 

@app.route('/2007-Unintentional')
def Unintentional_2007():
    return render_template('2007/2007-Unintentional Injury.html',) 

@app.route('/2008-Unintentional')
def Unintentional_2008():
    return render_template('2008/2008-Unintentional Injury.html',) 

@app.route('/2009-Unintentional')
def Unintentional_2009():
    return render_template('2009/2009-Unintentional Injury.html',) 

@app.route('/2010-Unintentional')
def Unintentional_2010():
    return render_template('2010/2010-Unintentional Injury.html',) 

@app.route('/2011-Unintentional')
def Unintentional_2011():
    return render_template('2011/2011-Unintentional Injury.html',) 

@app.route('/2012-Unintentional')
def Unintentional_2012():
    return render_template('2012/2012-Unintentional Injury.html',) 

@app.route('/2013-Unintentional')
def Unintentional_2013():
    return render_template('2013/2013-Unintentional Injury.html',) 

@app.route('/2014-Unintentional')
def Unintentional_2014():
    return render_template('2014/2014-Unintentional Injury.html',) 

@app.route('/2015-Unintentional')
def Unintentional_2015():
    return render_template('2015/2015-Unintentional Injury.html',) 


    



@app.route('/') 
@app.route('/index',methods=['POST'])
def entry_page() -> 'html':
    return render_template('index.html')

if __name__ == '__main__':

    app.run(port = 9002)   # debug=True, 在py使用, 在ipynb不使用
    
    
    

    
    
    
    
    
    
    
    
    