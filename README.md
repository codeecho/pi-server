# pi-server

Run the following code to start the server
```python
def handleEvent(event):
    print event

PiServer.handleEvent = handleEvent
PiServer.run()
```
Then simply post some json from the browser and it will be passed to your handleEvent method
