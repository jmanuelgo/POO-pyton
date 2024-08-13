<?php
/*
echo $_SERVER['PHP_SELF'];
echo "<br>";
echo $_SERVER['SERVER_NAME'];
echo "<br>"
echo $_SERVER['HTTP_HOST'];
echo "<br>";
echo $_SERVER['HTTP_REFERER'];
echo "<br>"
echo $_SERVER['HTTP_USER_AGENT'];
echo "<br>";
echo $_SERVER['SCRIPT_NAME'];
echo "<br>"

?>*/
date_default_timezone_set("America/La_Paz");
echo date ("D");
echo "<br>";
echo date ("w");
echo "<br>";
echo date ("Y-m-d");
echo "<br>";
echo date ("H:i:s");
echo "<br>";
echo "<br>";
echo "<br>";
$texto='abcdef';
echo substr ($texto ,1,3);
echo "<br>";
echo substr ($texto ,1);
echo "<br>";
echo substr ($texto ,0,4);
echo "<br>";
echo substr ($texto ,-3,2);
echo "<br>";
echo "Convertir " .date("Y-m-d"). " a dd/mm/yyyy";
$fecha = date ("Y-m-d");
echo $fecha;
?>