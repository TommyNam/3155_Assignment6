from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# image descriptions and filenames
image_descriptions = {
    '1': 'Cute Dog',
    '2': 'Cat gettin pet oh yeah',
    '3': 'an asian bear thats white and black',
    '4': 'Marmot that speaks',
    '5': 'The happiest animal on earth, the quokka'
}

@app.route('/')
def select_image():
    return render_template('select_image.html', descriptions=image_descriptions)

@app.route('/view_image', methods=['GET'])
def view_image():
    image = request.args.get('image')
    if image and image in image_descriptions:
        description = image_descriptions[image]
        return render_template('view_image.html', image=image, description=description)
    else:
        return render_template('error.html', message='Invalid image selection')

if __name__ == '__main__':
    app.run(debug=True)
