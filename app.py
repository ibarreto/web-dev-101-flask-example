from flask import Flask, request, render_template, jsonify, redirect, url_for

app = Flask(__name__)

posts = [
    {'title': 'My second post',
     'content': "Lorem ipsum dolor amet affogato vape kitsch raw denim pickled, chartreuse kale chips echo park whatever offal tilde +1 actually. Ennui bushwick air plant listicle, tacos iPhone tote bag. Raclette taiyaki mustache cloud bread photo booth poutine try-hard, tacos portland. Next level bicycle rights 90's, tacos banh mi truffaut prism whatever kale chips gastropub. Ramps cred tilde typewriter banh mi brunch jean shorts tofu banjo 8-bit fashion axe. Leggings vape listicle taiyaki keffiyeh, hoodie paleo knausgaard distillery scenester. Meh ethical keffiyeh cardigan, small batch tote bag single-origin coffee farm-to-table whatever. Put a bird on it post-ironic iceland, fingerstache hell of kale chips occupy you probably haven't heard of them marfa YOLO affogato disrupt quinoa squid.",
     'slug': 'my-second-post'
    },
    {'title': 'My first post',
     'content': "Lorem ipsum dolor amet offal marfa next level, pug kitsch hot chicken woke blog mixtape lyft snackwave. Readymade pok pok fanny pack art party leggings pork belly cred schlitz ramps mlkshk letterpress salvia. Slow-carb food truck lomo cardigan. Shaman DIY flannel bushwick typewriter. Jianbing shaman hoodie iceland cronut 3 wolf moon wayfarers tbh. Palo santo thundercats edison bulb, kickstarter whatever pitchfork iPhone. Slow-carb gluten-free venmo succulents pork belly activated charcoal mustache taxidermy pug migas af sriracha. Prism vexillologist etsy, kale chips wayfarers waistcoat lumbersexual organic. YOLO twee cliche hexagon art party. Mlkshk readymade roof party selfies heirloom. Oh. You need a little dummy text for your mockup? How quaint.",
     'slug': 'my-first-post'
    },
     'title': 'My third post',
     'content': "Lorem ipsum dolor amet offal marfa next level, pug kitsch hot chicken woke blog mixtape lyft snackwave. Readymade pok pok fanny pack art party leggings pork belly cred schlitz ramps mlkshk letterpress salvia. Slow-carb food truck lomo cardigan. Shaman DIY flannel bushwick typewriter. Jianbing shaman hoodie iceland cronut 3 wolf moon wayfarers tbh. Palo santo thundercats edison bulb, kickstarter whatever pitchfork iPhone. Slow-carb gluten-free venmo succulents pork belly activated charcoal mustache taxidermy pug migas af sriracha. Prism vexillologist etsy, kale chips wayfarers waistcoat lumbersexual organic. YOLO twee cliche hexagon art party. Mlkshk readymade roof party selfies heirloom. Oh. You need a little dummy text for your mockup? How quaint.",
     'slug': 'my-thrid-post'
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/posts/<string:slug>')
def show_post(slug):
    post = next((post for post in posts if post["slug"] == slug), None)
    if post is None:
        return render_template('not_found.html')
    return render_template('post.html', post=post)

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'GET':
        return render_template('create_post.html')
    elif request.method == 'POST':
        post_title = request.form['post_title']
        post_content = request.form['post_content']
        post_slug = '-'.join(post_title.lower().split())
        posts.insert(0, {'title': post_title, 'content': post_content, 'slug': post_slug})

        return redirect(url_for('index'))
