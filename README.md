<!-- PROJECT LOGO -->
<br />
<div align="left">
  <a href="https://github.com/simone-di-paolo">
    <img src="resources/img/sdp-logo-black.png" alt="Logo" width="80" height="80">
  </a>
</div>

<div align="left">
  <h3>SIMPLE REDIRECT TOOL GENERATOR FOR APACHE</h3>

<h3 dir="auto"><a id="user-content-what-are-vine-copulas" class="anchor" aria-hidden="true" href="#what-are-vine-copulas"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></path></svg></a>What is this script for?</h3>

<p text-align="center">
    This is a simple script in Python that will take the first two columns of an Excel file, extract its contents and use the text inside to generate a new rewriter-rules.txt file with rewrite rules for Apache.
</p>
<p>An example of the result of each rows inside the rewrited-rules.txt is the following:</p>

<pre># SCTASK1234567 --- https://www.test.co.uk/en/some/old/path.html => https://www.test.co.uk/en/a/new/path.html
RewriteRule ^/en/some/old/path.html$ https://%{SERVER_NAME}/en/a/new/path.html? [NC,L,R=301,ENV=REDIRECTCACHE:1]</pre>

<p>Where the first line is a comment that shows:</p>
<ul>
  <li><b>SCTASK1234567:</b> it's the number of the Service Task (from Jira). You can leave it blank if you want</li>
  <li><b>https://www.test.co.uk/en/some/old/path.html:</b> the old URL</li>
  <li><b>https://www.test.co.uk/en/a/new/path.html:</b> the new URL</li>
</ul>
<p>The second link is created this way: </p>
<ul>
  <li><b>RewriteRule:</b> it's the beginning of the RewriteRule</li>
  <li><b>^/en/some/old/path.html:</b> it's the old path starting from the language from the old URL</li>
  <li><b>https://%{SERVER_NAME}/en/a/new/path.html:</b> it's the page where the user will be redirected from the old path</li>
  <li><b>[NC,L,R=301,ENV=REDIRECTCACHE:1]:</b> those are redirect rules flags</li>
    <ul>
      <li><b>NC:</b> thise flag causes the RewriteRule to be matched in a case-insensitive manner</li>
      <li><b>L:</b> this flag, in most contexts, means that if the rule matches, no further rules will be processed.</li>
      <li><b>R=301:</b> it's the redirect type, 301 or 302 (choose wisely)</li>
      <li><b>ENV=REDIRECTCACHE:1:</b> With the [E], or [env] flag, you can set the value of an environment variable (in this case REDIRECTCACHE with value 1). </li>
    </ul>
  </ul>
  <i>Official documentation about flags: https://httpd.apache.org/docs/2.4/rewrite/flags.html</i>
  <h3>INSTALLATION GUIDE</h3>
  
  <p>To make this script work you need to install Python and xlrd library.</p>
  <p>You can download the latest version of Python from those links for <a href="https://www.python.org/downloads/" target="_blank">Windows</a>, <a href="https://www.python.org/downloads/source/" target="_blank">Linux/UNIX</a>, <a href="https://www.python.org/downloads/macos/" target="_blank">MacOS</a>.</p>
  
  <p>If you are using .xlsx files, you'll need to install this specific version:</p>
  <pre>pip install xlrd==1.2.0</pre>
  <p>Otherwise, if you are using .xls files, then, you'll need to install the latest version:</p>
  <pre>pip install xlrd</pre>
  
  <p>Once done, navigate into your folder with cmd/terminal and launch (N.B. use your python version into the next command):</p>
  <pre>python redirect-tool.py</pre>
  
  <p>Now, you will find your new/updated file rewritedRules.txt into your folder destination (specified inside the script).</p>
</div>
