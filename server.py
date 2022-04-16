from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

# DATA

learning_data = {
    "1": { 
    "id": "1", 
    "page_title": "Introduction",
    "info1": ["What is a distress signal?", "A distress signal, also known as a distress call, is an internationally recognized way of indicating that you are in serious and/or immediate danger and are in need of help."],
    "info2": [ "","You should not use a distress signal if you are not in serious and/or immediate danger."],
    "info3":[ "",""],
    "media": ["https://pbs.twimg.com/media/DPPj9YeXcAI2P8D.jpg","https://aceboater.com/media/guide/1/visual-distress-signals.jpg"],
    "category": "introduction",
    "subcategory": ""
    },
    "2": { 
    "id": "2", 
    "page_title": "Maritime Distress Signals",
    "info1": ["","We will first go over maritime boat signals, that is, distress signals that ships at sea use to communicate need for help."],
    "info2": [ "","The types of signals are divided into three categories: visual, sound, and radio."],
    "info3": [ "",""],
   "media":["https://assets.kalkomey.com/boaterexam/images/fm/boatingresources/visual-distress-signals.gif"],
    "category": "maritime",
    "subcategory": "intro"
    },
    "3": { 
    "id": "3", 
    "page_title": "Visual Maritime Distress Signals",
    "info1": ["What are common visual distress signals?", ["Red flares/sparks","Orange Smoke","Sea Marker Dye","Orange Distress Flag","Waving arms"]],
    "info2": [ "What is the benefit of visual distress signals?","The benefit of visual distress signals is that they not only draw attention to a ship’s distress from a distance but they help indicate the location of the troubled party.","Note: it is required by federal law for ships sailing on coastal waters to carry visual distress signals."],
    "info3": ["","Note: it is required by federal law for ships sailing on coastal waters to carry visual distress signals."],
    "media":["https://ke-courses-production.s3.amazonaws.com/asset_files/production/1559/attachments/original/distress_signals_set.jpg?1503937958"],
    "category": "maritime",
    "subcategory": "visual"
    },
    "4": { 
    "id": "4", 
    "page_title": "Sound Maritime Distress Signals",
    "info1": ["What are common sound maritime distress signals?", ["Firing gun or rocket at regular intervals","Making a continuous sound with a fog-signaling apparatus (aka foghorn), bell, or whistle","Yelling for help (usually if there are no other options)"]],
    "info2": [ "What are the benefits of sound maritime distress signals?","They grab the attention of local vessels or settlements"],
    "info3": [ "",""],
    "media": ["https://www.plastimo.com/media/catalog/product/cache/2/image/1200x/040ec09b1e35df139433887a97daa66f/p/l/pls_trompe-.jpg","https://m.media-amazon.com/images/I/81InNZC9uDL.jpg"],
    "category": "maritime",
    "subcategory": "sound"
    },
    "5": { 
    "id": "5", 
    "page_title": "Maritime Radio Distress Signals",
    "info1": ["How do you communicate distress through the radio?", ["Transmit a spoken Mayday message ('Mayday, Mayday, Mayday. This is [boat name/call sign]. x3')", "Send out an SOS message by Morse Code "]],
    "info2": [ "","Fun fact: Mayday comes from the English pronunciation of the French phrase for help “m’aidez”"],
    "info3": [ "",""],
    "media": ["https://i0.wp.com/www.malpope.com/wp-content/uploads/2021/05/ba665b97967605506331d3bc0c012ab7-e1619862114772.jpg?resize=850%2C667&ssl=1","https://pbs.twimg.com/media/DPPj9YeXcAI2P8D.jpg"],
    "category": "maritime",
    "subcategory": "radio"
    },
    "6": { 
    "id": "6", 
    "page_title": "Maritime Distress Signals Review",
    "info1": ["Check out this short video to review what you’ve learned!", ""],
    "info2": [ "",""],
    "info3": [ "",""],
    "media": ["https://www.youtube.com/watch?v=zjVJKa7faW8&feature=emb_logo"],
    "category": "maritime",
    "subcategory": "video"
    },
    "7": { 
    "id": "7", 
    "page_title": "Wilderness Distress Signals",
    "info1": ["", "This group of distress signals applies if, for example, you are stranded on a deserted island or lost in the wilderness. These solution assume you do not have proper equipment like a satellite phone, flare, or whistle to call for help."],
    "info2": [ "",""],
    "info3": [ "",""],
    "media": ["https://media.30seconds.com/tip/lg/Youre-About-to-Be-Stranded-on-a-Deserted-Island-What-4-Ite-15490-8661b483e3-1516247705.jpg"],
    "category": "wilderness",
    "subcategory": "intro"
    },
    "8": { 
    "id": "8", 
    "page_title": "Reflective Surfaces",
    "info1": ["", "Reflective surfaces can be used to signal airplanes flying up above. A signal mirror is the preferred tool but anything reflective like a credit card or belt buckle will work."],
    "info2": [ "",""],
    "info3": [ "",""],
    "media": ["https://www.survivalresources.com/images/banner/PageHeader.Original.jpg"],
    "category": "wilderness",
    "subcategory": "reflective"
    },
    "9": { 
    "id": "9", 
    "page_title": "Signal Fires",
    "info1": ["Why light a signal fire", "A signal fire is useful because it can be see for miles."],
    "info2": [ "What should a signal fire look like?",["One or Three Signal Fires in a Triangle Formation in an open space","(Depending on Resources) First layer dry tinder, second layer wood kindling, third layer moss and decaying plant life (optional), final layer green leafy vegetation"]],
    "info3":[ "",""],
    "media": ["https://www.youtube.com/watch?v=0G857JwMsM8"],
    "category": "wilderness",
    "subcategory": "fire"
    },
     "10": { 
    "id": "10", 
    "page_title": "Street Distress Signals",
    "info1": ["", "Aside from being lost at sea or stranded on a deserted island, you may have other reasons to signal for distress. And though most people seem to have easy access to a phone at all times, there are scenarios when calling for help may not be possible."],
    "info2": [ "In what specific scenarios may one need to call for help but be unable to?","Domestic Violence, Human Trafficking, and Kidnapping"],
    "info3": [ "What should I do if I find myself in one of these scenarios and can’t call for help?","Do the international hand signal for help"],
    "media": ["https://www.verywellhealth.com/thmb/WNrtvId6QPMIaIYGnnEPXn6rqfk=/614x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/Tiktokhandsignalcloseup-FINAL-46d537b506fb484eb69b851c8acbf772.jpg"],
    "category": "streets",
    "subcategory": "intro"
    },
     "11": { 
    "id": "11", 
    "page_title": "Street Distress Signals",
    "info1": ["", ""],
    "info2": [ "",""],
    "info3": [ "",""],
    "media": ["https://www.youtube.com/watch?v=AFLZEQFIm7k&feature=emb_logo"],
    "category": "streets",
    "subcategory": "video"
    },
};

