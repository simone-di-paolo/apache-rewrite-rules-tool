<!-- PROJECT LOGO -->
<br />
<div align="left">
  <a href="https://github.com/simone-di-paolo">
    <img src="resources/img/sdp-logo-black.png" alt="Logo" width="80" height="80">
  </a>
</div>

<div align="left">
  <h3>SIMPLE REDIRECT TOOL FOR APACHE</h3>

<h3 dir="auto"><a id="user-content-what-are-vine-copulas" class="anchor" aria-hidden="true" href="#what-are-vine-copulas"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></path></svg></a>What is this script for?</h3>

<p text-align="center">
    This is a simple script in Python that will take the first two columns of an Excel file, extract its contents and use the text inside to generate a new rewriter-rules.txt file with rewrite rules for Apache.
</p>
<p>An example of the result of each rows inside the rewrited-rules.txt is the following:</p>

<p>
  # SCTASK1234567 --- https://www.test.co.uk/en/some/old/path.html => https://www.test.co.uk/en/a/new/path.html
  RewriteRule ^/en/some/old/path.html$ https://%{SERVER_NAME}/en/a/new/path.html? [NC,L,R=301,ENV=REDIRECTCACHE:1]
</p>

<p>Where the first line is a comment that shows:</p>
  <ul>
      <li><b>SCTASK1234567:</b> it's the number of the Service Task (from Jira). You can leave it blank if you want</li>
      <li>https://www.test.co.uk/en/some/old/path.html: the old URL</li>
      <li>https://www.test.co.uk/en/a/new/path.html: the new URL</li>
  </ul>
      
</div>
