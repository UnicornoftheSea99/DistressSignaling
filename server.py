from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

# DATA

data = { 
1: { 
"id": "1", 
"title": "Star Wars: Episode IV - A New Hope",
"release_year": 1977, 
"summary": """The film is set 19 years after the formation of the Galactic Empire and 
the events of Revenge of the Sith; construction has finished on the Death Star, 
a weapon capable of destroying a planet. After Princess Leia Organa, 
a leader of the Rebel Alliance, receives the weapon's plans in the hope of finding 
a weakness, she is captured and taken to the Death Star. Meanwhile, a young farmer 
named Luke Skywalker meets Obi-Wan Kenobi, who has lived in seclusion for years 
on the desert planet of Tatooine. When Luke's home is burned and his aunt and uncle 
killed, Obi-Wan begins Luke's Jedi training as they—along with Han Solo, Chewbacca, 
C-3PO, and R2-D2—attempt to rescue the princess from the Empire.""", 
"main_characters": ["Luke Skywalker", "Leia Organa", "Han Solo", "Darth Vader"],
"droids":["R2-D2", "C-3PO"],
"era": "0 ABY",
"category":"original",
"image": "https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"
},
2: { 
"id": "2", 
"title": "Star Wars: Episode V - The Empire Strikes Back",
"release_year": 1980, 
"summary": """The film concerns the continuing struggles of the Rebel Alliance against 
the Galactic Empire. During the film, Han Solo, Chewbacca, and Princess Leia Organa 
are being pursued across space by Darth Vader and his elite forces. Meanwhile, 
Luke Skywalker begins his major Jedi training with Yoda in Dagoba, after an instruction 
from Obi-Wan Kenobi's spirit. In an emotional and near-fatal confrontation with Vader, 
Luke is presented with a horrific revelation and must face his destiny. """, 
"main_characters": ["Luke Skywalker", "Leia Organa", "Han Solo", "Darth Vader"],
"droids":["R2-D2", "C-3PO"],
"era": "3 ABY",
"category":"original",
"image": "https://m.media-amazon.com/images/M/MV5BYmU1NDRjNDgtMzhiMi00NjZmLTg5NGItZDNiZjU5NTU4OTE0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"
},
3: { 
"id": "3", 
"title": "Star Wars: Episode VI - Return of the Jedi",
"release_year": 1983, 
"summary": """Luke Skywalker and friends travel to Tatooine to rescue their friend Han Solo
 from the vile Jabba the Hutt. The Empire prepares to crush the Rebellion with a more 
 powerful Death Star, while the Rebel fleet mounts a massive attack on the space station. 
 Luke Skywalker confronts his father, Anakin, in a final climactic duel before the evil 
 Emperor Sidious. Features iconic slave Leia bikini and ewoks.""", 
"main_characters": ["Luke Skywalker", "Leia Organa", "Han Solo", "Darth Vader"],
"droids":["R2-D2", "C-3PO"],
"era": "4 ABY",
"category":"original",
"image": "https://m.media-amazon.com/images/M/MV5BOWZlMjFiYzgtMTUzNC00Y2IzLTk1NTMtZmNhMTczNTk0ODk1XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg"
},
4: { 
"id": "4", 
"title": "Star Wars: Episode I - The Phantom Menace",
"release_year": 1999, 
"summary": """Thirty-two years before the events of Star Wars: Episode IV A New Hope, there
 is a trade dispute between the Trade Federation and the outlying systems of the Galactic
Republic, which has led to a blockade of the small planet of Naboo. Two Jedi, Master 
Qui-Gon Jinn and his Padawan, Obi-Wan Kenobi, liberate the queen and her guards from the 
battle-droid invasion. In their escape, the queen’s starship is damaged by Federation 
battleships and so the Jedi decide to land on the nearby planet Tatooine. While searching 
for a new hyperdrive generator, they befriend young Anakin Skywalker, a slave boy, who 
Qui-Gon believes may be the Chosen One and wants to train to become a Jedi.  The queen, 
after failing to get aid from the Galactic Senate, returns to Naboo and takes back her 
planet with the help of the Great Gungan Army. As this happens, Anakin accidentally takes 
control of a starfighter and goes on to destroy the Federation's Droid Control Ship from 
the inside and Qui-Gon and Obi-Wan fight sith apprentice Darth Maul.""", 
"main_characters": ["Anakin Skywalker", "Obi-Wan Kenobi", "Padme Amidala", "Qui-Gon Jinn"],
"droids":["R2-D2", "C-3PO", "Separist Droid Army"],
"era": "32 BBY",
"category":"prequel",
"image": "https://m.media-amazon.com/images/M/MV5BYTRhNjcwNWQtMGJmMi00NmQyLWE2YzItODVmMTdjNWI0ZDA2XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg"
},
5: { 
"id": "5", 
"title": "Star Wars: Episode II - Attack of the Clones",
"release_year": 2002, 
"summary": """The film is set nine years after the Battle of Naboo, when the galaxy is on 
the brink of civil war. Under the leadership of renegade Jedi Master Count Dooku, thousands
 of systems threaten to secede from the Republic. When an assassination attempt is made on
Senator Padmé Amidala, the former Queen of Naboo, Jedi apprentice Anakin Skywalker is 
assigned to protect her, while his mentor Obi-Wan Kenobi is assigned to investigate the
assassination attempt. Soon the Jedi are drawn into the heart of the Separatist movement,
and the beginning of a new threat to the galaxy: the Clone Wars.""", 
"main_characters": ["Anakin Skywalker", "Obi-Wan Kenobi", "Padme Amidala"],
"droids":["R2-D2", "C-3PO", "Separist Droid Army"],
"era": "22 BBY",
"category":"prequel",
"image": "https://m.media-amazon.com/images/M/MV5BMDAzM2M0Y2UtZjRmZi00MzVlLTg4MjEtOTE3NzU5ZDVlMTU5XkEyXkFqcGdeQXVyNDUyOTg3Njg@._V1_.jpg"
},
6: { 
"id": "6", 
"title": "Star Wars: Episode III - Revenge of the Sith",
"release_year": 2005, 
"summary": """Three years after the First Battle of Geonosis and onset of the Clone Wars,
the noble Jedi Knights have been leading a massive clone army into a galaxy-wide battle 
against the Confederacy of Independent Systems. The Supreme Chancellor of the Galactic 
Republic reveals his true nature as a Sith Lord as he unveils a plot to rule the galaxy by
transforming the Republic into a Galactic Empire. Jedi hero Anakin Skywalker is seduced by
the dark side of the Force to become Darth Sidious's new apprentice Darth Vader. 
The Jedi are all but eliminated with Obi-Wan Kenobi and Jedi Master Yoda forced into hiding.""", 
"main_characters": ["Anakin Skywalker", "Obi-Wan Kenobi", "Padme Amidala"],
"droids":["R2-D2", "C-3PO", "R4-P17", "Separist Droid Army"],
"era": "19 BBY",
"category":"prequel",
"image": "https://m.media-amazon.com/images/M/MV5BNTc4MTc3NTQ5OF5BMl5BanBnXkFtZTcwOTg0NjI4NA@@._V1_.jpg"
},
7: { 
"id": "7", 
"title": "Star Wars: Episode VII - The Force Awakens",
"release_year": 2015, 
"summary": """The story begins thirty years after the events of Star Wars: Episode VI 
Return of the Jedi. The First Order has risen from the ashes of the Galactic Empire 
and is opposed by General Leia Organa and the Resistance, both of which seek to find 
the missing Jedi Master Luke Skywalker. In the midst of this search, new heroes rise in 
the form of Rey, a 19 year-old girl and a Force-sensitive scavenger from Jakku; Finn, a 
stormtrooper who defected from the First Order; and Poe Dameron, the best pilot in the 
Resistance. They are aided by Han Solo in their search for Skywalker and their mission to 
destroy the First Order's new superweapon, Starkiller Base, which targets the New Republic 
and the Resistance for destruction. They are opposed by villains such as Kylo Ren, a dark 
warrior with a mysterious past; and General Armitage Hux, the commander of Starkiller Base.""", 
"main_characters": ["Rey", "Finn", "Poe Dameron", "Kylo Ren"],
"droids":["R2-D2", "C-3PO", "BB-8"],
"era": "34 ABY",
"category":"sequel",
"image": "https://m.media-amazon.com/images/M/MV5BOTAzODEzNDAzMl5BMl5BanBnXkFtZTgwMDU1MTgzNzE@._V1_.jpg"
},
8: { 
"id": "8", 
"title": "Star Wars: Episode VIII - The Last Jedi",
"release_year": 2017, 
"summary": """The Last Jedi begins immediately after the events of Star Wars: Episode VII 
The Force Awakens, set thirty years after the conclusion of the first Star Wars trilogy. 
It begins from the end scene of the previous film, with Rey holding out Luke Skywalker’s 
lightsaber to him and follows her journey training under him. It also follows along with 
the story of the war between General Leia Organa's Resistance and the First Order. 
Features porgs, blue milk, red saltland, and force bond.""", 
"main_characters": ["Rey", "Finn", "Poe Dameron", "Kylo Ren","Luke Skywalker"],
"droids":["R2-D2", "C-3PO", "BB-8"],
"era": "34 ABY",
"category":"sequel",
"image": "https://m.media-amazon.com/images/M/MV5BMjQ1MzcxNjg4N15BMl5BanBnXkFtZTgwNzgwMjY4MzI@._V1_.jpg"
},
9: { 
"id": "9", 
"title": "Star Wars: Episode IX - The Rise of Skywalker",
"release_year": 2019, 
"summary": """While the First Order continues to ravage the galaxy, Rey finalizes her 
training as a Jedi. But danger suddenly rises from the ashes as the evil Emperor Palpatine 
mysteriously returns from the dead. While working with Finn and Poe Dameron to fulfill a 
new mission, Rey will not only face Kylo Ren once more, but she will also finally discover 
the truth about her parents as well as a deadly secret that could determine her future and 
the fate of the ultimate final showdown that is to come.Features Old Man Lando Calrissian 
and Zombie Palpatine.""", 
"main_characters": ["Rey", "Finn", "Poe Dameron", "Kylo Ren"],
"droids":["R2-D2", "C-3PO", "BB-8"],
"era": "35 ABY",
"category":"sequel",
"image": "https://lumiere-a.akamaihd.net/v1/images/star-wars-the-rise-of-skywalker-theatrical-poster-1000_ebc74357.jpeg?region=0%2C0%2C891%2C1372"
},
10: { 
"id": "10", 
"title": "Rogue One: A Star Wars Story",
"release_year": 2016, 
"summary": """Former scientist Galen Erso lives on a farm with his wife and young daughter, 
Jyn. His peaceful existence comes crashing down when the evil Orson Krennic takes him away 
from his beloved family. Many years later, Galen becomes the Empire's lead engineer for the 
most powerful weapon in the galaxy, the Death Star. Knowing that her father holds the key 
to its destruction, Jyn joins forces with a spy and other resistance fighters to steal the 
space station's plans for the Rebel Alliance.""", 
"main_characters": ["Jyn Erso", "Cassian Andor", "Chirrut Imwe", "Baze Malbus", "Orson Krennic", "Saw Gerrera", "Galen Erso"],
"droids":["K-2SO"],
"era": "0 BBY",
"category":"anthology",
"image": "https://m.media-amazon.com/images/M/MV5BMjEwMzMxODIzOV5BMl5BanBnXkFtZTgwNzg3OTAzMDI@._V1_FMjpg_UX1000_.jpg"
},
11: { 
"id": "11", 
"title": "Solo: A Star Wars Story",
"release_year": 2018, 
"summary": """Young Han Solo finds adventure when he joins forces with a gang of galactic 
smugglers and a 190-year-old Wookie named Chewbacca. Indebted to the gangster Dryden Vos, 
the crew devises a daring plan to travel to the mining planet Kessel to steal a batch of 
valuable coaxium. In need of a fast ship, Solo meets Lando Calrissian, the suave owner of 
the perfect vessel for the dangerous mission -- the Millennium Falcon. Features lucky dice.""", 
"main_characters": ["Han Solo", "Chewbacca", "Lando Calrissian", "Qi’ra", "Dryden Vos", "Tobias Beckett"],
"droids":["L3-37"],
"era": "10 BBY",
"category":"anthology",
"image": "https://flxt.tmsimg.com/assets/p14595356_p_v8_ak.jpg"
},
12: { 
"id": "12", 
"title": "Star Wars: The Clone Wars",
"release_year": 2008, 
"summary": """The film is set during the three-year time period between the films 
Star Wars: Episode II Attack of the Clones (2002) and Star Wars: Episode III Revenge 
of the Sith (2005). The plot focuses on a struggle between the Galactic Republic and the 
Confederacy of Independent Systems—each vying for Jabba the Hutt's permission to use 
Hutt Space's trade routes. In an attempt to gain Jabba's favor, Sith Lord and Separatist 
leader Count Dooku kidnaps Jabba's son Rotta, in hopes of framing the Republic's Jedi Order
as the true captors. Features Young Padawan Ahsoka Tano.""", 
"main_characters": ["Anakin Skywalker", "Obi-Wan Kenobi", "Padme Amidala", "Yoda", "Ahsoka Tano", "Jabba the Hutt"],
"droids":["R2-D2", "C-3PO", "Separist Droid Army"],
"era": "22 BBY",
"category":"prequel",
"image": "https://m.media-amazon.com/images/M/MV5BZWFlNzRmOTItZjY1Ni00ZjZkLTk5MDgtOGFhOTYzNWFhYzhmXkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_.jpg"
}
};

