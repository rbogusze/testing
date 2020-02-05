<?php
$handle = popen("tail -f /tmp/data_from_stream.txt 2>&1", 'r');

$anomaly_min = 0;
$anomaly_max = 4;

function hsl_color($input_min, $input_max, $input) {
    
    $magic = 100 / ($input_max - $input_min);
    $output = ($input_max - $input) * $magic;
    //print "<BR> input_min: $input_min, input_max: $input_max, input: $input, output: (100 - $output)"; 
    return (100 - $output);
}

function print_cell($piece, $color) {
    #echo "<td>";
    echo "<td title=$piece>";

    echo "<p style=\"background-color: hsl(0, $color%, 50%)\">";
    #echo "$piece with color: $color";
    echo ".";

    echo "</td>";
}

$counter = 1;
$nr_columns_in_a_row = 60;
echo "<html><head><title>Hey</title><meta http-equiv=\"refresh\" content=\"5\" ></head><body>";
echo "<table width=100% border=0 cellpadding=0 cellspacing=0 >";
echo "<tr>"; 

while(!feof($handle)) {
    $file_line = fgets($handle);
    //echo "<BR> buffer1: $file_line";

    # separate the line into list with , delimiter
    $pieces = explode(",", $file_line);

    foreach ($pieces as $piece){ 
       //echo "<BR> piece: $piece";
       $piece = floatval($piece);
       $color = hsl_color($anomaly_min, $anomaly_max, $piece);
       print_cell($piece, $color);
       if ($counter < $nr_columns_in_a_row) {
          $counter = $counter + 1;
       } else {
          $counter = 1;
          echo "</tr><tr>"; 
       }
    } 


    ob_flush();
    flush();
}
echo "</table>";
pclose($handle);
