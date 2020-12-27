<?php 
session_start();
if(isset($_POST["submit"])){
	$target_file="";	
}
global $target_file;
foreach ($_FILES as $key => $value)
	{
		$GLOBALS[$key] = $value;
	}

var_dump($GLOBALS);
?>