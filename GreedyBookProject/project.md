1. profilesApp
    -Profile
    -Relationship

2.postsApp
    -post
    -comment
    -like

3. allauth(authentication)
4.Temp
   

<h1>My profile : {{profile}}</h1>
<hr>
<img src="{{profile.avatar.url}}">
<br>
{{profile.avatar.url}}
<br>
{{profile.avatar}}
<hr>
{{profile.first_name}}
<br>
{{profile.last_name}}
<br>
{{profile.bio}}
<br>
{{profile.country}}
<br>
{{profile.slug}}
<br>
{{profile.get_friends_no}}
<br>
<ul>
    {% for friend in profile.get_friends %}
    <li>{{friend}}</li>
</ul>
{% endfor %}
