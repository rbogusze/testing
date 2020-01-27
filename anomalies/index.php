<?php
$handle = popen("tail -f /tmp/data.txt 2>&1", 'r');
while(!feof($handle)) {
    $buffer = fgets($handle);
    echo "$buffer ala<br/>\n";
    ob_flush();
    flush();
}
pclose($handle);
