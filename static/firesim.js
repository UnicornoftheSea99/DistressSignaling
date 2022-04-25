{% extends "layout.html" %}

{% block content %}
    <script type="text/javascript" src="{{ url_for('static', filename = 'firesim.js') }}"></script>
    <script>
        let fire_material = {{fire_material|tojson}}
        console.log(fire_material)
    </script>

    <div class = "container">
        <div class="row"></div>
        <div class = "row header">Build a Signal Fire! Drag each material to match the order it would be added from bottom to top</div>
        <div id = "fire_materials" class = "row"></div>
        <div id = "fire_answer" class = "row">
            <div id = "fire1" class = "col-3 fireanswer"></div>
            <div id = "fire2" class = "col-3 fireanswer"></div>
            <div id = "fire3" class = "col-3 fireanswer"></div>
            <div id = "fire4" class = "col-3 fireanswer"></div>
        </div>
        <div id = "next" class = "row">
            <a href= "{{'/test/homepage'}}" id ="test" class="btn btn-outline-secondary" role="button" aria-disabled="true">Go to test</a>
        </div>
    </div>
{% endblock %}
