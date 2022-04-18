from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)
import datetime
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
    "media": ["https://www.youtube.com/embed/zjVJKa7faW8"],
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
    "media": ["https://www.youtube.com/embed/0G857JwMsM8"],
    "category": "wilderness",
    "subcategory": "video"
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
    "media": ["https://www.youtube.com/embed/AFLZEQFIm7k"],
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

test_data = {
    "1": {"id": "1",
          "question": "Which of the following is not a category of maritime distress signal?",
          "a": "Visual",
          "b": "Sound",
          "c": "Olfactory",
          "d": "Radio"},
    "2": {"id": "2", "question": "True or False? You separate your first two and second two fingers to indicate distress.",
          "a": "True",
          "b": "False",
          "c": None,
          "d": None},
    "3": {"id": "3",
          "question": "Which of the following is not ideal fuel for your signal fire?",
          "a": "Moss",
          "b": "Twig",
          "c": "Wet Wood",
          "d": "Leafy Vegetation"},
    "4": {"id": "4",
          "question": "How many times (at minimum) should you repeat “Mayday” when sending a distress signal over the radio?",
          "a": "1",
          "b": "2",
          "c": "3",
          "d": "4"},
    "5": {"id": "5",
          "question": "Which of the following is not a common visual maritime distress signal?",
          "a": "Orange sea dye",
          "b": "Red sea dye",
          "c": "Orange Flag",
          "d": "Red sparks"},
}

test_answers = {
    "1": "c",
    "2": "b",
    "3": "c",
    "4": "c",
    "5": "b",
    }

# fill in the rest of quiz info
feedback = {
    "1": "temp",
    "2": "",
    "3": "",
    "4": "",
    "5": "",
    }

activity = {}

score = 0

# current_id = 12;

# ROUTES

@app.route('/')
def welcome():
   global activity
   time = datetime.datetime.now()
   activity[str(time)] = 'home page'
   return render_template('home_page.html')  

@app.route('/learn/introduction')
def learn_intro():
    global learning_data
    page_info = learning_data["1"]
    next_category = learning_data["2"]["category"]
    next_subcategory = learning_data["2"]["subcategory"]
    print(page_info)
    global activity
    time = datetime.datetime.now()
    activity[str(time)] = 'introduction'
    return render_template('learning.html', page_info = page_info, learning_data = learning_data, next_category=next_category,next_subcategory=next_subcategory)  

@app.route('/learn/<category>/<subcategory>')
def learn(category,subcategory):
    global activity
    time = datetime.datetime.now()
    activity[str(time)] = category+"/"+subcategory
    
    global learning_data
    page_info = {}
    for item in learning_data:
        # print(learning_data[item])
        if category == learning_data[item]["category"] and subcategory == learning_data[item]["subcategory"]:
            page_info = learning_data[item]
    # print(page_info)
    next_id = str(int(page_info["id"]) + 1)
    print(next_id)
    next_category = learning_data[next_id]["category"]
    next_subcategory = learning_data[next_id]["subcategory"]
    if page_info["subcategory"] == "video":
        video_link = page_info["media"][0].replace("watch?v=", "embed/watch?v=")
        return render_template('learningvideo.html', page_info = page_info, learning_data = learning_data,next_category=next_category,next_subcategory=next_subcategory,video_link=video_link) 
    else:  
        return render_template('learning.html', page_info = page_info, learning_data = learning_data,next_category=next_category,next_subcategory=next_subcategory)   

@app.route('/learn/signal_fire_activity')
def build_a_fire():
    global fire_simulation
    return render_template('firesim.html', fire_material = fire_simulation)   

# @app.route('/view/<id>')
# def film_info(id = None):
#     global data
#     movie = data[int(id)]
#     return render_template('film_info.html', movie = movie)    

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/log_in')
def log_in():
    return render_template('log_in.html')

@app.route('/test/homepage')
def th():
    global score
    score = 0
    
    return render_template('testhomepage.html')


@app.route('/test/<id>')
def test(id=None):
    
    one = test_data[id]
    next_id = str(int(id) + 1)
    return render_template('test.html', one=one, next_id=next_id)

@app.route('/record')
def get_record():
    print(activity)
    return render_template('record.html', activity = activity)

# ajax for checking answer in test.js
@app.route('/check_ans', methods=['GET', 'POST'])
def check_ans():
    global score
    json_data = request.get_json()  
    
    ans = json_data["ans"]
    num = json_data["num"]
    
    correct = "False"
    
    if ans == test_answers[num]:
        correct = "True"
        score += 1
    
    fb = feedback[num]
    
    return jsonify(feedback=fb, correct=correct)

@app.route('/certificate')
def certificate():
    grade = score / len(test_data) * 100
    return render_template('certificate.html', grade=grade)

if __name__ == '__main__':
   app.run(debug = True)

