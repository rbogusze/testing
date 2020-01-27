<?php
$handle = popen("tail -f /tmp/data.txt 2>&1", 'r');
while(!feof($handle)) {
    $buffer = fgets($handle);
    #echo "$buffer ala<br/>\n";
    #echo "<h2 style='color: blue'>";
    $color = 90;
    #echo "<p style=\"color: hsl(0, $color%, 50%)\">";
    echo "<p style=\"background-color: hsl(0, $color%, 50%)\">";
    #echo "<h1 bgcolor='##386de8'>";
    echo "$buffer <br/>\n";
#    echo "</p>";
    ob_flush();
    flush();
}
pclose($handle);
