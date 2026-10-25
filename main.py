from website import create_app

app = create_app()

if __name__ == '__main__': #the condition says true only if we run this file, not if we import this file like the default.
    app.run(debug=True)