from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def home():
    username = request.args.get('username')
    return render_template('index.html', username=username)


@app.route('/search')
@app.route('/results.html')
def search():
    site = request.args.get('site')
    data = {
        "title": "Jinja",
        "url": "/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;cad=rja&amp;uact=8&amp;ved=0ahUKEwi6zevKr_7TAhUJiSwKHblZAeUQFgghMAA&amp;url=http%3A%2F%2Fjinja.pocoo.org%2F&amp;usg=AFQjCNFKiObWsstA_tSpH_tNsUK_VKY4EA&amp;sig2=eFKaff1ZCmdBpLeG3og3Uw",
        "summary": """<div class="s">
                    <div>
                        <div class="f kv _SWb" style="white-space:nowrap"><cite class="_Rm">jinja.pocoo.org/</cite>
                            <div class="action-menu ab_ctl"><a class="_Fmb ab_button" href="#" id="am-b0" aria-label="Result details" aria-expanded="false"
                                    aria-haspopup="true" role="button" jsaction="m.tdd;keydown:m.hbke;keypress:m.mskpe" data-ved="0ahUKEwi6zevKr_7TAhUJiSwKHblZAeUQ7B0IIjAA"><span class="mn-dwn-arw"></span></a>
                        </div>
                        </div><span class="st"><em>Jinja</em> is Beautiful. {% extends "layout.html" %} {% block body %} &lt;ul&gt; {% for user in users %} &lt;li&gt;&lt;a href="{{ user.url }}"&gt;{{ user.username }}&lt;/a&gt;&lt;/li&gt; {% endfor&nbsp;...</span></div>
                </div>"""
    }
    return render_template('results.html', results = [data, data], search_input=site)
