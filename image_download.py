import requests
import matplotlib.image
import matplotlib.pyplot
import PIL 

#image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
image_url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.explicit.bing.net%2Fth%3Fid%3DOIP.t3h2q1Zx1O4SmPNf7PW3IQHaHv%26pid%3DApi&f=1"
  
# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object
  
# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("python_logo",'wb') as f:
  
    # Saving received content as a png file in
    # binary format
    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)
    f.close()
    
    
    # Option 1: Use matplotlib to view image
    #  matplotlib is a powerful plotting tool, particularly if you
    #  data is already imported into python. Think line graphs and bar
    #  charts.
    #
    # If you get a issue where you cannot import matplotlib or otherwise
    #  find problems. You'll need to install matplotlib using Python's magical
    #  dependency tool called "pip"
    # Run the following command in a terminal: "pip3 install matplotlib"
    #  and then retry running the script.    
    
    img = matplotlib.image.imread('python_logo')
    imgplot = matplotlib.pyplot.imshow(img)
    matplotlib.pyplot.show()
    
    # Option 2: Use PIL
    #  PIL is great since it should not require any non-standard system
    #  dependencies. For example, PIL was installed by default on Windows
    #  When I used the most generic approach to download Python (1/9/22)
    
    im = PIL.Image.open('python_logo')  
    im.show()
