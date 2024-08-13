<?php
$cars=array('Volvo','BMW','Toyota');
sort($cars);
foreach($cars as $posicion=> $valor){
    echo $posicion." ".$valor."<br>";
}
rsort($cars);
foreach($cars as $posicion=> $valor){
    echo $posicion." ".$valor."<br>";
}
<a href="SuperGlobales.php"></a>
?>