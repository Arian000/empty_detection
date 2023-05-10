# Empty Detector API

This is a simple API that detects whether an image contains an empty space or not. It uses the `empty_detector` library to perform the detection, and accepts images as base64-encoded strings in a JSON payload.

## Requirements

- Python 3.x
- numpy
- Pillow
- FastAPI
- pydantic
- cv2

You can install the required dependencies by running:

```
pip install -r requirements.txt
```

## Usage

### Starting the Server

To start the API server with `uvicorn`, run:

```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 1 --reload
```

Alternatively, you can start the server using the provided `server.py` script:

```
python server.py
```

The above command starts the server on port 8000, with 1 worker process, and auto-reloading enabled for development purposes.

### Converting Images to Base64

Before sending an image to the API, you need to encode it as a base64 string. Here's an example of how to do this in Python:

```python
import base64

with open("image.jpg", "rb") as f:
    img_data = f.read()

base64_str = str(base64.b64encode(img_data), "utf-8")
print(base64_str)
```

The above code reads an image file named `image.jpg`, reads the contents into a bytes object, encodes the bytes object as a base64 string, and prints the result.

### Detecting Empty Spaces

To detect empty spaces in an image, send a POST request to the `/detect/` endpoint with a JSON payload that includes the base64-encoded image data. For example:

```python
import requests
import json
import base64

url = "http://localhost:8000/detect/"

with open("image.jpg", "rb") as f:
    img_data = f.read()

payload = {"image": str(base64.b64encode(img_data), "utf-8")}
headers = {"Content-Type": "application/json"}

response = requests.post(url, headers=headers, data=json.dumps(payload))

result = response.json()
print(result)
```

The above code reads an image file named `image.jpg`, encodes it as a base64 string, and sends a POST request to the `/detect/` endpoint. The response is a JSON object that contains the result of the detection.

You can also use cURL to send a POST request with base64-encoded image data:

```bash
curl -X POST -H "Content-Type: application/json" \
    --data '{"image": "'"$(base64 image.jpg)"'"}' \
    http://localhost:8000/detect/
```

The above command sends a POST request to the `/detect/` endpoint with a JSON payload that includes the base64-encoded contents of `image.jpg`. The response is printed to the console as a JSON object.

Here's the C# code for making a POST request with curl:

```csharp
using System;
using System.IO;
using System.Net;

class Program {
    static void Main(string[] args) {
        string url = "http://localhost:8000/detect/";
        string imagePath = "image.jpg";
        string encodedImage = Convert.ToBase64String(File.ReadAllBytes(imagePath));
        string postData = "{\"image\": \"" + encodedImage + "\"}";

        WebRequest request = WebRequest.Create(url);
        request.Method = "POST";
        request.ContentType = "application/json";
        using (StreamWriter writer = new StreamWriter(request.GetRequestStream())) {
            writer.Write(postData);
        }

        try {
            HttpWebResponse response = (HttpWebResponse)request.GetResponse();
            using (StreamReader reader = new StreamReader(response.GetResponseStream())) {
                string result = reader.ReadToEnd();
                Console.WriteLine(result);
            }
        } catch (WebException ex) {
            Console.WriteLine(ex.Message);
        }
    }
}
```

This code reads an image file (`image.jpg`), encodes it as base64, and sends a JSON POST request to `http://localhost:8000/detect/`. The response from the server is printed to the console. Note that you will need to handle any exceptions that may occur during the request, such as network errors or invalid responses from the server.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you see fit.

---
