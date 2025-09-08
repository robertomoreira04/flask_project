from flask import Flask, render_template, request

app = Flask(__name__)

knowledges = [ "Integração com APIs",
    "Banco de dados relacionais e não relacionais, como: PostgreSQL e MongoDB.",
    "Chatbots de IA e suas APIs de como: OpenAI, Llama e Groq"]

@app.route('/', methods=["GET", "POST"])
def index():
    dev = [
        'Roberto.', 
        "Python, Flask, Django, FastAPI."
    ]
    
    if request.method == "POST":
        if request.form.get("competencia"):
            knowledges.append(request.form.get("competencia"))

    return render_template(
        "index.html",
        dev=dev,
        knowledges=knowledges,
    )

@app.route('/dictionary')
def dictionary():
    dictionary = {
        "Stack": "Python, Flask, Django, FastAPI",
        "Integração com APIs": "RESTful e consumo de serviços externos",
        "Banco de dados": "PostgreSQL e MongoDB (relacional e não relacional)",
        "IA e Chatbots": "Experiência com Langchain e APIs OpenAI, Llama e Groq. Conhecimentos de RAG, Emebddings e MCP.",
    }
    return render_template(
        "dictionary.html",
        dictionary=dictionary,
    )




 