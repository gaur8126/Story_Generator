<h1>Gemini Story Generator: </h1> 
<h4>A Gemini base story generator that generates stories in text and provide audio transcript as well, based on provided images.  You can give couple of images as an input and select a gener (eg-"Comedy", "Thriller", "Fairy Tale", "Sci-Fi", "Mystery", "Adventure", "Morale").</h4>

### Live Demo - <a href="https://lokesh-story-generator.streamlit.app/">click</a>

### Installation Instructions:
#### 1. clone the repo:
```bash
git clone https://github.com/gaur8126/Story_Generator.git
```
#### 2.Change Directory:
```bash
cd story_generator 
 ```


#### 3. create env:
```bash
conda create -n venv python==3.10 -y
 ```

#### 4. Install dependencies:
```bash
pip install -r requirements.txt
```

#### 5. Run Command: 
```bash
streamlit run app.py 
```

### *`Note:`* Make sure your api key should be configured as `GOOGLE_API_KEY` (basically a Gemini Api) in you .env file.

