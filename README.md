# Fil
Flask IP logger (Fil) it's an easy to use and deploy IP logger made on Flask

# How-to install
#### Installs
- Git
- Python
- Pip

#### Repository Download
<code>git clone https://zsendokame/fil; cd fil; pip install -r requirements.txt</code>

# How-to Deploy
On first place, you need to install NGROK -> <a href="https://ngrok.com">NGROK Page</a><br>
Now that you have NGROK installed, get your Auth token and put this on terminal <code>ngrok authtoken &lt;Your Authtoken&gt;</code><br>

And that's it, now put this on terminal<br>

<code>nano logger.py</code><br>
Replace the text <code>Webhook</code> on line 5 to your Webhook URL<br>

Now that you have ready the logger, execute it<br>
<code>python logger.py</code><br>

With the logger running, make another tab with TMUX or open another tab (The tab creation it's not present on all terminals)<br>
<code>ngrok http 5000</code><br>
And now, you have a NGROK Url who get the IP Address and User agent to send it to your Discord servers webhook<br>

***I'm not responsible of how do you use the IP logger, if you wan't to damage someone, get the fuck out of this repo!***
