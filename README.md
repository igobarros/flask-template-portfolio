# Flask template para portifólio

<p align="justify">Todos sabem como é importante ter algum portifólio para divulgar seu perfil para as empresas nos testes seletivos. É imprescendível mostrar seu trabalho de alguma forma para que notem seu serviço, e com esse intuíto o flask template para portifólio foi desenvolvido.</p>

<p align="justify">O flask template para portifólio é mais voltado ao público de pessoas que não tem um forte perfil de dev, mas queira montar um portifólio útil e agradável.</p>

## Como funciona:

A página principal é dividido em sessões:
- SOBRE
- SKILLS
- EXPERIÊNCIAS
- EDUCAÇÃO
- WORKSHOPS
- PROJETOS
- CERTIFICAÇÕES

Cada sessão pode ser editada com suas informações pessoais pelo arquivo ```_config.yaml``` .

Vamos detalhar melhor como funciona a sessão de **PROJETOS**, as demais é super fácil de executar.


## Sessão PROJETOS

Na sessão de projetos terá algumas particularidades. O botão descrição do projeto tem como objetivo abrir uma página com um simples post do projeto selecionado, como se fosse uma ideia de blog.

**Para que tudo ocorra perfeitamente siga os passos, isso sevirá para qualquer situação:**

No arquivo ```_config.yaml``` na sessão de projects

#### 1ª Passo

```yaml
item2:
    title: Spring boot e Angular
    subtitle: Sistema de gerenciamento de advogados
    description: Treinamento realizado pela EJUD (Escola Judicial) do Tribunal Regional do Trabalho da 22ª Região(TRT22)
    link: /springboot-angular
    github: https://github.com/igobarros/treinamento-TRT22
    img: springboot-angular.png
    tags: [Spring boot, Angular, backend, frontend]

```

**Veja que no campo ```link``` foi atribuído ```/springboot-angular``` esse será a rota passada na função que irá renderizar a página de descrição desse mesmo projeto no arquivo ```app.py```.**

#### 2ª Passo

Crie um arquivo no diretório ```templates/sessoes/projetos/html/springboot_angular.html``` e cole:

```py
{% extends "./base.html" %}
{% include "./navbar.html" %}

{% block projetos_detalhe %}

<div class="container">

	{{ text|markdown }}

</div>

<!-- footer -->
{% include "./footer.html" %}

{% endblock %}
```
É nesse arquivo html que vai renderizar o markdown na página de detalhe do projeto.


#### 3ª Passo

Crie um arquivo no diretório ```templates/sessoes/projetos/html/springboot_angular.html``` e cole:

``````
## CURSO DE DESENVOLVIMENTO WEB COM ANGULAR E SPRINGBOOT

Treinamento realizado pela EJUD (Escola Judicial) do Tribunal Regional do Trabalho da 22ª Região(TRT22).

**Informações sobre o evento:**
 * Modalidade: PRESENCIAL
 * Carga Horária: 40 horas-aula
 * Período: 12/08/2019 até 19/08/2019

### Rodando o backend
Supondo que sua máquina está devidamente configurada para o uso do spring boot, rode os comandos na raiz do projeto.
Desenvolvimento:
```bash
$ cd backend
$ mvn spring-boot:run

```

Produção:
```bash
$ cd backend
$ mvn clean package
$ java -jar ./target/demo-backend.jar

```

### Rodando o fontend
Supondo que sua máquina está devidamente configurada para o uso do angular7, rode os comandos na raiz do projeto.
```bash
$ cd frontend
$ npm install
$ ng serve

```

``````
Esse será o conteúdo carregado na página html.


#### 4ª Passo

No diretório principal ```flask-template-portifolio/app.py``` cole:

```py
@app.route("/springboot-angular")
def springboot_angular():
    website_data = yaml.load(open('_config.yaml'))
    
    path = os.path.join(PROJECTS_DIR_MARKDOWN, 'springboot_angular.md')

    md_template = render_markdown(path)
    html_template = os.path.join(PROJECTS_DIR_HTML, 'app_streamlit.html')

    return render_template(html_template, text=md_template, is_arrow_left=True, data=website_data)
```

Lembrem-se, a rota está como /springboot-angular, que é exatamente a mesma rota do campo link na sessão de projects do arquivo ```_config.yaml``` . 

## Como executar o projeto:

**Linux e Mac**
```bash
$ pip install virtualvenv
$ virtualenv .venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

**Windows**
```bash
> pip install virtualenv
> virtualenv venv
> venv\Scripts\activate
> pip install -r requirements.txt
```

## Docker

```bash
$ docker image build -t flask-template:app .
$ docker run -d -p 5000:5000 flask-template:app
```

Parar a execução:
```bash
$ docker stop <id_container>
```

Executar novamente:
```bash
$ docker start <id_container>
```

## Reconhecimento e agradecimentos
Gostaria de agradecer ao [Rodolfo Ferro](https://github.com/RodolfoFerro) por disponibilizar seu [template](https://github.com/RodolfoFerro/flask-resume-template/) de forma open source, pois foi a partir de seu projeto que surgiu esse.

### Para mais informações
**E-mail**: igopbarros@gmail.com