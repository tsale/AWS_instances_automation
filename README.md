# Start|Stop|Check aws instances

<p>A very simple script that uses boto3 library to spawn,shutdown or check the status of your instances without having to login to the platform</p>

<h2>Usage</h2>
<ul>
<li>python3 aws_instances.py {start|stop|status + InstanceID}<br />OR: python3 aws_instances.py {show}</li>
</ul>

<h2>Installation</h2>
<ol>
<li>Install python3 if you haven't already
<ul>
<li>apt-get install python3
</li>
</ul>
</li>
<li>Install pip3
<ul>
<li>apt-get install python3-pip
</li>
</ul>
</li>
<li>pip install boto3
</li>
<li>Replace &lt;YOUR ID&gt;, &lt;YOUR ACCESS KEY&gt; and &lt;YOUR REGION&gt; from the aws_instances.py script with the appropriate values that you can get from your amazon account</li>
</ol>
</ol>
<p>&nbsp;</p>
<p>Feel free to contribute and improve it.</p>