fire_simulation = {
    "1": { 
    "ordernum": "1", 
    "name":"Dry Tinder",
    "image":"https://b.rgbimg.com/users/l/lu/lusi/600/mgyuCEy.jpg"
    },
    "2": { 
    "ordernum": "3", 
    "name":"Moss/Decaying Plants",
    "image":"https://cdn.shopify.com/s/files/1/0260/8191/9066/products/Chartreuse_580x.png?v=1629396828"
    },
    "3": { 
    "ordernum": "4", 
    "name":"Leafy Vegetation",
    "image":"https://m.media-amazon.com/images/I/81BHFiAx4BL._AC_SX425_.jpg"
    },
     "4": { 
    "ordernum": "2", 
    "name":"Wood Kindling",
    "image":"https://m.media-amazon.com/images/I/513Xz4L6SHL._AC_US200_.jpg"
    } 
};



# current_id = 12;

# ROUTES

@app.route('/')
def welcome():
   return render_template('home_page.html', mostpopular = mostpopular)  

@app.route('/view/all')
def all_films():
    global data
    return render_template('all_films.html', all = data)   

@app.route('/view/<id>')
def film_info(id = None):
    global data
    movie = data[int(id)]
    return render_template('film_info.html', movie = movie)    
 
@app.route('/add')
def add_info():
    global data
    global all_characters
    global all_droids
    return render_template('add_film.html',all_characters = all_characters, all_droids = all_droids) 

@app.route('/edit/<id>')
def edit_info(id = None):
    global data
    global all_characters
    global all_droids
    movie = data[int(id)]
    return render_template('edit_film.html', movie = movie,all_characters = all_characters, all_droids = all_droids)    

# ajax to add
@app.route('/add_data', methods=['GET', 'POST'])
def add():
    global data 
    global current_id 

    json_data = request.get_json() 
    title = json_data["title"]
    release_year = json_data["release_year"]
    era = json_data["era"]
    series = json_data["category"]
    mains2 = json_data["main_characters"]
    mains = mains2.split(',')
    droids2 = json_data["droids"]
    droids = droids2.split(',')
    summary = json_data["summary"]
    imgurl = json_data["image"]
  
    current_id += 1
    new_id = current_id 
    new_entry = {
        "id":  str(current_id),
        "title": title,
        "release_year": release_year,
        "era": era,
        "category": series,
        "main_characters": mains,
        "droids": droids,
        "summary": summary,
        "image": imgurl
    }
    data[current_id]=new_entry
    return jsonify(data = data)

@app.route('/edit/edit_data/<id>', methods=['POST'])
def edit(id = None):
    global data 

    json_data = request.get_json() 
    title = json_data["title"]
    release_year = json_data["release_year"]
    era = json_data["era"]
    series = json_data["category"]
    mains2 = json_data["main_characters"]
    mains = mains2.split(',')
    droids2 = json_data["droids"]
    droids = droids2.split(',')
    summary = json_data["summary"]
    imgurl = json_data["image"]
  
    modified_entry = {
        "id": id,
        "title": title,
        "release_year": release_year,
        "era": era,
        "category": series,
        "main_characters": mains,
        "droids": droids,
        "summary": summary,
        "image": imgurl
    }
    data[int(id)]=modified_entry
    return jsonify(data = data)

@app.route('/search/<query>',methods=['GET'])
def search(query):
    global data
    results = []
    title_results = []
    category_results = []
    character_results = []
    droid_results = []
    sum_results = []
    for movie in data:
        if (query.casefold() in data[movie]["title"].casefold()):
            results.append(data[movie])
            title_results.append(data[movie])
        if (query.casefold() in data[movie]["category"].casefold()):
            results.append(data[movie])
            category_results.append(data[movie])
        if (query.casefold() in data[movie]["summary"].casefold()):
            results.append(data[movie])
            sum_results.append(data[movie])
        char_to_lower = ([x.casefold() for x in data[movie]["main_characters"]])
        for char in char_to_lower:
            if (query.casefold() in char):
                results.append(data[movie])
                character_results.append(data[movie])
        droid_to_lower = ([x.casefold() for x in data[movie]["droids"]])
        for droid in droid_to_lower:
            if (query.casefold() in droid):
                results.append(data[movie])
                droid_results.append(data[movie])

    return render_template('search.html', query = query,results = results, titleres = title_results,
    catres = category_results,charres = character_results,droidres = droid_results,sumres=sum_results) 

if __name__ == '__main__':
   app.run(debug = True)