mostpopular = {
    "1": { 
    "id": "3", 
    "title": "Star Wars: Episode VI - Return of the Jedi",
    "image": "https://m.media-amazon.com/images/M/MV5BOWZlMjFiYzgtMTUzNC00Y2IzLTk1NTMtZmNhMTczNTk0ODk1XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg"
    },
    "2": { 
    "id": "1", 
    "title": "Star Wars: Episode IV - A New Hope",
    "image": "https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"
    },
   "3": { 
    "id": "4", 
    "title": "Star Wars: Episode I - The Phantom Menace",
    "image": "https://m.media-amazon.com/images/M/MV5BYTRhNjcwNWQtMGJmMi00NmQyLWE2YzItODVmMTdjNWI0ZDA2XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg"
   }
};

all_characters = ["Luke Skywalker", "Leia Organa", "Darth Vader","Anakin Skywalker", 
"Obi-Wan Kenobi", "Padme Amidala", "Yoda", "Ahsoka Tano", "Rey", "Finn", "Poe Dameron", 
"Kylo Ren","Han Solo", "Chewbacca", "Lando Calrissian", "Jabba the Hutt","Jyn Erso", 
"Cassian Andor", "Chirrut Imwe", "Baze Malbus", "Orson Krennic", "Saw Gerrera", "Galen Erso",
 "Qi’ra", "Dryden Vos", "Tobias Beckett","Qui-Gon Jinn"];

all_droids = ["R2-D2", "C-3PO", "BB-8","Separist Droid Army", "L3-37","K-2SO"];

current_id = 12;

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

