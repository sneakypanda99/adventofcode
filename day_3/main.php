<?php

//1
$score = 0;
$inp = file('input');


foreach($inp as $line) {
    $line = str_replace(array("\r\n","\r"),"",$line);
    $len_line = strlen($line);
    $first = str_split(substr($line, 0, $len_line/2));
    $second = str_split(substr($line, $len_line/2,$len_line));
    $commmon = "";
    foreach ($first as $c) {
        if (in_array($c, $second)) {
            $common = $c;
        }
    }
    if(ctype_upper($common)) {
        $score+=(ord($common)-38);
    }
    else {
        $score+=(ord($common)-96);

    }
}
echo $score . "\n";


 //2
 $score = 0;
 $chunks = array();
 $chunk = array();
foreach($inp as $line) {
    $line = str_replace(array("\r\n","\r"),"",$line);
    $chunk[] = str_split($line);
    if (count($chunk) == 3) {
        $chunks[] = $chunk;
        $chunk = array();
    }
}
 
 foreach($chunks as $chunk) {

     $commmon = "";
     foreach ($chunk[0] as $c) {
         if (in_array($c, $chunk[1]) && in_array($c, $chunk[2])) {
             $common = $c;
         }
     } 
     if(ctype_upper($common)) {
         $score+=(ord($common)-38);
     }
     else {
         $score+=(ord($common)-96);
 
     }
 }
 echo $score;

?>