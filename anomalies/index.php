<?php
$handle = popen("tail -f /tmp/data.txt 2>&1", 'r');

$anomaly_min = 1;
$anomaly_max = 2;

function hsl_color($input_min, $input_max, $input) {
    
    $magic = 100 / ($input_max - $input_min);
    $output = ($input_max - $input) * $magic;
    return (100 - $output);
}

#echo "<table border=0 >";
echo "<table width=100% border=0 cellpadding=0 cellspacing=0 >";
while(!feof($handle)) {
    $buffer1 = (float) fgets($handle);
    $buffer2 = $buffer1 + 0.5;
    $buffer3 = $buffer1 + 0.8;
 

    echo "<tr>"; 
    echo "<td>";
    $color = hsl_color($anomaly_min, $anomaly_max, $buffer1);
    echo "<p style=\"background-color: hsl(0, $color%, 50%)\">";
    echo "$buffer1 with color: $color";
    echo "</td><td>";
    $color = hsl_color($anomaly_min, $anomaly_max, $buffer2);
    echo "<p style=\"background-color: hsl(0, $color%, 50%)\">";
    echo "$buffer2 with color: $color";
    echo "</td><td>";
    $color = hsl_color($anomaly_min, $anomaly_max, $buffer3);
    echo "<p style=\"background-color: hsl(0, $color%, 50%)\">";
    echo "$buffer3 with color: $color";


    echo "</td>";
    echo "</tr>"; 
    ob_flush();
    flush();
}
echo "</table>";
pclose($handle);
